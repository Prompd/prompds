# @prompd/support-triage

Classifies, prioritizes, and routes incoming support tickets against a caller-defined set of categories and routing rules. Returns structured JSON with category, subcategory, priority, assigned team, customer sentiment, urgency signals, and a one-sentence summary — ready for direct ingestion by ticketing systems and helpdesk automation.

Categories and routing are fully configurable per call, making this suitable for multi-product support organizations where team boundaries and priority rules vary by queue.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `ticket_text` | string | yes | — | The full support ticket text including subject and body |
| `categories` | array | yes | — | Valid category strings to classify into |
| `priority_rules` | object | no | `{}` | Condition-to-priority override map (e.g. `{"billing_issue": "P2"}`) |
| `routing_map` | object | no | `{}` | Category-to-team routing map (e.g. `{"billing": "finance-team"}`) |

## Example

Input:
```json
{
  "ticket_text": "Subject: Charged twice for March\n\nHi, I just noticed I was charged twice for my March subscription — once on March 1 and again on March 3. I need this resolved today, this is unacceptable.",
  "categories": ["billing", "technical", "account", "feature-request"],
  "priority_rules": {"billing_issue": "P2"},
  "routing_map": {"billing": "finance-team", "technical": "eng-tier-2"}
}
```

Output:
```json
{
  "category": "billing",
  "subcategory": "incorrect_charge",
  "priority": "P2",
  "assigned_team": "finance-team",
  "sentiment": "frustrated",
  "urgency_signals": ["charged twice", "need this resolved today", "unacceptable"],
  "suggested_response_template": "billing_duplicate_charge",
  "summary": "Customer reports being charged twice for their March subscription and is requesting an immediate resolution.",
  "customer_intent": "refund_request"
}
```

## Install

```
prompd install @prompd/support-triage
```
