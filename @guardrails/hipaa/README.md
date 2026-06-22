# @guardrails/hipaa

Detects Protected Health Information (PHI) in text, covering all 18 HIPAA Safe Harbor identifiers plus extended clinical data types including MRNs, ICD-10/ICD-11 diagnosis codes, CPT procedure codes, DEA provider numbers, and insurance member identifiers.

Use this guardrail to screen text before storing, logging, or forwarding it — anywhere PHI exposure creates regulatory liability under HIPAA. It operates as a pure analysis layer: pass text in, receive a structured JSON finding set back. Three action modes control downstream behavior: flag for audit trails, redact for scrubbing pipelines, and reject for hard-stop enforcement gates.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `text` | string | yes | — | The text to analyze for PHI content |
| `action` | string | no | `"flag"` | What to do when PHI is found — `flag`, `redact`, or `reject` |
| `phi_categories` | array | no | `["all"]` | Specific PHI categories to check: `mrn`, `diagnosis`, `procedure`, `insurance`, `dea`, `name`, `dob`, `address`, `phone`, `email`, `ssn`, or `all` |

## Example

**Input**

```json
{
  "text": "Patient John Smith, MRN-4892017, was admitted on 03/15/1978 and diagnosed with ICD-10: E11.9. His insurance member ID is BCB-00291847. Prescribing physician DEA: AB1234563.",
  "action": "redact",
  "phi_categories": ["all"]
}
```

**Output**

```json
{
  "phi_detected": true,
  "findings": [
    {
      "category": "name",
      "value": "John Smith",
      "location": "sentence 1",
      "confidence": 0.98
    },
    {
      "category": "mrn",
      "value": "MRN-4892017",
      "location": "sentence 1",
      "confidence": 0.99
    },
    {
      "category": "dob",
      "value": "03/15/1978",
      "location": "sentence 1",
      "confidence": 0.95
    },
    {
      "category": "diagnosis",
      "value": "ICD-10: E11.9",
      "location": "sentence 1",
      "confidence": 0.99
    },
    {
      "category": "insurance",
      "value": "BCB-00291847",
      "location": "sentence 2",
      "confidence": 0.96
    },
    {
      "category": "dea",
      "value": "AB1234563",
      "location": "sentence 3",
      "confidence": 0.97
    }
  ],
  "redacted_text": "Patient [NAME-REDACTED], [MRN-REDACTED], was admitted on [DOB-REDACTED] and diagnosed with [DIAGNOSIS-REDACTED]. His insurance member ID is [INSURANCE-REDACTED]. Prescribing physician DEA: [DEA-REDACTED].",
  "action_taken": "redact",
  "phi_count": 6
}
```

## Install

```
prompd install @guardrails/hipaa
```
