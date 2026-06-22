# @guardrails/format-validator

Validates that LLM-generated output conforms to structural requirements: required sections are present, prohibited phrases are absent, and character length falls within configured bounds. Designed for pipelines where output must meet editorial, legal, or UX compliance standards before delivery.

## How it works

The validator evaluates the output against up to four constraint types simultaneously. Required sections are matched case-insensitively as substrings, so a required heading of "Summary" will match "Executive Summary" in the output. Prohibited phrases are also matched case-insensitively and include location context in the violation report. Length is measured in characters.

Every constraint failure is recorded as a violation with a type and human-readable detail. The `valid` field is only true when there are zero violations across all constraint types.

Output is always JSON only. No prose is returned.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `output` | string | yes | — | The LLM-generated text to validate against format requirements |
| `required_sections` | array | no | `[]` | Section headings or phrases that must appear in the output |
| `max_length` | number | no | `0` | Maximum character length. `0` means no limit. |
| `min_length` | number | no | `0` | Minimum character length. `0` means no limit. |
| `prohibited_phrases` | array | no | `[]` | Phrases or keywords that must NOT appear in the output |

## Example

**Input:**
```json
{
  "output": "Here is what I think. I cannot provide specific legal advice. Please consult a lawyer.",
  "required_sections": ["Summary", "Recommendation"],
  "max_length": 2000,
  "min_length": 100,
  "prohibited_phrases": ["I cannot", "I am unable"]
}
```

**Output:**
```json
{
  "valid": false,
  "violations": [
    {"type": "missing_section", "detail": "Required section 'Summary' not found in output"},
    {"type": "missing_section", "detail": "Required section 'Recommendation' not found in output"},
    {"type": "prohibited_phrase", "detail": "Output contains prohibited phrase 'I cannot'", "location": "sentence 2"},
    {"type": "below_min_length", "detail": "Output length 87 is below minimum required length of 100"}
  ],
  "length": 87,
  "within_length_limits": false
}
```

## Install

```
prompd install @guardrails/format-validator
```
