# @examples/code-review-skill

A skill package example demonstrating how to create reusable tools that agents can invoke.

## What This Shows

- The `"type": "skill"` package type in `prompd.json`
- The `"tools"` array declaring callable tool names
- System prompts that define the skill's persona
- Context files that provide reference material to the LLM
- Multiple prompts within a single skill package

## Tools

| Tool | Description |
|------|-------------|
| `review-code` | Reviews code for correctness, security, performance, and best practices |
| `suggest-tests` | Suggests unit tests for a given code snippet |

## Files

- `prompts/review-code.prmd` - Code review prompt with configurable focus areas
- `prompts/suggest-tests.prmd` - Test suggestion prompt
- `systems/code-reviewer.md` - System prompt defining the reviewer persona
- `contexts/review-checklist.md` - Reference checklist used during reviews

## Usage

```bash
# Run the code review prompt
prompd run prompts/review-code.prmd \
  --provider openai --model gpt-4o \
  --param language="typescript" \
  --param focus="security" \
  --param code="function login(user, pass) { return db.query('SELECT * FROM users WHERE name=' + user); }"

# Run the test suggestion prompt
prompd run prompts/suggest-tests.prmd \
  --provider openai --model gpt-4o \
  --param language="python" \
  --param framework="pytest" \
  --param code="def divide(a, b): return a / b"
```

## License

Elastic License 2.0 (ELv2) - See [LICENSE](../../LICENSE)
