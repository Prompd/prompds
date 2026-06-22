# @prompd/churn-signal-detector

Analyzes customer communications — emails, support tickets, survey responses, or chat messages — and returns a structured churn risk assessment. Produces a risk score, detected signals with supporting excerpts, a recommended action, and suggested talking points for customer success teams.

Signal categories are configurable so you can focus detection on the signals relevant to your retention workflow. Optional account metadata (plan tier, tenure, NPS) is incorporated into risk scoring when provided.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `customer_text` | string | yes | — | Customer message, email, support ticket, or survey response to analyze |
| `account_context` | object | no | `{}` | Account metadata to contextualize risk (e.g. plan, months_active, recent_nps) |
| `signal_categories` | array | no | `["all"]` | Signal types to detect: `competitor`, `frustration`, `cancellation`, `value_doubt`, `support_fatigue`, or `all` |

## Example

Input:
```json
{
  "customer_text": "Hi, we've been using your platform for over a year but honestly we're looking at other tools now. Not sure this is worth the cost at our current usage level. Your team has been helpful when we reach out but we've had to reach out a lot.",
  "account_context": {
    "plan": "enterprise",
    "months_active": 18,
    "recent_nps": 4
  },
  "signal_categories": ["all"]
}
```

Output:
```json
{
  "churn_risk_score": 0.82,
  "risk_level": "high",
  "signals_detected": [
    {
      "category": "competitor",
      "signal": "evaluating_alternatives",
      "excerpt": "we're looking at other tools now",
      "weight": 0.40
    },
    {
      "category": "value_doubt",
      "signal": "roi_question",
      "excerpt": "not sure this is worth the cost at our current usage level",
      "weight": 0.35
    },
    {
      "category": "support_fatigue",
      "signal": "repeated_contact",
      "excerpt": "we've had to reach out a lot",
      "weight": 0.20
    }
  ],
  "recommended_action": "escalate_to_csm",
  "suggested_talking_points": [
    "Review account usage data and identify underutilized features relative to their plan",
    "Prepare ROI summary using their specific usage metrics and outcomes",
    "Offer an executive business review to realign on value delivered",
    "Address support volume — identify root cause and present a resolution plan"
  ],
  "urgency": "within_24_hours"
}
```

## Install

```
prompd install @prompd/churn-signal-detector
```
