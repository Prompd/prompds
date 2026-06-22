# @prompd/contract-analyzer

Analyzes contract text and returns a structured JSON summary of parties, key dates, obligations, termination conditions, and risk flags. Designed for legal operations pipelines, contract management systems, and compliance workflows where contracts must be ingested at scale without manual review for every document.

The analyzer identifies clause types present in the document, extracts obligations per party, and surfaces risk flags with citations to specific sections. Both the analysis scope and the minimum risk level for inclusion are configurable per call.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `contract_text` | string | yes | — | The full contract text to analyze |
| `focus_areas` | array | no | `["all"]` | Clause types to analyze: `termination`, `liability`, `ip`, `payment`, `confidentiality`, `indemnification`, or `all` |
| `risk_threshold` | string | no | `"medium"` | Minimum risk level to surface in findings: `low`, `medium`, or `high` |

## Example

Input:
```json
{
  "contract_text": "SERVICE AGREEMENT\n\nThis Agreement is entered into as of January 1, 2024 (\"Effective Date\") by Acme Corp (\"Service Provider\") and Beta LLC (\"Client\")...\n[full contract text]",
  "focus_areas": ["termination", "liability"],
  "risk_threshold": "medium"
}
```

Output:
```json
{
  "parties": [
    {"role": "Service Provider", "name": "Acme Corp"},
    {"role": "Client", "name": "Beta LLC"}
  ],
  "effective_date": "2024-01-01",
  "expiration_date": "2025-12-31",
  "auto_renewal": true,
  "governing_law": "Delaware, USA",
  "key_obligations": [
    {"party": "Acme Corp", "obligation": "Deliver monthly reports by the 5th", "deadline": "Monthly"}
  ],
  "termination_conditions": [
    {"trigger": "30-day written notice", "type": "convenience"},
    {"trigger": "Material breach uncured after 15 days", "type": "cause"}
  ],
  "risk_flags": [
    {
      "clause": "Limitation of Liability",
      "risk_level": "high",
      "detail": "Liability cap of $500 is below typical industry standard",
      "location": "Section 8.2"
    }
  ],
  "clause_inventory": ["payment_terms", "confidentiality", "ip_assignment", "indemnification", "limitation_of_liability"]
}
```

## Install

```
prompd install @prompd/contract-analyzer
```
