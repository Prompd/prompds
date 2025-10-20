#!/usr/bin/env python
"""Reset all packages to version 1.0.0 and rebuild them"""

import os
import json
import shutil
import subprocess
from pathlib import Path

# Define packages to reset and rebuild
PACKAGES = [
    ("@prompd.io/api-development", "1.0.1", "1.0.0"),
    ("@prompd.io/code-review", "1.0.1", "1.0.0"),
    ("@prompd.io/core-patterns", "2.0.1", "1.0.0"),  # Reset to 1.0.0
    ("@prompd.io/core-patterns", "2.1.0", "1.0.0"),  # Reset to 1.0.0
    ("@prompd.io/data-science-toolkit", "1.0.0-fixed", "1.0.0"),  # Use fixed version
    ("@prompd.io/meeting-minutes", "1.0.1", "1.0.0"),
]

PRODUCTION_DIR = Path("production")

def update_package_version(package_dir, old_version, new_version):
    """Update version in all .prmd files and manifest.json"""

    # Update .prmd files
    for prmd_file in package_dir.rglob("*.prmd"):
        with open(prmd_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update version in YAML frontmatter
        content = content.replace(f"version: {old_version}", f"version: {new_version}")

        with open(prmd_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  Updated version in {prmd_file.relative_to(package_dir)}")

    # Update manifest.json if it exists
    manifest_path = package_dir / "manifest.json"
    if manifest_path.exists():
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = json.load(f)
        manifest['version'] = new_version
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2)
        print(f"  Updated manifest.json")
    else:
        print(f"  No manifest.json found")

def create_manifest_if_missing(package_dir, package_name, version, description):
    """Create manifest.json if it doesn't exist"""
    manifest_path = package_dir / "manifest.json"
    if not manifest_path.exists():
        manifest = {
            "name": package_name,
            "version": version,
            "description": description,
            "license": "MIT",
            "tags": [],
            "dependencies": {},
            "keywords": []
        }

        # Find main .prmd file
        prmd_files = list(package_dir.rglob("*.prmd"))
        if prmd_files:
            main_file = prmd_files[0]
            manifest["main"] = str(main_file.relative_to(package_dir))

            # Add other files
            if len(prmd_files) > 1:
                manifest["files"] = [str(f.relative_to(package_dir)) for f in prmd_files[1:]]

        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2)
        print(f"  Created manifest.json")

def rebuild_package(package_name, source_dir, output_name, description):
    """Rebuild package using prompd CLI"""
    output_path = PRODUCTION_DIR / f"{output_name}-1.0.0.pdpkg"

    # Remove old package if exists
    if output_path.exists():
        output_path.unlink()
        print(f"  Removed old package: {output_path}")

    cmd = [
        "python", "-m", "prompd", "package", "create",
        str(source_dir),
        str(output_path),
        "--name", package_name,
        "--version", "1.0.0",
        "--description", description
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"  SUCCESS: Created {output_path}")
        return True
    else:
        print(f"  ERROR: {result.stderr}")
        return False

def main():
    """Main function"""
    print("Resetting package versions to 1.0.0 and rebuilding...")

    # Package descriptions
    descriptions = {
        "@prompd.io/api-development": "Complete API development toolkit with endpoint generators",
        "@prompd.io/code-review": "Comprehensive code review system covering security and best practices",
        "@prompd.io/core-patterns": "Base framework for structured analysis tasks",
        "@prompd.io/data-science-toolkit": "Complete data science toolkit with ML pipeline builders",
        "@prompd.io/meeting-minutes": "AI-powered meeting transcription and minutes generation"
    }

    success_count = 0

    for package_name, old_version_dir, new_version in PACKAGES:
        print(f"\n{'='*60}")
        print(f"Processing {package_name}")
        print('='*60)

        # Special handling for core-patterns (skip 2.1.0, use 2.0.1)
        if package_name == "@prompd.io/core-patterns" and old_version_dir == "2.1.0":
            print("  Skipping core-patterns@2.1.0 (will use 2.0.1 source)")
            continue

        source_dir = PRODUCTION_DIR / f"{package_name}@{old_version_dir}"

        if not source_dir.exists():
            print(f"  ERROR: Source directory not found: {source_dir}")
            continue

        # Update versions in source files
        print(f"  Updating versions from {old_version_dir} to {new_version}")
        update_package_version(source_dir, old_version_dir, new_version)

        # Create manifest if missing
        description = descriptions.get(package_name, f"Package {package_name}")
        create_manifest_if_missing(source_dir, package_name, new_version, description)

        # Rebuild package
        output_name = package_name.replace("@prompd.io/", "").replace("/", "-")
        if rebuild_package(package_name, source_dir, output_name, description):
            success_count += 1

    print(f"\n{'='*60}")
    print(f"SUMMARY: Successfully rebuilt {success_count}/{len(PACKAGES)-1} packages")  # -1 for skipped core-patterns
    print('='*60)

    # List all 1.0.0 packages
    print("\nRebuilt packages:")
    for pdpkg in sorted(PRODUCTION_DIR.glob("*-1.0.0.pdpkg")):
        print(f"  - {pdpkg.name}")

if __name__ == "__main__":
    main()