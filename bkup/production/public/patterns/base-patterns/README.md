# @prompd.io/base-patterns

Universal foundation patterns for Prompd development with common parameter structures, validation patterns, and response formats.

## Features

- **Universal Parameters**: Standard parameter structure used across all Prompd packages
- **Validation Framework**: Multi-level validation system (minimal, standard, strict, comprehensive)
- **Response Formatting**: Consistent output formats (structured, JSON, markdown, CSV)
- **Inheritance Foundation**: Base pattern for all other Prompd packages to inherit from
- **Context Management**: Flexible context scoping for different use cases

## Usage

### Direct Usage
```bash
prompd run base-patterns.prmd \
  --output_format "json" \
  --validation_level "comprehensive" \
  --context_scope "focused"
```

### Inheritance Usage
```yaml
---
name: "@yournamespace/your-package"
version: "1.0.0"
inherits: "@prompd.io/base-patterns@2.1.0"
parameters:
  - name: "domain_specific_param"
    type: "string"
    required: true
---
```

## Standard Parameters

- `output_format`: structured, json, markdown, csv, detailed
- `validation_level`: minimal, standard, strict, comprehensive  
- `context_scope`: minimal, focused, comprehensive, exhaustive
- `priority_level`: low, normal, high, critical
- `custom_instructions`: Optional additional instructions

## Response Structure

All packages inheriting from base-patterns will provide consistent response formats with summary, key findings, details, validation results, and metadata sections.

## Inheritance Guidelines

1. Always preserve core parameter structure
2. Extend with domain-specific parameters
3. Maintain standard response format
4. Include reference to base pattern
5. Follow validation standards

This is the foundational package that all other @prompd.io packages inherit from.