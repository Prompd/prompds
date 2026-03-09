# @prompd/batch-classifier

Classify arrays of text items into predefined categories with confidence scores. Built for automated data pipelines where output must be deterministic, schema-compliant, and machine-parseable.

## How it works

You pass in a list of text items and a list of categories. Each category can have a name, description, and example values to help the model understand the boundaries. The classifier scores every item against every category and assigns either a single best-fit category or multiple categories (multi-label mode), along with a confidence score.

Items that don't clearly fit any category — or fall below the configurable `unknown_threshold` — are bucketed into `_unknown` rather than being forced into the closest match. This is intentional: pipelines need to know when to route items to human review rather than silently miscategorize them.

Output is JSON only. The model produces no prose, no markdown, no explanation — just the structured result ready for your downstream consumer.

## Output structure

```json
{
  "batch_id": "optional-trace-id",
  "item_count": 42,
  "category_distribution": {
    "billing": 18,
    "support": 12,
    "feedback": 8,
    "_unknown": 4
  },
  "results": [
    {
      "index": 0,
      "input": "my card was charged twice",
      "category": "billing",
      "confidence": 0.94,
      "reasoning": "Explicit mention of a double charge indicates a billing dispute."
    }
  ]
}
```

In multi-label mode, each result has a `classifications` array instead of a single `category` field.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `items` | array | yes | — | Array of strings to classify |
| `categories` | array | yes | — | Category objects with `name`, optional `description` and `examples` |
| `multi_label` | boolean | no | `false` | Allow each item to belong to multiple categories |
| `include_reasoning` | boolean | no | `false` | Add a brief reasoning string per item (increases token usage) |
| `unknown_threshold` | number | no | `0.5` | Confidence below this maps to `_unknown` instead of forcing a category |
| `batch_id` | string | no | — | Optional identifier included in output for pipeline traceability |

## Behavioral notes

- **Consistency**: identical or near-identical items receive identical classifications within the same batch
- **Calibration**: confidence scores reflect actual certainty — they don't default to high values
- **Order preservation**: results array matches the order of the input `items` array exactly
- **Conservative bias**: when uncertain, the model prefers lower confidence over a confident wrong answer

## Use cases

- Support ticket routing by issue type
- Content moderation pipeline pre-screening
- Log line categorization for alerting rules
- Data labeling at scale before human review
- Customer feedback bucketing for analytics
