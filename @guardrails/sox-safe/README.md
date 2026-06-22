# @guardrails/sox-safe

Detects material non-public information (MNPI) risk, insider trading indicators, and Sarbanes-Oxley compliance issues in LLM-generated text. Returns a structured risk assessment with flagged excerpts, risk level, recommended action, and applicable SOX sections.

This guardrail targets financial services, publicly traded companies, and any pipeline where LLM outputs could inadvertently surface unannounced earnings data, pending M&A activity, undisclosed regulatory outcomes, or other information that would constitute MNPI under SEC standards. It operates as a pre-disclosure screening layer — run it before LLM output is transmitted externally, stored in shared systems, or shown to users who might trade on the information.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `output` | string | yes | — | The LLM-generated text to analyze for MNPI risk |
| `context` | string | no | — | Additional context about the data sources or conversation that produced this output |
| `company_ticker` | string | no | — | Publicly traded company ticker symbol if content relates to a specific company |

## Example

**Input**

```json
{
  "output": "Based on the internal forecast model, Q3 earnings will exceed analyst consensus by 40%. Additionally, the merger with TechCorp is expected to close next week pending final board approval.",
  "context": "Generated from internal financial planning system query",
  "company_ticker": "ACME"
}
```

**Output**

```json
{
  "mnpi_risk": true,
  "risk_level": "critical",
  "flagged_content": [
    {
      "excerpt": "Q3 earnings will exceed analyst consensus by 40%",
      "risk_type": "material_financial",
      "explanation": "Unannounced material earnings information sourced from internal forecast model constitutes MNPI; disclosure before public announcement violates Regulation FD"
    },
    {
      "excerpt": "merger with TechCorp is expected to close next week pending final board approval",
      "risk_type": "merger_acquisition",
      "explanation": "Non-public M&A information at a definitive stage; trading on this information constitutes insider trading under SEC Rule 10b-5"
    }
  ],
  "recommended_action": "block",
  "sox_sections_implicated": ["Section 302", "Section 906"]
}
```

## Install

```
prompd install @guardrails/sox-safe
```
