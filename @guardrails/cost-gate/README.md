# @guardrails/cost-gate

Estimates the token count of an input against a configured budget and applies truncation when the input exceeds the limit. Returns a structured JSON report with the token estimate, budget status, truncated input (if applicable), and tokens removed.

This guardrail belongs at the front of any pipeline where unbounded user input could cause cost overruns, context window exhaustion, or latency spikes. Configure the maximum token budget and target model once; the guardrail handles estimation using model-specific tokenizer heuristics and applies one of four truncation strategies to bring over-budget inputs back within limits before they reach the model call.

Token estimates are approximations derived from character-to-token ratios for the target model's tokenizer. Actual counts may vary by up to 10% from real tokenizer output.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `input` | string | yes | — | The text to measure and optionally truncate |
| `max_tokens` | number | yes | — | Maximum allowed token count for the input |
| `model` | string | no | `"gpt-4o"` | Target model for token estimation: `gpt-4o`, `gpt-3.5-turbo`, `claude-3-5-sonnet`, `claude-3-haiku`, `gemini-1.5-pro` |
| `truncation_strategy` | string | no | `"end"` | How to truncate if over budget: `start`, `end`, `middle`, or `summarize` |

## Truncation Strategies

| Strategy | Behavior |
|---|---|
| `end` | Removes content from the end, preserving the beginning |
| `start` | Removes content from the beginning, preserving the end |
| `middle` | Removes content from the middle, preserving beginning and end equally |
| `summarize` | Compresses redundant and repetitive content without removing unique information |

## Example

**Input**

```json
{
  "input": "[a long document with approximately 4,821 tokens of content]",
  "max_tokens": 2000,
  "model": "gpt-4o",
  "truncation_strategy": "end"
}
```

**Output**

```json
{
  "estimated_tokens": 4821,
  "max_tokens": 2000,
  "within_budget": false,
  "truncation_applied": true,
  "truncation_strategy": "end",
  "truncated_input": "[first 2000 tokens of content, trailing content removed]",
  "tokens_removed": 2821,
  "model": "gpt-4o"
}
```

**Within-budget output**

```json
{
  "estimated_tokens": 843,
  "max_tokens": 2000,
  "within_budget": true,
  "truncation_applied": false,
  "truncation_strategy": null,
  "truncated_input": "[original input unchanged]",
  "tokens_removed": 0,
  "model": "gpt-4o"
}
```

## Install

```
prompd install @guardrails/cost-gate
```
