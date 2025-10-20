# CLAUDE.md

Note: For a consolidated, up-to-date overview of repo guidelines and current status, see `prompd.md` at the repository root. This file focuses on Claude/agent usage with canonical verbs (compile/run/validate).

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a meta-Prompd project containing engineering prompt templates used across the Prompd development ecosystem. The prompts compile high-quality, consistent prompts for development tasks by dogfooding Prompd's own platform.

**Key Innovation:** This project implements an advanced composable AI prompt ecosystem - building toward the "npm for AI prompts" - enabling package-based distribution, inheritance patterns, and universal compilation to any AI provider.

## Core Commands

### Run Engineering Prompts
```bash
# Compile implementation prompt with parameters
prompd compile prompds/code-implementation.prompd \
  --params component_name="Registry Auth Middleware" \
  language="nodejs" \
  security_level="critical"

# Compile bug fix prompt
prompd compile prompds/bug-fix.prompd \
  --params bug_description="Token validation fails intermittently" \
  affected_component="Auth System" \
  severity="high"

# Compile architecture review prompt
prompd compile prompds/architecture-review.prompd \
  --params system_component="Package Versioning API" \
  review_type="new_design" \
  scale_requirements="production"

# Compile testing strategy prompt
prompd compile prompds/integration-testing.prompd \
  --params test_scope="integration" \
  component="Package Versioning API" \
  coverage_target=85
```

### Real-World Domain Prompts
```bash
# API development
prompd compile real-world-prompts/api-integration/rest-endpoint-builder.prompd \
  --params-file real-world-prompts/api-integration/params/saas-api.json

# Security audit
prompd compile real-world-prompts/security/owasp-security-audit.prompd \
  --params application_type="web-app" \
  technology_stack="React + Node.js + PostgreSQL"

# Database migration
prompd compile real-world-prompts/database/schema-migration-builder.prompd \
  --params migration_name="Add user preferences table" \
  database_type="postgresql"

# Machine learning pipeline
prompd compile real-world-prompts/data-science/ml-pipeline-builder.prompd \
  --params-file real-world-prompts/data-science/params/customer-churn-ml.json
```

### Run Workflows
```bash
# Run complete engineering workflow
prompd compile pdflows/engineering-workflow.pdflow \
  --params feature_name="User Authentication System" \
  language="nodejs" \
  security_level="critical"
```

### Use Master Coordinator
```bash
# Get prompt selection guidance
prompd compile prompds/master-prompt.prompd \
  --params task_type="implement user authentication" \
  urgency="today"
```

### Enhanced Interactive Shell
```bash
# Start enhanced shell with conversational AI
prompd shell

# Available shell features:
# - Rich CLI experience with syntax highlighting
# - Natural language processing for commands
# - Chat mode for AI assistance
# - Context-aware suggestions and command completion
# - Seamless switching between command mode and chat mode

# Example shell interactions:
# prompd> compile my security audit for Node.js app
# prompd> show me what's in that API prompt
# prompd> chat
# chat> help me create a prompt for database migrations
# chat> exit
# prompd> list all packages
```

## Composable Architecture

This project implements the composable prompt architecture documented in `COMPOSABLE-ARCHITECTURE.md`:

### Package-Based Development
```bash
# Install composable packages
prompd install @prompd.io/security-toolkit@1.0.0
prompd install @prompd.io/api-toolkit@1.0.0

# Use inheritance and composition
prompd compile composable-packages/@prompd.io--security-toolkit@1.0.0/prompts/security-audit.prompd \
  --params target="Node.js application"

# Multi-format compilation
prompd compile security-audit.prompd --to provider-json:anthropic --output claude.json
prompd compile security-audit.prompd --to provider-json:openai --output gpt4.json
```

### Context Composition
```bash
# Pass context files for analysis
prompd run security-audit.prompd \
  --meta:context ./src/auth.js \
  --meta:context ./config/database.yml \
  --meta:context ./package.json
```

## Development Workflow

### Project Structure
- **`prompds/`** - Core engineering prompt templates (5 templates)
- **`real-world-prompts/`** - Domain-specific prompts organized by industry/function
- **`composable-packages/`** - Package-based prompt components with inheritance
- **`pdflows/`** - Multi-step workflow definitions
- **`engineering-prompts.pdproj`** - Project metadata and configuration

### Core Prompt Templates
1. **`code-implementation.prompd`** - Feature/component implementation with security built-in
2. **`architecture-review.prompd`** - System design and architecture analysis  
3. **`bug-fix.prompd`** - Focused debugging and problem resolution
4. **`integration-testing.prompd`** - Comprehensive testing strategies
5. **`master-prompt.prompd`** - Meta-prompt for selecting appropriate templates

### Validation and Quality Assurance
```bash
# Validate prompt syntax and structure
prompd validate prompds/code-implementation.prompd

# Validate with verbose output
prompd validate prompds/architecture-review.prompd -v

# Validate entire project
find . -name "*.prompd" -exec prompd validate {} \;
```

### Testing Prompts
```bash
# Test prompt compilation
prompd compile prompds/code-implementation.prompd \
  --params component_name="Test Component" \
  language="python" \
  --output test-output.md
```

## Parameter System

### Security Levels
- **`standard`** - Basic security practices
- **`high`** - Enhanced security with validation  
- **`critical`** - Maximum security, includes audit logging, rate limiting

### Languages Supported
- **`python`** - Python with type hints and PEP 8 compliance
- **`go`** - Go with zero dependencies and proper error handling
- **`nodejs`** - Node.js with TypeScript and async/await patterns
- **`typescript`** - Strict TypeScript with proper typing

### Scale Requirements
- **`prototype`** - Proof of concept, local development
- **`production`** - 1000+ users, high availability
- **`enterprise`** - 10,000+ users, multi-region, 99.9% SLA

## Integration Context

This prompt library integrates with the broader Prompd ecosystem:

### Core Engine Team Integration
- Compiles consistent implementation prompts for Python, Go, and Node.js CLI development
- Enforces security standards across all compiled code
- Provides architecture review templates for major system changes

### Registry Team Integration  
- API development prompts for registry backend endpoints
- Database migration prompts for schema changes
- Security audit prompts for production deployments

### IDE Team Integration
- Workflow prompts for VS Code extension development
- Integration testing prompts for IDE features

## Best Practices

### Prompt Chaining
Chain prompts for comprehensive coverage:
```bash
# Architecture → Implementation → Security → Testing
prompd compile prompds/architecture-review.prompd --params-file params.json
prompd compile prompds/code-implementation.prompd --params-file params.json  
prompd compile real-world-prompts/security/owasp-security-audit.prompd --params-file params.json
prompd compile prompds/integration-testing.prompd --params-file params.json
```

### Parameter Management
- Use descriptive parameter file names (`saas-api.json`, `startup-dcf.json`)
- Group related parameters together
- Version parameter files for different environments

### Context Files
Use context files for analysis of existing code:
```bash
# Pass existing code for analysis
prompd compile real-world-prompts/security/owasp-security-audit.prompd \
  --params-file security-params.json \
  --meta:context ./src/auth.js \
  --meta:context ./config/database.yml
```

## Package Management

### Registry Operations
```bash
# Search for packages
prompd search security

# Install specific versions
prompd install @prompd.io/security-toolkit@1.0.0

# Publish new packages
prompd publish security-toolkit.pdpkg

# List installed packages
prompd list
```

### Cache Management
```bash
# Clear package cache
prompd cache clear

# Show cache information
prompd cache info
```

## Revolutionary Architecture Features

### Universal Compilation
This project demonstrates an advanced universal AI prompt compiler with unique capabilities:
- **Multi-Provider Support**: Compiles to OpenAI, Anthropic, Google formats
- **Package Inheritance**: Full npm-like dependency system for prompts
- **Context Composition**: Binary file extraction (Excel, Word, PDF, images)
- **Format Extensibility**: Plugin architecture for new output formats

### Language Server Integration
The composable architecture supports full IDE integration:
- Real-time syntax highlighting for YAML + Handlebars + Markdown
- IntelliSense for package imports and parameter completion
- Live compilation preview
- Dependency graph visualization

This represents an advancement beyond existing prompt management tools, offering a comprehensive development ecosystem that combines package-based inheritance, universal compilation, and complete toolchain integration for AI workflows.
