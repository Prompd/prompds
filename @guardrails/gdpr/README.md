# @guardrails/gdpr

Detects EU personal data and special category data in text, assesses legal basis requirements under GDPR Articles 6 and 9, and identifies right-to-erasure triggers and Data Protection Authority notification risk.

This guardrail is designed for pipelines that process text potentially containing EU data subject information — customer support transcripts, document ingestion, AI-generated summaries, and similar workloads. It returns a structured JSON report covering what personal data was found, whether it qualifies as special category data requiring explicit consent, and a risk summary suitable for audit logging or automated enforcement gates.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `text` | string | yes | — | The text to analyze for EU personal data |
| `jurisdiction` | string | no | `"EU"` | Legal jurisdiction — `EU`, `UK`, or `EEA`. Affects which regulations apply. |
| `processing_purpose` | string | no | — | Stated purpose for processing this data. Used to assess legal basis adequacy under Article 6. |

## Example

**Input**

```json
{
  "text": "Customer jan.kowalski@example.pl called regarding his diabetes treatment. He is a member of the Workers Union of Poland and requested deletion of his account.",
  "jurisdiction": "EU",
  "processing_purpose": "Customer support case resolution"
}
```

**Output**

```json
{
  "personal_data_detected": true,
  "legal_basis_required": true,
  "findings": [
    {
      "category": "contact_data",
      "value": "jan.kowalski@example.pl",
      "special_category": false,
      "right_to_erasure_applicable": true,
      "requires_explicit_consent": false
    },
    {
      "category": "health_data",
      "value": "diabetes treatment",
      "special_category": true,
      "right_to_erasure_applicable": true,
      "requires_explicit_consent": true
    },
    {
      "category": "trade_union_membership",
      "value": "Workers Union of Poland",
      "special_category": true,
      "right_to_erasure_applicable": true,
      "requires_explicit_consent": true
    }
  ],
  "special_category_data": true,
  "dpa_notification_likely_required": true,
  "risk_summary": "Text contains special category health and trade union data requiring explicit consent under GDPR Art. 9; right-to-erasure request identified and must be actioned within 30 days."
}
```

## Install

```
prompd install @guardrails/gdpr
```
