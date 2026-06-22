# @prompd/document-summarizer

Summarizes long-form documents into structured JSON output. Supports three output formats — structured (full breakdown with sections, entities, and action items), bullets (discrete key points), and narrative (cohesive prose) — with a configurable word count target and optional topic filtering.

Built as a general-purpose base that can be extended by domain-specific summarizers. Suitable for board reports, research papers, meeting transcripts, policy documents, and any long-form content requiring automated digestion.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `document` | string | yes | — | The full document text to summarize |
| `output_format` | string | no | `"structured"` | Output format: `bullets`, `narrative`, or `structured` |
| `max_length` | number | no | `500` | Target maximum word count across all summary text fields |
| `focus_topics` | array | no | `[]` | Topics to prioritize. Empty array means summarize all content. |

## Example

Input:
```json
{
  "document": "Q3 2024 Board Report\n\nFinancial Performance\nRevenue grew 23% year-over-year to $4.2M...\n[full document text]",
  "output_format": "structured",
  "max_length": 400,
  "focus_topics": []
}
```

Output (structured format):
```json
{
  "title": "Q3 2024 Board Report",
  "executive_summary": "Revenue grew 23% YoY to $4.2M driven by enterprise expansion. Headcount reached 142 with three key hires in engineering.",
  "key_points": [
    "Revenue up 23% YoY",
    "Headcount at 142",
    "Enterprise segment now 61% of ARR"
  ],
  "sections": [
    {"heading": "Financial Performance", "summary": "Q3 revenue of $4.2M represents 23% growth year-over-year, led by a 41% increase in enterprise contract value."}
  ],
  "entities": {
    "people": ["Jane Smith", "Carlos Rivera"],
    "organizations": ["Acme Corp", "Beta LLC"],
    "dates": ["2024-09-30", "2024-10-15"]
  },
  "action_items": [
    "Board to approve Q4 hiring plan by October 31",
    "CFO to present revised projections at November meeting"
  ]
}
```

Output (bullets format):
```json
{
  "title": "Q3 2024 Board Report",
  "bullets": [
    "Revenue grew 23% year-over-year to $4.2M in Q3 2024.",
    "Enterprise contracts now represent 61% of ARR.",
    "Headcount increased to 142 with three engineering hires.",
    "Board approval required for Q4 hiring plan by October 31."
  ]
}
```

Output (narrative format):
```json
{
  "title": "Q3 2024 Board Report",
  "summary": "The Q3 2024 board report details strong financial performance with revenue reaching $4.2M, a 23% year-over-year increase driven primarily by enterprise contract growth. The company added three senior engineering hires, bringing total headcount to 142. The board is asked to approve the Q4 hiring plan before the end of October."
}
```

## Install

```
prompd install @prompd/document-summarizer
```
