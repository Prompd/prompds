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