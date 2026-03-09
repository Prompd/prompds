# @prompd/incident-triage

Automated incident classification, severity assessment, and routing for ops/SRE pipelines. Ingests alert payloads with optional log context, matches runbooks, routes to service owners, and evaluates escalation rules — returning a structured triage decision ready for your incident management system.

## How it works

You pass in the raw alert object from your monitoring system (PagerDuty, OpsGenie, Datadog, or any system that emits JSON). The triage engine identifies the affected service, assesses blast radius, determines customer impact, assigns a severity level, and produces a full triage object.

When you provide supporting context — recent log lines, a runbook index, service ownership maps, or escalation rules — the engine incorporates all of it into the decision. Runbooks are matched by symptoms. Owners are resolved from the service map. Escalation rules are evaluated as conditional logic.

The engine is calibrated for conservative severity: over-triaging wastes on-call time and causes alert fatigue, but under-triaging causes customer impact. When genuinely uncertain, it biases one level higher than its best estimate and sets a lower `confidence` score.

## Severity levels

| Severity | Meaning |
|---|---|
| `critical` | Customer-facing service down or severely degraded, data loss occurring or imminent, active security breach. Immediate human response required. |
| `high` | Service degradation affecting a subset of customers, SLOs breached, significantly elevated error rates. Response within 15 minutes. |
| `medium` | Elevated error rates within tolerance, capacity approaching limits, non-critical degradation. Response within 1 hour. |
| `low` | Informational alerts, preemptive warnings, non-impacting anomalies. Address next business day. |

## Output structure

```json
{
  "incident_id": "inc-7f3a2b1c",
  "timestamp": "2024-01-15T14:32:00Z",
  "severity": "high",
  "title": "Payment service error rate elevated — 12% of requests failing",
  "service": "payment-service",
  "blast_radius": "service",
  "customer_impact": "partial",
  "summary": "Error rate on the payment service spiked to 12% at 14:28 UTC. Affected requests are returning 503s from the downstream processor. No data loss detected.",
  "probable_cause": "Downstream payment processor connectivity issue based on timeout pattern in logs",
  "matched_runbooks": ["rb-payment-503"],
  "route_to": "payments-team",
  "escalate": false,
  "escalation_reason": null,
  "recommended_actions": [
    "Check payment processor status page",
    "Review circuit breaker state in payment-service dashboard"
  ],
  "after_hours": false,
  "confidence": 0.82
}
```

## After-hours behavior

When `business_hours` is `false`, the engine applies after-hours protocol automatically: only `critical` and `high` severity incidents are escalated — `medium` and `low` are queued for morning. The `after_hours` flag is set in the output for SLA tracking.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `alert_payload` | object | yes | — | Raw alert from your monitoring system |
| `log_context` | string | no | — | Recent log lines surrounding the alert timestamp (50–200 lines) |
| `runbook_index` | array | no | — | Runbook entries with `id`, `title`, `symptoms`, and `service` for matching |
| `service_owners` | object | no | — | Map of service names to team/owner identifiers |
| `escalation_rules` | array | no | `[]` | Custom rules as objects with `condition` and `action` |
| `business_hours` | boolean | no | `true` | Affects severity thresholds and routing for after-hours alerts |

## Use cases

- First-line automated triage before paging on-call
- Runbook auto-suggestion on incoming alerts
- Alert enrichment before passing to incident management tools
- After-hours alert filtering to reduce unnecessary pages
- SRE pipeline integration with PagerDuty, OpsGenie, or Datadog webhooks
