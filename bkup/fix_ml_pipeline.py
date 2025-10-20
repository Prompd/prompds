#!/usr/bin/env python
"""Fix template syntax in ml-pipeline-builder.prmd"""

import re

def fix_template_syntax(content):
    """Fix template syntax from {{var}} to {var} and remove complex switch statements"""

    # First, replace simple double braces {{var}} with {var}
    content = re.sub(r'\{\{(\w+)\}\}', r'{\1}', content)

    # Remove complex switch/case blocks that aren't supported in Jinja2
    # Replace with simpler if/else statements

    # Remove switch statements
    content = re.sub(r'\{\{#switch [^}]+\}\}', '', content)
    content = re.sub(r'\{\{/switch\}\}', '', content)
    content = re.sub(r'\{\{#case "[^"]+"\}\}', '', content)
    content = re.sub(r'\{\{/case\}\}', '', content)

    # Fix conditional statements to use proper Jinja2 syntax
    content = re.sub(r'\{\{#if (\w+)\}\}', r'{%- if \1 %}', content)
    content = re.sub(r'\{\{/if\}\}', r'{%- endif %}', content)

    # Fix version back to 1.0.0
    content = re.sub(r'version: 1\.0\.1', 'version: 1.0.0', content)

    return content

# Read the problematic file
file_path = "production/@prompd.io/data-science-toolkit@1.0.0-fixed/prompts/ml-pipeline-builder.prmd"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the syntax
fixed_content = fix_template_syntax(content)

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(fixed_content)

print("Fixed template syntax in ml-pipeline-builder.prmd")
print("- Converted {{var}} to {var}")
print("- Removed unsupported switch/case statements")
print("- Reset version to 1.0.0")