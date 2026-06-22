# @prompd/bitbucket-pr-reviewer

PR review skill for Bitbucket Pipelines. Extends `@prompd/base-pr-reviewer` and maps all findings to the Bitbucket Code Insights API format — producing a `report` object for the pipeline dashboard and an `annotations` array for inline findings, ready to submit via `PUT /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}` and `POST .../annotations`.

Findings are mapped to Bitbucket's typed annotation system: security findings become `VULNERABILITY`, logic errors become `BUG`, and style or test issues become `CODE_SMELL`. The report result is set to `FAILED` whenever any critical or high finding exists.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `diff` | string | ✓ | — | Unified diff from the Bitbucket pipeline |
| `title` | string | ✓ | — | Pull request title |
| `description` | string | | `""` | Pull request description |
| `base_branch` | string | | `"main"` | Destination branch (BITBUCKET_PR_DESTINATION_BRANCH) |
| `pr_id` | integer | | — | Pull request ID (BITBUCKET_PR_ID) |
| `workspace` | string | | — | Bitbucket workspace slug |
| `repository` | string | | — | Repository slug (BITBUCKET_REPO_SLUG) |
| `author` | string | | — | PR author display name |
| `review_focus` | array | | `["security","correctness","performance","maintainability","tests"]` | Review categories to focus on |
| `max_findings` | integer | | `20` | Maximum number of findings to return |
| `language` | string | | `"auto"` | Primary programming language (auto-detect if not specified) |

## Example

Input:

```json
{
  "diff": "diff --git a/src/auth/login.ts b/src/auth/login.ts\n...",
  "language": "typescript",
  "severity_threshold": "medium",
  "pull_request_id": 23,
  "workspace": "acme",
  "repo_slug": "backend"
}
```

Output:

```json
{
  "report": {
    "title": "Prompd Code Review",
    "details": "1 critical security vulnerability, 2 code quality issues",
    "report_type": "SECURITY",
    "result": "FAILED",
    "data": [
      {"type": "BOOLEAN", "title": "Security Issues Found", "value": true},
      {"type": "NUMBER", "title": "Critical Findings", "value": 1},
      {"type": "NUMBER", "title": "Total Findings", "value": 3}
    ]
  },
  "annotations": [
    {
      "external_id": "finding-001",
      "path": "src/auth/login.ts",
      "line": 42,
      "message": "User input interpolated directly into SQL query without parameterization. Use parameterized queries to prevent injection.",
      "severity": "CRITICAL",
      "type": "VULNERABILITY",
      "link": null
    }
  ],
  "pr_comment": "Code Insights review complete. 1 CRITICAL vulnerability must be resolved before merge."
}
```

## Install

```
prompd install @prompd/bitbucket-pr-reviewer
```
