# @guardrails/json-enforcer

Validates that LLM-generated output is parseable JSON conforming to a target schema. When repair mode is enabled, it attempts to fix common LLM formatting mistakes — such as markdown code fences, trailing commas, and unquoted keys — before reporting a failure. Designed as a post-processing guardrail in pipelines where structured JSON output is required.

## How it works

The enforcer first attempts to parse the LLM output as-is. When repair mode is enabled and parsing fails, it applies a sequence of targeted repairs: stripping markdown fences, removing prose preamble or postamble, fixing trailing commas, correcting unquoted keys, and replacing single quotes with double quotes. Only the minimum repairs needed to produce valid JSON are applied — the content is never rewritten.

Once the output is parseable, it is validated against the provided JSON Schema. Required fields, types, constraints, and enumerated values are all enforced. Every violation is reported with a JSONPath location and message.

Output is always JSON only. No prose is returned.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `llm_output` | string | yes | — | The raw LLM output string to validate and optionally repair |
| `expected_schema` | object | yes | — | JSON Schema object the output must conform to |
| `repair_mode` | boolean | no | `true` | Attempt to repair common formatting issues before failing |

## Example

**Input:**
```json
{
  "llm_output": "```json\n{\"name\": \"Acme Corp\", \"amount\": 1500.00,}\n```",
  "expected_schema": {
    "type": "object",
    "required": ["name", "amount"],
    "properties": {
      "name": {"type": "string"},
      "amount": {"type": "number"}
    }
  },
  "repair_mode": true
}
```

**Output:**
```json
{
  "valid": true,
  "repaired": true,
  "parsed_output": {"name": "Acme Corp", "amount": 1500.00},
  "errors": [],
  "repairs_applied": ["stripped_markdown_fences", "fixed_trailing_comma"]
}
```

## Install

```
prompd install @guardrails/json-enforcer
```
