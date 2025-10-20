#!/usr/bin/env python
"""Fix template syntax and rebuild all packages with bumped versions."""

import os
import re
import shutil
import json
from pathlib import Path
import subprocess

# Define packages to fix and rebuild
PACKAGES = [
    ("@prompd.io/database-helper", "1.0.0", "1.0.1"),
    ("@prompd.io/documentation", "1.0.0", "1.0.1"),
    ("@prompd.io/meeting-minutes", "1.0.0", "1.0.1"),
    ("@prompd.io/simple-code-gen", "1.0.0", "1.0.1"),
    ("@prompd.io/testing", "1.0.0", "1.0.1"),
]

PRODUCTION_DIR = Path("C:/git/github/Logikbug/prompd-base/production")
PROMPD_CLI = Path("C:/git/github/Logikbug/prompd-cli/cli/python")
OUTPUT_DIR = Path("C:/git/github/Logikbug/prompd-cli/examples")

def fix_template_syntax(content):
    """Fix double-brace {{var}} to single-brace {var} syntax."""
    # Replace {{variable}} with {variable}
    # But preserve {%- if %} and other Jinja2 control structures

    # First protect control structures
    protected = content
    protected = re.sub(r'\{%-', '<<<JINJA_START_STRIP', protected)
    protected = re.sub(r'-%\}', 'JINJA_END_STRIP>>>', protected)
    protected = re.sub(r'\{%', '<<<JINJA_START', protected)
    protected = re.sub(r'%\}', 'JINJA_END>>>', protected)
    protected = re.sub(r'\{#', '<<<JINJA_COMMENT_START', protected)
    protected = re.sub(r'#\}', 'JINJA_COMMENT_END>>>', protected)

    # Now fix double braces
    fixed = re.sub(r'\{\{(\w+)\}\}', r'{\1}', protected)

    # Restore control structures
    fixed = re.sub(r'<<<JINJA_START_STRIP', '{%-', fixed)
    fixed = re.sub(r'JINJA_END_STRIP>>>', '-%}', fixed)
    fixed = re.sub(r'<<<JINJA_START', '{%', fixed)
    fixed = re.sub(r'JINJA_END>>>', '%}', fixed)
    fixed = re.sub(r'<<<JINJA_COMMENT_START', '{#', fixed)
    fixed = re.sub(r'JINJA_COMMENT_END>>>', '#}', fixed)

    return fixed

def bump_version_in_content(content, old_version, new_version):
    """Bump version in YAML frontmatter."""
    return content.replace(f"version: {old_version}", f"version: {new_version}")

def process_package(package_name, old_version, new_version):
    """Process a single package: copy, fix, and rebuild."""
    print(f"\n{'='*60}")
    print(f"Processing {package_name} ({old_version} -> {new_version})")
    print('='*60)

    # Determine source and destination paths
    old_dir = PRODUCTION_DIR / f"{package_name}@{old_version}"
    new_dir = PRODUCTION_DIR / f"{package_name}@{new_version}"

    if not old_dir.exists():
        print(f"ERROR: Source directory not found: {old_dir}")
        return False

    # Copy to new version directory
    if new_dir.exists():
        print(f"Removing existing directory: {new_dir}")
        shutil.rmtree(new_dir)

    print(f"Copying {old_dir} -> {new_dir}")
    shutil.copytree(old_dir, new_dir)

    # Fix all .prmd files
    prmd_files = list(new_dir.rglob("*.prmd"))
    print(f"Found {len(prmd_files)} .prmd files to fix")

    for prmd_file in prmd_files:
        print(f"  Fixing: {prmd_file.relative_to(new_dir)}")
        with open(prmd_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix template syntax
        content = fix_template_syntax(content)

        # Bump version
        content = bump_version_in_content(content, old_version, new_version)

        with open(prmd_file, 'w', encoding='utf-8') as f:
            f.write(content)

    # Update manifest.json if it exists
    manifest_path = new_dir / "manifest.json"
    if manifest_path.exists():
        print(f"  Updating manifest.json")
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = json.load(f)
        manifest['version'] = new_version
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2)

    # Build the package
    package_filename = f"{package_name.replace('@prompd.io/', '').replace('/', '-')}-{new_version}.pdpkg"
    output_path = OUTPUT_DIR / package_filename

    print(f"\nBuilding package: {package_filename}")

    # Use prompd CLI to create package
    cmd = [
        "python", "-m", "prompd", "package", "create",
        str(new_dir),
        str(output_path)
    ]

    result = subprocess.run(
        cmd,
        cwd=str(PROMPD_CLI),
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"SUCCESS: Package created at {output_path}")

        # Validate the new package
        validate_cmd = [
            "python", "-m", "prompd", "package", "validate",
            str(output_path)
        ]

        validate_result = subprocess.run(
            validate_cmd,
            cwd=str(PROMPD_CLI),
            capture_output=True,
            text=True
        )

        if validate_result.returncode == 0:
            print(f"VALIDATED: Package validation passed")
        else:
            print(f"VALIDATION ERROR: {validate_result.stderr}")

        return True
    else:
        print(f"BUILD ERROR: {result.stderr}")
        return False

def process_special_packages():
    """Process the special packages (public/examples and test packages)."""
    print("\n" + "="*60)
    print("Processing special packages")
    print("="*60)

    # Process public/examples
    public_dir = PRODUCTION_DIR / "public/examples"
    if public_dir.exists():
        print("\nProcessing public/examples")

        # Fix .prmd files
        for prmd_file in public_dir.glob("*.prmd"):
            print(f"  Fixing: {prmd_file.name}")
            with open(prmd_file, 'r', encoding='utf-8') as f:
                content = f.read()

            content = fix_template_syntax(content)
            # Bump version from 1.0.0 to 1.0.1
            content = bump_version_in_content(content, "1.0.0", "1.0.1")

            with open(prmd_file, 'w', encoding='utf-8') as f:
                f.write(content)

        # Update manifest if exists
        manifest_path = public_dir / "manifest.json"
        if manifest_path.exists():
            with open(manifest_path, 'r', encoding='utf-8') as f:
                manifest = json.load(f)
            manifest['version'] = "1.0.1"
            with open(manifest_path, 'w', encoding='utf-8') as f:
                json.dump(manifest, f, indent=2)

        # Build package
        output_path = OUTPUT_DIR / "public-examples-1.0.1.pdpkg"
        cmd = [
            "python", "-m", "prompd", "package", "create",
            str(public_dir),
            str(output_path)
        ]

        result = subprocess.run(cmd, cwd=str(PROMPD_CLI), capture_output=True, text=True)
        if result.returncode == 0:
            print(f"SUCCESS: Created {output_path}")
        else:
            print(f"ERROR: {result.stderr}")

    # Process test-simple-code-gen (copy from simple-code-gen)
    test_source = PRODUCTION_DIR / "@prompd.io/simple-code-gen@1.0.1"
    test_dest = PRODUCTION_DIR / "@prompd.io/test-simple-code-gen@1.0.1"

    if test_source.exists():
        print("\nProcessing test-simple-code-gen")

        if test_dest.exists():
            shutil.rmtree(test_dest)

        shutil.copytree(test_source, test_dest)

        # Update manifest to change name
        manifest_path = test_dest / "manifest.json"
        if manifest_path.exists():
            with open(manifest_path, 'r', encoding='utf-8') as f:
                manifest = json.load(f)
            manifest['name'] = "@prompd.io/test-simple-code-gen"
            manifest['description'] = "Test package for simple code generation"
            with open(manifest_path, 'w', encoding='utf-8') as f:
                json.dump(manifest, f, indent=2)

        # Build package
        output_path = OUTPUT_DIR / "test-simple-code-gen-1.0.1.pdpkg"
        cmd = [
            "python", "-m", "prompd", "package", "create",
            str(test_dest),
            str(output_path)
        ]

        result = subprocess.run(cmd, cwd=str(PROMPD_CLI), capture_output=True, text=True)
        if result.returncode == 0:
            print(f"SUCCESS: Created {output_path}")
        else:
            print(f"ERROR: {result.stderr}")

def main():
    """Main function to process all packages."""
    print("Starting package fixing and rebuilding process...")

    success_count = 0

    # Process main packages
    for package_name, old_version, new_version in PACKAGES:
        if process_package(package_name, old_version, new_version):
            success_count += 1

    # Process special packages
    process_special_packages()

    print("\n" + "="*60)
    print(f"SUMMARY: Processed {success_count}/{len(PACKAGES)} main packages successfully")
    print("="*60)

    # List all new packages
    print("\nNew packages in examples directory:")
    for pdpkg in sorted(OUTPUT_DIR.glob("*-1.0.1.pdpkg")):
        print(f"  - {pdpkg.name}")

if __name__ == "__main__":
    main()