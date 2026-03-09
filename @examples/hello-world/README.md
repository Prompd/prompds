# @examples/hello-world

The simplest possible Prompd package. One prompt, one parameter.

## Usage

```bash
# Compile to see the rendered output
prompd compile prompts/hello.prmd --param name="Stephen"

# Run with a provider
prompd run prompts/hello.prmd --provider openai --model gpt-4o --param name="Stephen"
```

## What This Shows

- Minimal `.prmd` file structure (YAML frontmatter + Markdown body)
- Defining a typed parameter with a default value
- Using `{{ name }}` template syntax to inject parameters
- Minimal `prompd.json` package manifest

## License

Elastic License 2.0 (ELv2) - See [LICENSE](../../LICENSE)
