# @prompd/release-notes-generator

Transforms a list of git commit objects into structured, human-readable release notes. Understands conventional commit format, automatically classifies commits that do not follow the convention, identifies breaking changes, and supports three output formats: Markdown, JSON, and HTML.

## How it works

You pass in the commits for a release — each with a SHA, message, author, and date — along with the version string. The generator classifies each commit into a category, strips type prefixes from displayed messages, omits merge and bot commits, and assembles the output in your chosen format.

Breaking changes are detected from BREAKING CHANGE footer tokens, the `!` suffix on commit types, and language patterns in the message body. When breaking changes are present, they appear as a dedicated top-level section and the output includes specific upgrade notes derived from the commit messages.

## Output formats

- `markdown` — returns a JSON object with a `"content"` key containing the full Markdown string
- `json` — returns a structured JSON object with categorized commits, a summary sentence, and upgrade notes
- `html` — returns a JSON object with a `"content"` key containing the HTML string

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `commits` | array | yes | — | Array of commit objects. Each must have: `sha` (string), `message` (string), `author` (string), `date` (string) |
| `version` | string | yes | — | Release version string (e.g. `"1.4.2"`) |
| `output_format` | string | no | `"markdown"` | Output format: `markdown`, `json`, or `html` |
| `categorize_by` | string | no | `"type"` | Grouping strategy: `type` (conventional commit type), `scope` (commit scope token), or `impact` (user-facing vs internal) |
| `include_breaking` | boolean | no | `true` | Surface breaking changes as a prominent top-level section with upgrade instructions |

## Example

Input:

```json
{
  "commits": [
    {"sha": "a3f2b1c", "message": "feat!: remove deprecated /v1/users endpoint", "author": "jsmith", "date": "2024-11-15"},
    {"sha": "b4c3d2e", "message": "feat(webhooks): add retry with exponential backoff", "author": "mmartinez", "date": "2024-11-14"},
    {"sha": "c5d4e3f", "message": "fix(session): resolve race condition in session handler", "author": "kwong", "date": "2024-11-13"}
  ],
  "version": "1.4.2",
  "output_format": "json",
  "categorize_by": "type",
  "include_breaking": true
}
```

Output:

```json
{
  "version": "1.4.2",
  "date": "2024-11-15",
  "categories": [
    {
      "name": "Breaking Changes",
      "commits": [
        {"sha": "a3f2b1c", "message": "remove deprecated /v1/users endpoint", "author": "jsmith"}
      ]
    },
    {
      "name": "New Features",
      "commits": [
        {"sha": "b4c3d2e", "message": "(webhooks) add retry with exponential backoff", "author": "mmartinez"}
      ]
    },
    {
      "name": "Bug Fixes",
      "commits": [
        {"sha": "c5d4e3f", "message": "(session) resolve race condition in session handler", "author": "kwong"}
      ]
    }
  ],
  "summary": "This release includes 1 breaking change, 1 new feature, and 1 bug fix.",
  "upgrade_notes": "The /v1/users endpoint has been removed. Migrate all calls to /v2/users before upgrading. No other changes to request or response shapes are required."
}
```

## Install

```
prompd install @prompd/release-notes-generator
```
