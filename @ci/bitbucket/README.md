# @ci/bitbucket

PR review skill for Bitbucket Pipelines. Extends `@prompd/base-pr-reviewer` and maps all findings to the Bitbucket Code Insights API format — producing a `report` object for the pipeline dashboard and an `annotations` array for inline findings, ready to submit via `PUT /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}` and `POST .../annotations`.

Findings are mapped to Bitbucket's typed annotation system: security findings become `VULNERABILITY`, logic errors become `BUG`, and style or test issues become `CODE_SMELL`. The report result is set to `FAILED` whenever any critical or high finding exists.

## Parameters

All parameters from `@prompd/base-pr-reviewer` are inherited and available. The following parameters are added by this package:

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `diff` | string | yes | — | Unified diff output of the pull request (git diff format) |
| `language` | string | no | `"auto"` | Primary programming language for language-specific rules |
| `review_focus` | array | no | `["all"]` | Categories to focus on: `security`, `style`, `logic`, `tests`, `all` |
| `severity_threshold` | string | no | `"low"` | Minimum severity to include: `low`, `medium`, `high`, `critical` |
| `context` | string | no | — | Additional PR context (title, description, linked issue) |
| `pull_request_id` | number | yes | — | Bitbucket pull request ID |
| `workspace` | string | yes | — | Bitbucket workspace slug |
| `repo_slug` | string | yes | — | Bitbucket repository slug |

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
prompd install @ci/bitbucket
```
