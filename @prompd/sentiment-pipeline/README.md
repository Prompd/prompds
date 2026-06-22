# @prompd/sentiment-pipeline

Production-grade sentiment analysis returning overall sentiment, calibrated confidence scores, aspect-level breakdowns, detected emotions, and trend signals. Suitable for customer feedback pipelines, NPS follow-up analysis, support ticket sentiment tracking, and review monitoring.

Extends `@prompd/base-llm-evaluator`. Aspect detection is automatic by default but can be constrained to a caller-specified list. An optional context window allows prior conversation to inform interpretation of ambiguous sentiment.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `text` | string | yes | — | The text to analyze for sentiment |
| `aspects` | array | no | `[]` | Specific aspects to analyze. Empty means auto-detect aspects from the text. |
| `include_intensity` | boolean | no | `true` | Include emotional intensity score (0.0-1.0) alongside direction |
| `context_window` | string | no | — | Prior conversation or context to aid interpretation |

## Example

Input:
```json
{
  "text": "Your support team was incredibly helpful and resolved my issue quickly. That said, the pricing has gotten way too expensive and I'm honestly not sure we can justify renewing at this rate.",
  "aspects": ["pricing", "support"],
  "include_intensity": true
}
```

Output:
```json
{
  "overall_sentiment": "mixed",
  "confidence": 0.94,
  "intensity": 0.72,
  "aspects": [
    {
      "aspect": "pricing",
      "sentiment": "negative",
      "confidence": 0.95,
      "excerpt": "pricing has gotten way too expensive"
    },
    {
      "aspect": "support",
      "sentiment": "positive",
      "confidence": 0.97,
      "excerpt": "support team was incredibly helpful and resolved my issue quickly"
    }
  ],
  "emotions": ["frustration", "appreciation"],
  "trend_signal": "unknown",
  "key_phrases": [
    "incredibly helpful",
    "resolved my issue quickly",
    "way too expensive",
    "not sure we can justify renewing"
  ]
}
```

## Install

```
prompd install @prompd/sentiment-pipeline
```
