# @prompd/base-pr-reviewer

Core PR review engine that analyzes unified diffs for security vulnerabilities, logic errors, style violations, and test coverage gaps. This is a base package — it is not intended for direct use in pipelines. Extend it with a platform-specific package (`@ci/github`, `@ci/gitlab`, `@ci/bitbucket`) to get output formatted for your code hosting platform's API.

## How it works

You provide a `git diff` output and configure which areas to focus on and which severity levels to surface. The reviewer analyzes every added line against a prioritized rule set — security vulnerabilities first, then logic errors, style issues, and test gaps — and returns a structured JSON object with a per-finding breakdown, an overall verdict, and a security risk assessment.

The output is consumed directly by CI automation. There is no prose — only a single parseable JSON object.

## When to use the base package directly

Use `@prompd/base-pr-reviewer` directly when you are building a custom integration and want to handle the platform mapping yourself. If you are integrating with GitHub Actions, GitLab CI, or Bitbucket Pipelines, use the corresponding platform package instead — it inherits this base and produces output already shaped for that platform's API.

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `diff` | string | yes | — | Unified diff output of the pull request (git diff format) |
| `language` | string | no | `"auto"` | Primary programming language for language-specific rules. Values: `auto`, `python`, `typescript`, `javascript`, `go`, `java`, `ruby`, `rust`, `csharp` |
| `review_focus` | array | no | `["all"]` | Categories to focus on: `security`, `style`, `logic`, `tests`, `all` |
| `severity_threshold` | string | no | `"low"` | Minimum severity to include. Values: `low`, `medium`, `high`, `critical` |
| `context` | string | no | — | Additional context (PR title, description, linked issue) to improve finding relevance |

## Example

Input:

```json
{
  "diff": "diff --git a/src/auth/login.ts b/src/auth/login.ts\n...",
  "language": "typescript",
  "review_focus": ["security", "logic"],
  "severity_threshold": "medium",
  "context": "PR #142: Add user login endpoint. Fixes #88."
}
```

Output:

```json
{
  "findings": [
    {
      "id": "finding-001",
      "file": "src/auth/login.ts",
      "line": 42,
      "severity": "critical",
      "category": "security",
      "title": "SQL injection vulnerability",
      "detail": "User input is interpolated directly into the SQL query string without parameterization. An attacker can manipulate the query to bypass authentication or exfiltrate data.",
      "suggestion": "Use parameterized queries: db.query('SELECT * FROM users WHERE id = $1', [userId])"
    }
  ],
  "summary": "1 critical security issue, 0 high, 0 medium, 0 low findings",
  "overall_rating": "changes_requested",
  "security_risk_level": "critical",
  "test_coverage_assessment": "insufficient",
  "positive_observations": []
}
```

## Install

```
prompd install @prompd/base-pr-reviewer
```
