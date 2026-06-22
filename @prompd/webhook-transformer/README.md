# @prompd/webhook-transformer

Transforms arbitrary webhook payloads to a caller-defined target schema using natural language mapping rules. Handles type coercion, unit conversion, field renaming, and nested object reconstruction — returning only the transformed JSON object with no wrapping or metadata.

Designed for integration pipelines that receive webhooks from third-party services with inconsistent or inconvenient schemas. Mapping rules are expressed in plain language, making it practical to configure transformations without writing code.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `payload` | object | yes | — | The raw webhook payload JSON object to transform |
| `source_format` | string | no | — | Human-readable description of the payload source (e.g. `"Stripe payment.succeeded event"`) |
| `target_schema` | object | yes | — | JSON Schema object defining the expected output structure |
| `mapping_rules` | string | no | — | Natural language field mapping instructions |

## Example

Input:
```json
{
  "payload": {
    "id": "evt_1234",
    "type": "payment.succeeded",
    "data": {
      "object": {
        "amount": 4999,
        "currency": "usd",
        "customer": {
          "email": "jane@example.com",
          "id": "cus_abc123"
        },
        "created": 1700000000
      }
    }
  },
  "source_format": "Stripe payment.succeeded event",
  "target_schema": {
    "type": "object",
    "properties": {
      "event_id": {"type": "string"},
      "user_email": {"type": "string"},
      "customer_id": {"type": "string"},
      "amount_usd": {"type": "number"},
      "occurred_at": {"type": "string", "format": "date-time"}
    },
    "required": ["event_id", "user_email", "customer_id", "amount_usd", "occurred_at"]
  },
  "mapping_rules": "map id to event_id, map data.object.customer.email to user_email, map data.object.customer.id to customer_id, convert data.object.amount from cents to dollars and map to amount_usd, convert data.object.created from Unix timestamp to ISO 8601 and map to occurred_at"
}
```

Output:
```json
{
  "event_id": "evt_1234",
  "user_email": "jane@example.com",
  "customer_id": "cus_abc123",
  "amount_usd": 49.99,
  "occurred_at": "2023-11-14T22:13:20Z"
}
```

## Install

```
prompd install @prompd/webhook-transformer
```
