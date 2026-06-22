# @guardrails/schema-validator

Validates that input conforms to an expected JSON Schema definition before it is passed to downstream processing. Reports every violation with a JSONPath location, human-readable message, and the actual value that failed. Optionally attempts type coercion to recover from common formatting issues before rejecting input.

## How it works

The validator parses the input as JSON, then validates it field-by-field against the provided schema. Required fields, type constraints, format rules, enumerated values, and array/object cardinality are all enforced. Nested objects and array items are validated recursively.

When `strict_mode` is enabled (the default), any property present in the input that is not declared in the schema is reported as a violation. When `coerce` is enabled, the validator attempts type conversions — such as converting the string `"42"` to the number `42` — before failing on a type mismatch.

Output is always JSON only. No prose is returned. This makes the skill safe to wire directly into automated pipeline gating.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `input` | string | yes | — | The raw input to validate — may be a JSON string or unstructured text |
| `schema` | object | yes | — | JSON Schema object defining the expected structure, types, and constraints |
| `strict_mode` | boolean | no | `true` | When true, fail on unknown properties. When false, allow extra fields. |
| `coerce` | boolean | no | `false` | Attempt type coercion (e.g. `"42"` to `42`) before failing on type mismatches |

## Example

**Input:**
```json
{
  "input": "{\"amount\": \"forty-two\", \"currency\": \"USD\"}",
  "schema": {
    "type": "object",
    "required": ["amount", "currency"],
    "properties": {
      "amount": {"type": "number"},
      "currency": {"type": "string", "enum": ["USD", "EUR", "GBP"]}
    }
  },
  "strict_mode": true,
  "coerce": true
}
```

**Output:**
```json
{
  "valid": false,
  "errors": [
    {"path": "$.amount", "message": "Expected number, got string", "value": "forty-two"}
  ],
  "coerced_input": {"amount": 42, "currency": "USD"},
  "coercion_applied": true
}
```

## Install

```
prompd install @guardrails/schema-validator
```
