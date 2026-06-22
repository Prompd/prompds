# @guardrails/language-detect

Detects the language of input text using BCP-47 language tags and validates it against a caller-defined list of permitted locales. Designed for pipelines that must enforce language policies — such as restricting a customer-facing LLM to supported languages, or routing multilingual inputs to the correct downstream handler.

## How it works

The detector identifies the dominant language of the input and produces a BCP-47 tag, a confidence score, and the full English language name. It then compares the detected language against the `allowed_languages` list using BCP-47 matching rules: a regional tag (`en-GB`) matches a base-language entry (`en`), but a base tag does not automatically match a region-specific entry.

When the detected language is not in the allowed list, the configured `action_on_mismatch` determines the outcome: `flag` records the mismatch without blocking, `reject` signals that the input should be blocked, and `translate` indicates a translation to the first allowed language is required.

Output is always JSON only. No prose is returned.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `input` | string | yes | — | The text to analyze for language detection |
| `allowed_languages` | array | yes | — | BCP-47 language codes that are permitted (e.g. `["en", "en-US", "fr", "es"]`) |
| `action_on_mismatch` | string | no | `"flag"` | What to do when the detected language is not allowed — `flag`, `reject`, or `translate` |

## Example

**Input:**
```json
{
  "input": "Bonjour, je voudrais annuler ma commande.",
  "allowed_languages": ["en", "en-US"],
  "action_on_mismatch": "flag"
}
```

**Output:**
```json
{
  "detected_language": "fr",
  "confidence": 0.98,
  "language_name": "French",
  "allowed": false,
  "action_taken": "flag",
  "translation_needed": null,
  "message": "Input detected as French (fr), not in allowed list: [\"en\", \"en-US\"]"
}
```

## Install

```
prompd install @guardrails/language-detect
```
