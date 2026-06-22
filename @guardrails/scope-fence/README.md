# @guardrails/scope-fence

Validates that agent and LLM output stays within defined task boundaries. Detects off-topic content, unauthorized actions, and role drift — three failure modes common in agentic pipelines where a model exceeds its intended scope.

This guardrail sits in the output layer of an agent loop. After the agent produces a response, pass it here along with the original task description and the list of topics the agent is permitted to address. The guardrail returns a structured assessment with specific violations, a scope coverage score, and a containment recommendation that your orchestration layer can act on directly.

Two modes are available: standard mode allows closely related topics that are reasonably implied by the scope definition, while strict mode requires every claim to map explicitly to the allowed topics list — appropriate for high-stakes or regulated deployments.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `output` | string | yes | — | The agent or LLM output to validate against scope boundaries |
| `allowed_topics` | array | yes | — | List of topics or domains the agent is permitted to address |
| `task_description` | string | yes | — | The original task the agent was given. Used as the scope anchor. |
| `strict_mode` | boolean | no | `false` | When `true`, any content not explicitly in `allowed_topics` fails. When `false`, closely related topics pass. |

## Example

**Input**

```json
{
  "output": "Your account balance is $1,240.00. You should also consider your investment portfolio — given current market conditions, I'd recommend reallocating to bonds. As your financial advisor, I can help you build a long-term wealth strategy.",
  "allowed_topics": ["account balance inquiries", "billing questions", "payment methods"],
  "task_description": "Answer customer questions about their account balance and billing.",
  "strict_mode": false
}
```

**Output**

```json
{
  "in_scope": false,
  "violations": [
    {
      "type": "off_topic",
      "excerpt": "You should also consider your investment portfolio — given current market conditions, I'd recommend reallocating to bonds.",
      "reason": "Investment advice is outside the permitted scope of account balance and billing inquiries"
    },
    {
      "type": "role_drift",
      "excerpt": "As your financial advisor, I can help you build a long-term wealth strategy.",
      "reason": "Agent assumed the role of financial advisor, an unauthorized identity outside its customer service scope"
    }
  ],
  "scope_coverage": 0.28,
  "recommendation": "block"
}
```

## Install

```
prompd install @guardrails/scope-fence
```
