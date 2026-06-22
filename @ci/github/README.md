# @ci/github

PR review skill for GitHub Actions pipelines. Extends `@prompd/base-pr-reviewer` and maps all findings to the GitHub Reviews API and GitHub Checks API formats — producing a `review` object ready to submit via `POST /repos/{owner}/{repo}/pulls/{pull_number}/reviews` and a `check_run` object for `POST /repos/{owner}/{repo}/check-runs`.

Each finding becomes both an inline review comment and a check run annotation. Severity levels map to GitHub annotation levels: critical and high produce `failure` annotations, medium produces `warning`, and low produces `notice`. The overall verdict maps to a GitHub review event (`APPROVE`, `REQUEST_CHANGES`, or `COMMENT`) and a check run conclusion (`success`, `action_required`, or `neutral`).

## Parameters

All parameters from `@prompd/base-pr-reviewer` are inherited and available. The following parameters are added by this package:

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `diff` | string | yes | — | Unified diff output of the pull request (git diff format) |
| `language` | string | no | `"auto"` | Primary programming language for language-specific rules |
| `review_focus` | array | no | `["all"]` | Categories to focus on: `security`, `style`, `logic`, `tests`, `all` |
| `severity_threshold` | string | no | `"low"` | Minimum severity to include: `low`, `medium`, `high`, `critical` |
| `context` | string | no | — | Additional PR context (title, description, linked issue) |
| `pr_number` | number | yes | — | GitHub pull request number |
| `repo` | string | yes | — | Repository in `owner/repo` format (e.g. `acme/backend`) |
| `commit_sha` | string | yes | — | HEAD commit SHA of the PR being reviewed |

## Example

Input:

```json
{
  "diff": "diff --git a/src/auth/login.ts b/src/auth/login.ts\n...",
  "language": "typescript",
  "severity_threshold": "medium",
  "pr_number": 142,
  "repo": "acme/backend",
  "commit_sha": "a3f2b1c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3"
}
```

Output:

```json
{
  "review": {
    "commit_id": "a3f2b1c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3",
    "body": "Code review completed. 1 critical issue requires resolution before merge.",
    "event": "REQUEST_CHANGES",
    "comments": [
      {
        "path": "src/auth/login.ts",
        "line": 42,
        "body": "**[CRITICAL] Security: SQL Injection**\n\nUser input is interpolated directly into the SQL query string without parameterization. An attacker can manipulate the query to bypass authentication or exfiltrate data.\n\n**Suggestion:** Use parameterized queries: `db.query('SELECT * FROM users WHERE id = $1', [userId])`"
      }
    ]
  },
  "check_run": {
    "name": "prompd/code-review",
    "head_sha": "a3f2b1c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3",
    "status": "completed",
    "conclusion": "action_required",
    "output": {
      "title": "1 critical finding",
      "summary": "Review complete. 1 critical security vulnerability must be resolved before merge.",
      "annotations": [
        {
          "path": "src/auth/login.ts",
          "start_line": 42,
          "end_line": 42,
          "annotation_level": "failure",
          "message": "User input interpolated directly into SQL query without parameterization.",
          "title": "SQL Injection vulnerability"
        }
      ]
    }
  }
}
```

## Install

```
prompd install @ci/github
```
