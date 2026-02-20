# Prompd Community Prompts

A collection of open-source prompt packages and templates for the [Prompd](https://github.com/Prompd/prompd-app) ecosystem. Use these as starting points for your own prompts, or install them directly as dependencies in your projects.

## What's Inside

This repository contains `@prompd/public-examples` — a reference package demonstrating the core features of the Prompd prompt composition system: inheritance, template composition, typed parameters, and context injection.

### Prompts

| Prompt | Description |
|--------|-------------|
| `api-development.prmd` | API endpoint development with conditional logic for auth, validation, and framework selection |
| `base-prompt.prmd` | Foundation template for inheritance — clean structure other prompts build on |
| `basic-inheritance.prmd` | Inherits from `base-prompt.prmd` with Jinja2 conditionals and analysis depth |
| `package-inheritance.prmd` | Cross-package versioned inheritance from a published registry package |
| `team-project-planner.prmd` | Multi-role project planning with object and array parameters |

### Assistants

| Prompt | Description |
|--------|-------------|
| `code-assistant.prmd` | General-purpose coding assistant supporting 6 languages and 5 task modes |

### Context Files

| File | Type | Description |
|------|------|-------------|
| `typescript-examples.ts` | Code | Sample TypeScript class structures |
| `architecture-patterns.json` | Data | Architecture patterns with pros, cons, and tradeoffs |
| `deployment-config.yaml` | Config | Deployment strategies, monitoring, and backup policies |
| `code-review-checklist.md` | Documentation | Comprehensive code review checklist |

### Persona Files

| File | Description |
|------|-------------|
| `systems/system-admin.md` | System administrator role definition and competencies |
| `users/user-lead-engineer.md` | Technical lead role definition and responsibilities |

## Usage

### Install as a dependency

```bash
prompd install @prompd/public-examples@latest
```

### Run the main prompt

```bash
prompd run "@prompd/public-examples@latest" \
  --provider openai \
  -p endpoint_name="user authentication"
```

### Run a specific prompt

```bash
prompd run "@prompd/public-examples@latest/prompts/basic-inheritance.prmd" \
  --provider anthropic \
  -p topic="distributed systems" \
  -p analysis_depth="comprehensive"
```

### Compile to provider JSON

```bash
prompd compile "src/prompts/api-development.prmd" \
  --to-provider-json openai \
  -p endpoint_name="login" \
  -p auth_required=true
```

## Examples

### API Development

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
prompd run "@prompd/public-examples@latest/prompts/team-project-planner.prmd" \
  --provider anthropic \
  -p project_name="E-commerce Platform" \
  -p project_phase="development" \
  -p tech_stack='{"language":"typescript","framework":"fastify","architecture":"microservices"}' \
  -p team_roles='["developer","lead_engineer","system_admin","qa"]'
```

### Code Assistant

```bash
prompd run "@prompd/public-examples@latest/assistants/code-assistant.prmd" \
  --provider anthropic \
  -p language="typescript" \
  -p task_mode="implement" \
  -p include_tests=true
```

## File Format

Prompd files use YAML frontmatter + Markdown body with Jinja2 templating:

```yaml
---
name: my-prompt
version: 1.0.0
inherits: "./base-prompt.prmd"
parameters:
  - name: topic
    type: string
    required: true
    description: "The topic to analyze"
---

# System

You are an expert analyst.

# User

Analyze {topic} in depth.

{%- if analysis_depth == "comprehensive" %}
Include historical context and future projections.
{%- endif %}
```

### Key Concepts

**Inheritance** — Prompts can extend other prompts, locally or from published packages:
```yaml
inherits: "./base-prompt.prmd"                              # Local file
inherits: "@prompd/public-examples@^1.0.0/prompts/base.prmd"  # Package
```

**Parameters** — Typed, validated inputs with defaults and enums:
```yaml
parameters:
  - name: language
    type: string
    enum: [typescript, python, go, rust, java, csharp]
    default: typescript
```

**Context injection** — Reference files that get compiled into the prompt:
```yaml
contexts:
  - "contexts/typescript-examples.ts"
  - "contexts/architecture-patterns.json"
```

## Project Structure

```
public-examples/
├── src/
│   ├── manifest.json           # Package metadata and dependencies
│   ├── prompts/                # Prompt files (.prmd)
│   ├── assistants/             # Assistant role prompts
│   ├── systems/                # System persona files (.md)
│   ├── users/                  # User persona files (.md)
│   └── contexts/               # Context files (code, data, docs)
└── dist/                       # Built package bundles (.pdpkg)
```

## Contributing

Want to add your own prompts to the community collection?

1. Fork this repository
2. Add your `.prmd` files following the existing patterns
3. Test with `prompd validate` and `prompd run`
4. Submit a pull request

## Related

- [Prompd Desktop App](https://github.com/Prompd/prompd-app) — Visual IDE for building and deploying AI workflows
- [Prompd CLI](https://github.com/Prompd/prompd-cli) — Command-line toolchain for compiling and managing prompts
- [Prompd Docs](https://github.com/Prompd/prompd-docs) — Format spec, guides, and reference documentation
- [Prompd Registry](https://www.prompdhub.ai/registry) — Browse and install community packages

## License

MIT License — see [LICENSE](LICENSE) for details.