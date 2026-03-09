# Prompd Community Prompts

A collection of prompt packages and templates for the [Prompd](https://github.com/prompd/prompd-cli) ecosystem. Use these as starting points for your own prompts, or install them directly as dependencies in your projects.

## Repository Structure

```
prompds/
├── @prompd/                         # Official Prompd packages
│   ├── safety-evaluator/            # LLM safety evaluation toolkit
│   ├── structured-extractor/        # Structured data extraction
│   ├── batch-classifier/            # Batch classification workflows
│   ├── incident-triage/             # Incident response prompts
│   ├── webhook-transform/           # Webhook data transformation
│   ├── ci-gate/                     # CI/CD quality gate prompts
│   └── base-llm-evaluator/         # Base LLM evaluation framework
└── @examples/                       # Example packages and templates
    ├── hello-world/                 # Simplest possible package (start here)
    ├── examples/                    # Comprehensive examples (inheritance, composition, contexts)
    ├── core/                        # Core prompt patterns
    ├── blog-writing/                # Blog content generation
    ├── csv-toolkit/                 # CSV data processing
    ├── dog-blog-writing/            # Cross-package inheritance demo
    ├── asset-extraction/            # Binary file extraction (Excel, PDF, images)
    ├── demo-prompts/                # Demo prompts
    ├── code-review-skill/           # Skill package example (tools, system prompts)
    └── topic-research-workflow/     # Workflow example (trigger → prompt → output)
```

## Quick Start

```bash
# Install the CLI
npm install -g @prompd/cli

# Clone this repo and try the hello-world example
git clone https://github.com/Prompd/prompds
cd prompds/@examples/hello-world

# Compile to see the rendered prompt
prompd compile prompts/hello.prmd --param name="World"

# Run with a provider
prompd run prompts/hello.prmd --provider openai --model gpt-4o --param name="World"

# Install a published package from the registry
prompd install @prompd/safety-evaluator@latest
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

Analyze {{ topic }} in depth.

{%- if analysis_depth == "comprehensive" %}
Include historical context and future projections.
{%- endif %}
```

### Key Concepts

**Inheritance** -- Prompts can extend other prompts, locally or from published packages:
```yaml
inherits: "./base-prompt.prmd"                                  # Local file
inherits: "@prompd/safety-evaluator@^1.0.0/prompts/base.prmd"  # Package
```

**Parameters** -- Typed, validated inputs with defaults and enums:
```yaml
parameters:
  - name: language
    type: string
    enum: [typescript, python, go, rust, java, csharp]
    default: typescript
```

**Context injection** -- Reference files that get compiled into the prompt:
```yaml
contexts:
  - "contexts/typescript-examples.ts"
  - "contexts/architecture-patterns.json"
```

## Contributing

Want to add your own prompts to the community collection?

1. Fork this repository
2. Add your `.prmd` files following the existing patterns
3. Test with `prompd validate` and `prompd run`
4. Submit a pull request

## Related

- [Prompd CLI](https://github.com/prompd/prompd-cli) -- Command-line tools for compiling and managing prompts
- [Prompd App](https://github.com/prompd/prompd-app) -- Desktop IDE for AI workflows
- [Prompd API](https://github.com/prompd/prompd-api) -- API integration packages
- [Prompd Docs](https://github.com/prompd/prompd-docs) -- Format spec, guides, and reference
- [PrompdHub](https://prompdhub.ai) -- Package registry

## License

Elastic License 2.0 (ELv2) -- see [LICENSE](LICENSE) for details.
