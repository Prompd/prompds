# @guardrails/common

Common guardrail prompts for inline filtering of LLM inputs and outputs. Drop these into any workflow as guardrail nodes to enforce safety, quality, and compliance constraints on every LLM call.

## Guardrails included

| Guardrail | File | Purpose |
|---|---|---|
| **PII Filter** | `prompts/pii-filter.prmd` | Detect and flag personally identifiable information (emails, SSNs, phone numbers, addresses, financial data) |
| **Content Policy** | `prompts/content-policy.prmd` | Enforce content policy rules (violence, hate speech, illegal activity, harassment, misinformation) |
| **Topic Fence** | `prompts/topic-fence.prmd` | Keep conversations on-topic, detect derailment attempts and conversational drift |
| **Output Validator** | `prompts/output-validator.prmd` | Validate LLM output against expected format (JSON schema, examples, or descriptions) |
| **Toxicity Filter** | `prompts/toxicity-filter.prmd` | Score text for toxic, hostile, or offensive language across multiple dimensions |
| **Hallucination Check** | `prompts/hallucination-check.prmd` | Compare LLM output against source documents to detect fabricated or unsupported claims |

## Usage

Each guardrail is a standalone `.prmd` file that can be referenced individually:

```yaml
using:
  - name: "@guardrails/common@0.0.1"
    prefix: "@guard"

# Then reference individual guardrails:
# @guard/prompts/pii-filter.prmd
# @guard/prompts/toxicity-filter.prmd
```

Or use them directly in workflow guardrail nodes by pointing to the specific prompt file.

## Design philosophy

These guardrails are designed as **inline filters**, not batch evaluation tools. The difference:

- **Inline filter** (this package): Runs on every LLM call in a workflow. Fast, focused, returns a structured pass/fail verdict. Use in guardrail nodes.
- **Batch evaluator** (e.g., `@prompd/safety-evaluator`): Runs after the fact on collected outputs. Deeper analysis, weighted scoring, evaluation reports. Use in eval pipelines.

Every guardrail returns structured JSON output with a clear verdict, making them easy to wire into conditional workflow logic.

## Parameters

All guardrails share a common pattern:
- Required: the text/output to evaluate
- Optional: configuration to tune sensitivity, restrict categories, or customize thresholds
- Output: structured JSON with a boolean verdict and detailed findings

See each `.prmd` file's frontmatter for the full parameter specification.
