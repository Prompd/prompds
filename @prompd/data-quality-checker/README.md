# @prompd/data-quality-checker

Validates batches of data records against configurable quality rules and returns a structured report with an overall quality score, pass/fail decision, per-record violations, a violation summary, and per-rule pass rates.

Supports five rule types: required field presence, format validation, range bounds, uniqueness within the batch, and referential integrity against a reference list. Designed for ETL pipelines and data ingestion workflows where data quality must be enforced and measured before records proceed downstream.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `records` | array | yes | — | Array of data record objects to validate |
| `rules` | array | yes | — | Array of rule objects, each with `name`, `field`, `type`, and `params` |
| `fail_threshold` | number | no | `0.8` | Quality score below which the batch is considered failed (0.0-1.0) |

### Rule object structure

Each rule in the `rules` array must have:
- `name` (string) — unique identifier for the rule, used in violation reports
- `field` (string) — the record field to validate
- `type` (string) — one of `required`, `format`, `range`, `uniqueness`, `referential`
- `params` (object) — type-specific parameters (e.g. `{"pattern": "^\\S+@\\S+\\.\\S+$"}` for format, `{"min": 0, "max": 100}` for range, `{"values": ["active", "inactive"]}` for referential)

## Example

Input:
```json
{
  "records": [
    {"customer_id": "C001", "email": "alice@example.com", "age": 29, "status": "active"},
    {"customer_id": "C002", "email": "notanemail", "age": 29, "status": "active"},
    {"customer_id": "C003", "email": "bob@example.com", "age": null, "status": "pending"},
    {"customer_id": null, "email": "carol@example.com", "age": 34, "status": "active"}
  ],
  "rules": [
    {"name": "required_customer_id", "field": "customer_id", "type": "required", "params": {}},
    {"name": "email_format", "field": "email", "type": "format", "params": {"pattern": "^\\S+@\\S+\\.\\S+$"}},
    {"name": "age_range", "field": "age", "type": "range", "params": {"min": 0, "max": 120}},
    {"name": "status_referential", "field": "status", "type": "referential", "params": {"values": ["active", "inactive", "suspended"]}}
  ],
  "fail_threshold": 0.8
}
```

Output:
```json
{
  "quality_score": 0.25,
  "passed": false,
  "total_records": 4,
  "passed_records": 1,
  "failed_records": [
    {
      "record_index": 1,
      "violations": [
        {"rule": "email_format", "field": "email", "value": "notanemail", "severity": "error"}
      ]
    },
    {
      "record_index": 2,
      "violations": [
        {"rule": "age_range", "field": "age", "value": null, "severity": "error"},
        {"rule": "status_referential", "field": "status", "value": "pending", "severity": "error"}
      ]
    },
    {
      "record_index": 3,
      "violations": [
        {"rule": "required_customer_id", "field": "customer_id", "value": null, "severity": "critical"}
      ]
    }
  ],
  "violation_summary": {
    "email_format": 1,
    "age_range": 1,
    "status_referential": 1,
    "required_customer_id": 1
  },
  "rule_pass_rates": {
    "required_customer_id": 0.75,
    "email_format": 0.75,
    "age_range": 0.75,
    "status_referential": 0.75
  }
}
```

## Install

```
prompd install @prompd/data-quality-checker
```
