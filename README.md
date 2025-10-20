# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is `@prompd/public-examples`, a reference implementation package demonstrating the core features of the Prompd prompt composition system. It showcases inheritance patterns, template composition, parameter handling, and package-based references.

**Purpose:** Educational example package demonstrating best practices for building reusable, composable AI prompts using the Prompd format (.prmd files).

## Common Commands

### Package Management
```bash
# Create a new package bundle from src/
prompd package create

# Validate package structure and manifest
prompd package validate dist/public-examples-{version}.pdpkg

# Install the package locally for testing
prompd install @prompd/public-examples@latest

# Publish to registry (requires authentication)
prompd registry publish dist/public-examples-{version}.pdpkg
```

### Running Prompts
```bash
# Run the main prompt (api-development.prmd)
prompd run "@prompd/public-examples@latest" --provider openai -p endpoint_name="user authentication"

# Run specific prompt file
prompd run "@prompd/public-examples@latest/prompts/basic-inheritance.prmd" --provider anthropic -p topic="blockchain"

# Run with parameter file
prompd run "@prompd/public-examples@latest/prompts/package-inheritance.prmd" -f params.json
```

### Compilation
```bash
# Compile to markdown
prompd compile "src/prompts/api-development.prmd" --to-markdown -p endpoint_name="login" -o output.md

# Compile to provider JSON (OpenAI format)
prompd compile "src/prompts/basic-inheritance.prmd" --to-provider-json openai -p topic="AI systems"

# Compile to provider JSON (Anthropic format)
prompd compile "src/prompts/package-inheritance.prmd" --to-provider-json anthropic -p domain="healthcare"
```

### Validation
```bash
# Validate individual prompt file
prompd validate src/prompts/api-development.prmd

# Validate with verbose output
prompd validate src/prompts/package-inheritance.prmd -v

# Validate entire package
prompd package validate dist/public-examples-{version}.pdpkg
```

## Architecture

### File Structure
```
public-examples/
├── .prompd/                    # Prompd workspace configuration
│   ├── config.yaml            # Local configuration
│   ├── lock.json              # Dependency lock file
│   └── cache/                 # Downloaded package cache
├── src/                        # Package source files
│   ├── manifest.json          # Package metadata (name, version, dependencies)
│   ├── README.md              # Package documentation
│   ├── prompts/               # Prompt files (.prmd)
│   │   ├── api-development.prmd       # Main entry point (complex templating)
│   │   ├── base-prompt.prmd           # Base template for inheritance
│   │   ├── basic-inheritance.prmd     # Local file inheritance example
│   │   ├── package-inheritance.prmd   # Cross-package inheritance example
│   │   └── team-project-planner.prmd  # Multi-role project planning
│   ├── assistants/            # Assistant role prompts
│   │   └── code-assistant.prmd        # General-purpose coding assistant
│   ├── systems/               # System persona files (.md)
│   │   └── system-admin.md            # System administrator persona/guidelines
│   ├── users/                 # User persona files (.md)
│   │   └── user-lead-engineer.md      # Lead engineer persona/guidelines
│   └── contexts/              # Context files (TypeScript, JSON, YAML, Markdown)
│       ├── typescript-examples.ts     # Sample TypeScript class structures
│       ├── code-review-checklist.md   # Comprehensive review checklist
│       ├── deployment-config.yaml     # Deployment and monitoring configs
│       └── architecture-patterns.json # Architecture patterns with tradeoffs
└── dist/                       # Built package bundles (.pdpkg)
    └── public-examples-{version}.pdpkg
```

### Prompt File Format (.prmd)

Prompd files use YAML frontmatter + Markdown body with Jinja2 templating:

```yaml
---
id: unique-prompt-id
name: "Human Readable Name"
description: "What this prompt does"
version: 1.0.0
inherits: "./base-prompt.prmd"  # or "@package@version/path.prmd"
parameters:
  - name: param_name
    type: string|boolean|array|object
    required: true|false
    default: "value"
    description: "Parameter description"
---
# Markdown content with {parameter} substitution and {% jinja2 %} logic
```

### Key Prompts

The package includes several demonstration prompts, each showcasing different capabilities:

**Prompts Directory (`prompts/`)**
- `api-development.prmd` - Main entry point; complex conditional logic for API development
- `base-prompt.prmd` - Foundation template demonstrating clean prompt structure
- `basic-inheritance.prmd` - Local file inheritance with Jinja2 conditionals
- `package-inheritance.prmd` - Cross-package, versioned inheritance example
- `team-project-planner.prmd` - Multi-role project planning with object/array parameters

**Assistants Directory (`assistants/`)**
- `code-assistant.prmd` - General-purpose coding assistant supporting 6 languages and 5 task modes

**Systems/Users Directories**
- `systems/system-admin.md` - DevOps/infrastructure persona definition
- `users/user-lead-engineer.md` - Technical leadership persona definition

**Contexts Directory (`contexts/`)**
- `typescript-examples.ts` - Sample TypeScript class structures
- `architecture-patterns.json` - Architecture patterns with pros/cons/tradeoffs
- `deployment-config.yaml` - Deployment strategies, monitoring, backup policies
- `code-review-checklist.md` - Comprehensive code review checklist

### Key Concepts

**1. Inheritance Chain**
- `base-prompt.prmd` → Foundation template
- `basic-inheritance.prmd` → Inherits from local `./base-prompt.prmd`
- `package-inheritance.prmd` → Inherits from `@prompd/public-examples@1.0.5/prompts/base-prompt.prmd` (cross-version)

**2. Self-Referential Dependencies**
The package demonstrates version migration by depending on an earlier version of itself (`1.0.5` depends on `1.0.4`). This shows how prompts can evolve while maintaining backward compatibility.

**3. Parameter Types**
- **string**: `{endpoint_name}`, `{topic}`
- **boolean**: `{auth_required}` → `{% if auth_required %}`
- **array**: `{stakeholders}` → `{% for stakeholder in stakeholders %}`
- **object**: `{config.field}` → nested access
- **enum**: Restricts values to predefined list

**4. Template Engine (Jinja2)**
- Conditionals: `{% if %}`, `{% elif %}`, `{% else %}`, `{% endif %}`
- Loops: `{% for item in items %}...{% endfor %}`
- Variables: `{variable_name}`
- Filters: `{variable|filter}`
- Comments: `{# comment #}`

**5. Package Bundle (.pdpkg)**
- ZIP archive containing all package files
- Excludes `.pdproj` files (like NuGet excludes `.csproj`)
- Includes `manifest.json`, prompts, contexts, README

**6. Persona Files (.md)**
The `systems/` and `users/` directories contain markdown persona files (not .prmd):
- Define role-specific competencies, responsibilities, and best practices
- Used as context/reference for role-based prompts
- Can be imported into .prmd files via `contexts:` field
- Examples: system-admin.md, user-lead-engineer.md

## Development Workflow

### Updating Prompts
1. Edit files in `src/prompts/`
2. Update version in `src/manifest.json`
3. Test locally: `prompd run "src/prompts/{file}.prmd" -p param=value`
4. Validate: `prompd validate src/prompts/{file}.prmd -v`
5. Create package: `prompd package create`
6. Publish: `prompd registry publish dist/public-examples-{version}.pdpkg`

### Testing Inheritance
When modifying inherited prompts, test the inheritance chain:
```bash
# Test base template
prompd run "src/prompts/base-prompt.prmd" -p topic="test"

# Test local inheritance
prompd run "src/prompts/basic-inheritance.prmd" -p topic="test" -p analysis_depth="comprehensive"

# Test package inheritance (requires published version)
prompd install @prompd/public-examples@1.0.5
prompd run "src/prompts/package-inheritance.prmd" -p domain="technology"
```

### Version Management
- Follow semantic versioning (MAJOR.MINOR.PATCH)
- Update `manifest.json` version before creating package
- Test cross-version compatibility when using `inherits` with versioned packages
- Self-referential dependency requires previous version to be published

## Integration Points

### Context Files
The `contexts/` directory contains files that can be referenced in prompts for additional context:
- **Code files** (TypeScript, Python, Go, etc.) - Sample implementations and type definitions
- **JSON data** - Structured information like architecture patterns with tradeoffs
- **YAML configs** - Deployment configurations, monitoring alerts, backup policies
- **Markdown docs** - Checklists, guidelines, documentation (e.g., code review checklists)

Context files are declared in the .prmd frontmatter:
```yaml
contexts:
  - "contexts/typescript-examples.ts"
  - "contexts/architecture-patterns.json"
  - "contexts/deployment-config.yaml"
  - "contexts/code-review-checklist.md"
```

These are extracted during compilation and injected into the prompt context.

### Package Dependencies
Defined in `manifest.json` under `dependencies`:
```json
{
  "dependencies": {
    "@prompd/public-examples": "1.0.5"
  }
}
```

Dependencies are resolved from:
1. Local cache (`.prompd/cache/`)
2. Registry download (https://registry.prompdhub.ai)

### Main Entry Point
The `main` field in `manifest.json` specifies the default prompt:
```json
{
  "main": "prompts/api-development.prmd"
}
```

This allows running without specifying a path:
```bash
prompd run "@prompd/public-examples@latest"
```

## Important Notes

- **DO NOT modify** files in `.prompd/cache/` - these are managed by the Prompd CLI
- **Version consistency**: When updating package version, ensure `inherits` references are correct
- **Parameter validation**: Required parameters must be provided or have defaults
- **Jinja2 syntax**: Use `{%- ... %}` to suppress whitespace, `{% ... %}` to preserve it
- **Enum validation**: Parameter values are validated against enum constraints
- **File extensions**:
  - `.prmd` for executable prompts
  - `.md` for persona/documentation files (in systems/, users/ directories)
  - `.pdpkg` for package bundles
  - `.pdproj` for project files (excluded from packages)
- **Distribution files**: Only `.pdpkg` files should be published to registry
- **Context injection**: Files in `contexts/` are automatically processed during compilation
- **Persona vs Prompt files**: .md persona files define roles/guidelines; .prmd files are executable templates

## Example Use Cases

### API Development (Main Entry Point)
```bash
prompd run "@prompd/public-examples@latest" \
  --provider openai \
  -p endpoint_name="payment processing" \
  -p http_method="POST" \
  -p framework="fastify" \
  -p auth_required=true \
  -p validation_level="enterprise"
```

### Team Project Planning
```bash
# Comprehensive project plan with all roles
prompd run "@prompd/public-examples@latest/prompts/team-project-planner.prmd" \
  --provider anthropic \
  -p project_name="E-commerce Platform" \
  -p project_phase="development" \
  -p tech_stack='{"language":"typescript","framework":"fastify","architecture":"microservices"}' \
  -p team_roles='["developer","lead_engineer","system_admin","qa"]'

# Planning phase for new project
prompd run "@prompd/public-examples@latest/prompts/team-project-planner.prmd" \
  --provider openai \
  -p project_name="Mobile App Backend" \
  -p project_phase="planning"
```

### Code Assistant
```bash
# TypeScript implementation with tests
prompd run "@prompd/public-examples@latest/assistants/code-assistant.prmd" \
  --provider anthropic \
  -p language="typescript" \
  -p task_mode="implement" \
  -p include_tests=true

# Debug Python code
prompd run "@prompd/public-examples@latest/assistants/code-assistant.prmd" \
  --provider openai \
  -p language="python" \
  -p task_mode="debug" \
  -p include_tests=false
```

### Analysis with Inheritance
```bash
prompd run "@prompd/public-examples@latest/prompts/basic-inheritance.prmd" \
  --provider anthropic \
  -p topic="distributed systems" \
  -p analysis_depth="comprehensive"
```

### Multi-Stakeholder Analysis (Package Inheritance)
```bash
prompd run "@prompd/public-examples@latest/prompts/package-inheritance.prmd" \
  -f params.json \
  --provider openai
```

Where `params.json`:
```json
{
  "domain": "healthcare technology",
  "stakeholders": ["developers", "executives", "regulators"]
}
```


# Prompd Engineering Prompts

## 🎯 Purpose
This is a meta-Prompd project that produces high-quality prompts for our engineering team. By using Prompd to compile prompts for Prompd development, we're dogfooding our own platform while ensuring consistency and quality across all development tasks.

## 🚀 Quick Start

```bash
# Navigate to the project
cd C:\git\github\Logikbug\prompd-engineering-prompts

# Compile a prompt for implementing a new feature
prompd compile code-implementation.prompd \
  --params component_name="Registry Auth Middleware" \
  language="nodejs" \
  security_level="critical"

# Compile a bug fix prompt
prompd compile bug-fix.prompd \
  --params bug_description="Token validation fails intermittently" \
  affected_component="Auth System" \
  severity="high"
```

## 📁 Available Prompts

### 1. Code Implementation (`code-implementation.prompd`)
**Purpose:** Compile precise implementation prompts with security and best practices built-in

**Use Cases:**
- Building new features
- Implementing components
- Creating APIs
- Writing utilities

**Key Features:**
- Language-specific best practices
- Security level configuration (standard/high/critical)
- Testing requirements
- Anti-pattern prevention

### 2. Architecture Review (`architecture-review.prompd`)
**Purpose:** Compile prompts for system design and architecture analysis

**Use Cases:**
- New system design
- Architecture refactoring
- Security reviews
- Performance optimization
- Integration planning

**Key Features:**
- Scale-aware (prototype/production/enterprise)
- Review type selection
- Comprehensive checklists
- Deliverable specifications

### 3. Bug Fix (`bug-fix.prompd`)
**Purpose:** Compile focused debugging and fix prompts

**Use Cases:**
- Critical production issues
- Bug resolution
- Performance problems
- Security vulnerabilities

**Key Features:**
- Severity-based approach
- Root cause analysis focus
- Regression prevention
- Critical issue protocol

### 4. Integration Testing (`integration-testing.prompd`)
**Purpose:** Compile comprehensive testing strategy prompts

**Use Cases:**
- Unit test creation
- Integration testing
- E2E test design
- Performance testing
- Security testing

**Key Features:**
- Coverage targets
- Test scope selection
- CI/CD integration
- Best practices enforcement

### 5. Master Prompt (`master-prompt.prompd`)
**Purpose:** Meta-prompt to help select the right prompt for any task

**Use Cases:**
- Task analysis
- Prompt selection
- Workflow coordination
- Team assignment

## 🔧 Integration with Development Workflow

### For Individual Developers:
1. Identify your task type
2. Select appropriate prompt template
3. Compile prompt with specific parameters
4. Use compiled prompt with Claude instance
5. Implement solution following prompt guidelines

### For Team Coordination:
1. Lead Coordinator identifies tasks from sprint
2. Compile appropriate prompts for each task
3. Assign prompts to team instances
4. Track implementation progress
5. Validate against prompt requirements

## 💡 Best Practices

### DO:
- ✅ Use specific, detailed parameters
- ✅ Chain prompts for complex tasks
- ✅ Include security_level for any user-facing code
- ✅ Set testing_required=true for production code
- ✅ Reference existing code patterns via context_files

### DON'T:
- ❌ Skip security considerations
- ❌ Ignore testing requirements
- ❌ Use generic descriptions
- ❌ Forget to specify language/platform
- ❌ Bypass the architecture review for major changes

## 🔄 Workflow Examples

### Example 1: Implementing a New Registry Endpoint

```bash
# Step 1: Architecture Review
prompd compile architecture-review.prompd \
  --params system_component="Package Versioning API" \
  review_type="new_design" \
  scale_requirements="production"

# Step 2: Implementation
prompd compile code-implementation.prompd \
  --params component_name="Package Versioning API" \
  language="nodejs" \
  security_level="high" \
  context_files='["registry/routes/packages.js", "registry/models/package.js"]'

# Step 3: Testing
prompd compile integration-testing.prompd \
  --params test_scope="integration" \
  component="Package Versioning API" \
  coverage_target=85
```

### Example 2: Critical Bug Fix

```bash
# Compile comprehensive bug fix prompt
prompd compile bug-fix.prompd \
  --params bug_description="Memory leak in package validation causing server crashes" \
  affected_component="Package Validator" \
  severity="critical" \
  error_message="FATAL ERROR: Reached heap limit Allocation failed"
```

## 📊 Prompt Parameter Reference

### Common Parameters Across All Prompts:
- `component_name` / `system_component` / `affected_component`: The specific part being worked on
- `severity` / `security_level`: Importance and security requirements
- `test_scope` / `testing_required`: Testing expectations

### Security Levels:
- `standard`: Basic security practices
- `high`: Enhanced security with validation
- `critical`: Maximum security, includes audit logging, rate limiting

### Scale Requirements:
- `prototype`: Proof of concept, local development
- `production`: 1000+ users, high availability
- `enterprise`: 10,000+ users, multi-region, 99.9% SLA

## 🚀 Advanced Usage

### Parameterized Bulk Compilation
Create a params file for repeated use:

```json
// registry-params.json
{
  "language": "nodejs",
  "security_level": "high",
  "testing_required": true,
  "context_files": ["registry/server.js", "registry/auth.js"]
}
```

```bash
prompd compile code-implementation.prompd --params-file registry-params.json \
  --params component_name="Rate Limiter Middleware"
```

### Custom Templates
Extend existing prompts for specific needs:

```yaml
---
extends: code-implementation
id: cli-command-implementation
name: CLI Command Implementation
parameters:
  - name: command_name
    type: string
    required: true
  - name: cli_platform
    type: string
    enum: [python, go, nodejs]
    required: true
---

# Additional CLI-specific requirements...
```

## 🎯 Success Metrics

Track the effectiveness of prompts by measuring:
- Implementation speed
- Bug density
- Security issue frequency
- Test coverage achieved
- Code review iterations needed

## 🔮 Future Enhancements

- [ ] AI-powered prompt parameter suggestion
- [ ] Historical prompt effectiveness tracking
- [ ] Team-specific prompt customization
- [ ] Automated prompt chaining for workflows
- [ ] Integration with CI/CD for automated prompt generation

## 📚 Related Documentation

- [Prompd CLI Documentation](../prompd-cli/docs/CLI.md)
- [Format Specification](../prompd-cli/docs/FORMAT.md)
- [Team Coordination Guide](../CLAUDE.md)
- [Architecture Vision](../PROMPD-VISION.md)

---

*Remember: We're building the operating system for the AI internet. Every prompt, every line of code, every decision matters. Use these prompts to maintain the highest standards.*
