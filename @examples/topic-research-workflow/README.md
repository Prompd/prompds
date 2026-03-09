# @examples/topic-research-workflow

A simple workflow example demonstrating the basic **trigger -> prompt -> output** pattern in Prompd.

## What This Shows

- How to define a `.pdflow` workflow file
- Connecting a trigger node to a prompt node to an output node
- Passing workflow parameters into a `.prmd` prompt file
- Using `sourceType: "file"` to reference local prompt files

## Files

- `main.pdflow` - The workflow definition (3 nodes, 2 edges)
- `prompts/topic-researcher.prmd` - The prompt that gets executed

## Usage

```bash
# Compile the prompt standalone
prompd compile prompts/topic-researcher.prmd

# Run the workflow
prompd run main.pdflow --provider openai --model gpt-4o --param topic="composable AI systems"
```

## License

Elastic License 2.0 (ELv2) - See [LICENSE](../../LICENSE)
