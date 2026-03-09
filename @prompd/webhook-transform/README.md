# @prompd/webhook-transform

Transform webhook payloads between service formats using natural language mapping rules. Sits in integration pipelines between services that don't share schemas — eliminating custom glue code for each service pair.

## How it works

You provide the incoming payload, identify the source and target services, and optionally supply explicit field mappings. The transformer applies the mappings, handles type normalization, and returns a clean JSON payload ready for the target service to consume — along with metadata about what was mapped, dropped, and any warnings.

When no explicit `mapping_rules` are provided, the transformer infers the target format from known conventions for that service. When you provide a `target_schema`, the output is validated strictly against it — all required fields must be present and no extra fields are included.

Output is JSON only. No prose, no markdown, no explanation.

## Output structure

```json
{
  "transformed": {
    "customer": {
      "email": "user@example.com",
      "name": "Jane Smith"
    },
    "amount": 4999,
    "currency": "usd",
    "created_at": "2024-01-15T10:30:00Z"
  },
  "metadata": {
    "source_format": "stripe",
    "target_format": "hubspot",
    "fields_mapped": 8,
    "fields_dropped": 3,
    "warnings": ["billing_address had no target mapping"]
  }
}
```

## Data normalizations applied automatically

| Type | Normalization |
|---|---|
| Timestamps | ISO 8601 UTC regardless of source format |
| Currency | Minor units (cents as integers) or major units (floats) depending on target |
| Phone numbers | E.164 format (`+1XXXXXXXXXX`) |
| Booleans | Normalized from truthy/falsy (`1/0`, `"yes"/"no"`, `"true"/"false"`) to proper booleans |
| IDs | Preserved as strings to prevent integer overflow |

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `source_payload` | object | yes | — | The incoming webhook payload |
| `source_format` | string | yes | — | Source service identifier (e.g. `stripe`, `github`, `shopify`) |
| `target_format` | string | yes | — | Target service identifier |
| `mapping_rules` | array | no | — | Explicit rules: objects with `source_field`, `target_field`, and optional `transform` description |
| `target_schema` | object | no | — | JSON schema for the output — overrides format inference when provided |
| `drop_unmapped` | boolean | no | `true` | Silently drop fields with no target mapping (false collects them under `_unmapped`) |
| `null_handling` | string | no | `"omit"` | How to handle nulls: `omit`, `preserve` as null, or replace with type `default` |

## Use cases

- Stripe payment events → internal order management schema
- GitHub webhooks → Slack message payloads
- Shopify order events → CRM contact and deal records
- PagerDuty alerts → internal incident tracking format
- Any service-to-service integration where schemas diverge
