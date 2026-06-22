# @guardrails/brand-voice

Evaluates LLM-generated content against brand guidelines, checking for tone mismatches, forbidden phrases, competitor mentions, reading level compliance, and required disclaimer presence. Returns a structured JSON compliance report with specific violations and actionable rewrite suggestions.

This guardrail is designed for content generation pipelines where LLM output must conform to a defined brand voice before publication — marketing copy, customer communications, chatbot responses, and documentation. It accepts your brand guidelines as a runtime parameter, making it reusable across multiple brands or guideline versions without changing the prompt.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `content` | string | yes | — | The LLM-generated content to validate against brand guidelines |
| `brand_guidelines` | object | yes | — | Brand configuration with keys: `tone` (array of adjectives), `forbidden_phrases` (array), `required_reading_level` (`elementary`, `middle`, `high`, or `professional`) |
| `prohibited_competitors` | array | no | `[]` | Competitor names or brands that must not be mentioned |
| `required_disclaimers` | array | no | `[]` | Disclaimer phrases or patterns that must appear in the content |

## Example

**Input**

```json
{
  "content": "Our platform is super easy to use! Unlike Acme Corp, we don't make you jump through hoops. Get started in minutes and watch your team crush it.",
  "brand_guidelines": {
    "tone": ["professional", "confident", "precise"],
    "forbidden_phrases": ["crush it", "jump through hoops"],
    "required_reading_level": "professional"
  },
  "prohibited_competitors": ["Acme Corp", "Acme"],
  "required_disclaimers": ["Results may vary."]
}
```

**Output**

```json
{
  "compliant": false,
  "violations": [
    {
      "type": "tone_mismatch",
      "detail": "Phrase 'super easy to use' uses informal register inconsistent with 'professional' tone requirement",
      "excerpt": "super easy to use"
    },
    {
      "type": "competitor_mention",
      "detail": "Prohibited competitor 'Acme Corp' is directly named in a comparative context",
      "excerpt": "Unlike Acme Corp"
    },
    {
      "type": "forbidden_phrase",
      "detail": "Phrase 'jump through hoops' is on the forbidden phrases list",
      "excerpt": "jump through hoops"
    },
    {
      "type": "forbidden_phrase",
      "detail": "Phrase 'crush it' is on the forbidden phrases list",
      "excerpt": "crush it"
    }
  ],
  "suggestions": [
    "Replace 'super easy to use' with 'straightforward to implement' or 'designed for immediate productivity'",
    "Remove competitor reference entirely or replace with 'other solutions' without naming them",
    "Replace 'jump through hoops' with 'navigate unnecessary complexity'",
    "Replace 'crush it' with 'accelerate results' or 'drive meaningful outcomes'"
  ],
  "disclaimer_check": {
    "required": 1,
    "found": 0,
    "missing": ["Results may vary."]
  }
}
```

## Install

```
prompd install @guardrails/brand-voice
```
