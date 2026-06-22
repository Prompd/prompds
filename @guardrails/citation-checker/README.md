# @guardrails/citation-checker

Audits LLM-generated output for factual claims that are not grounded in the provided source context. Designed for RAG pipelines where responses must be traceable to retrieved documents, and for any system where fabricated or unsupported assertions are a quality or compliance concern.

## How it works

The checker extracts factual claims from the LLM output — numerical values, named entity attributes, temporal assertions, causal statements, and comparatives — and evaluates each one against the provided source context. Claims are categorized as grounded (directly supported by source text), ungrounded (not traceable to the source), or contradicted (in direct conflict with source content).

Strictness controls how the checker handles paraphrasing: at `high` strictness, claims must be near-verbatim in the source; at `medium`, reasonable paraphrases are accepted but specific numbers and dates must appear explicitly; at `low`, only claims with no plausible derivation from the source are flagged.

A `score` field (0.0 to 1.0) gives the proportion of grounded claims for use in threshold-based pipeline gating. Output is always JSON only.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `output` | string | yes | — | The LLM-generated text to check for ungrounded claims |
| `source_context` | string | yes | — | The source documents or context the LLM was given. Claims must be traceable to this. |
| `strictness` | string | no | `"medium"` | Detection sensitivity — `low`, `medium`, or `high`. High flags any claim not verbatim in context. |

## Example

**Input:**
```json
{
  "output": "The company was founded in 1987. Revenue grew 23% year-over-year, reaching $4.2M.",
  "source_context": "YoY revenue growth reached 23%. Total revenue for the period was $4.2M.",
  "strictness": "medium"
}
```

**Output:**
```json
{
  "ungrounded_claims": [
    {"claim": "The company was founded in 1987", "reason": "No founding date mentioned in source context"}
  ],
  "grounded_claims": [
    {"claim": "Revenue grew 23% year-over-year", "source_excerpt": "YoY revenue growth reached 23%"},
    {"claim": "reaching $4.2M", "source_excerpt": "Total revenue for the period was $4.2M"}
  ],
  "contradicted_claims": [],
  "score": 0.67,
  "summary": "1 of 3 claims could not be grounded in the provided context"
}
```

## Install

```
prompd install @guardrails/citation-checker
```
