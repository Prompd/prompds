# @prompd/structured-extractor

Extract structured JSON from unstructured text using a caller-defined schema. Designed for ETL pipelines, data ingestion, and automated processing where output must be valid, schema-compliant JSON with zero hallucination tolerance.

## How it works

You provide the raw text and a JSON schema describing the shape of the output you want. The extractor maps values from the source text onto your schema fields, applies normalization rules, and returns JSON only — no prose, no code fences, no explanation.

The core behavioral contract is strict: if a value cannot be extracted from the source text with sufficient confidence, it is set to `null`. The model does not guess, infer from context, or fill in plausible-sounding values. This makes it safe to run in automated pipelines where fabricated data causes downstream failures.

Two modes extend the default behavior:

- **Strict mode** (default `true`): every extracted value must be directly traceable to specific text in the input. Ambiguous fields return `null`.
- **Array mode** (`false` by default): when the source text contains multiple entities matching your schema (e.g., a list of invoices in one document), enable this to return an array of objects instead of a single object.

## Output

When `array_mode` is false, returns a single JSON object conforming to your schema. When `array_mode` is true, returns a JSON array of objects, maintaining source order.

All fields in your schema appear in the output — missing fields are `null`, never absent.

## Data normalizations applied automatically

| Type | Normalization |
|---|---|
| Dates | ISO 8601 (`YYYY-MM-DD`) |
| Phone numbers | E.164 format (`+1XXXXXXXXXX`) |
| Currency | Numeric only, no symbols |
| Strings | Extracted as-is — no spelling correction or abbreviation expansion unless schema description requests it |

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `input_text` | string | yes | — | Raw unstructured text to extract from |
| `schema` | object | yes | — | JSON schema defining field names, types, and descriptions |
| `strict_mode` | boolean | no | `true` | Require direct traceability; return `null` for ambiguous fields |
| `array_mode` | boolean | no | `false` | Extract multiple entities as an array |
| `confidence_threshold` | number | no | `0.8` | Fields below this confidence score are set to `null` (0.0–1.0) |

## Use cases

- Invoice and receipt data extraction
- Resume parsing into structured candidate records
- Legal document field extraction (parties, dates, terms)
- Email-to-ticket ingestion pipelines
- Form digitization from scanned or OCR'd text
