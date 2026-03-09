# @prompd/ci-gate

Automated code quality gate for CI/CD pipelines. Analyzes git diffs against configurable rule categories and returns a structured pass/fail verdict with machine-parseable findings — including file, line number, and a concrete fix suggestion for each issue.

## How it works

You pass in a unified diff (the output of `git diff`) and configure which rule categories to enforce. The gate analyzes the added lines against those rules and returns a JSON verdict with a `pass` or `fail` decision, aggregate stats, and a detailed findings list.

The gate is intentionally conservative: it only flags issues it is confident about. False positives erode trust and waste developer time, so ambiguous cases are not reported. Each finding includes a severity level (`error`, `warning`, or `info`), and you configure the `severity_threshold` that triggers a failure — letting you run the gate in advisory mode (`info`) during rollout or in strict mode (`error`-only) for less critical checks.

Language detection is automatic by default (`auto`) but can be set explicitly for more accurate rule application.

## Output structure

```json
{
  "verdict": "fail",
  "summary": "2 security findings in auth.ts",
  "stats": {
    "files_analyzed": 1,
    "lines_added": 34,
    "lines_removed": 12,
    "findings_total": 2,
    "findings_by_severity": { "error": 1, "warning": 1, "info": 0 }
  },
  "findings": [
    {
      "id": "security-1",
      "severity": "error",
      "rule": "security",
      "file": "src/auth.ts",
      "line": 42,
      "title": "Hardcoded API key",
      "detail": "Line 42 assigns a literal string to `apiKey`. This value will be committed to version control.",
      "suggestion": "Move to an environment variable and access via process.env.API_KEY"
    }
  ]
}
```

## Available rules

| Rule | What it checks |
|---|---|
| `security` | Hardcoded secrets, SQL injection vectors, path traversal, unsafe deserialization, missing input validation, weak cryptography |
| `error-handling` | Silent catch blocks, unhandled I/O errors, error messages leaking internals, unchecked return values |
| `naming` | Generic variable names (`data`, `result`, `tmp`), boolean variables missing `is/has/should`, vague function names, inconsistent conventions |
| `complexity` | Functions over ~30 lines, nesting depth > 3, more than 5 parameters, cyclomatic complexity concerns |
| `documentation` | Public functions without docstrings, complex logic without comments, updated signatures with stale docs |
| `testing` | New public functions without test additions, weakened assertions, conditional logic without branch coverage |
| `logging` | Sensitive data in log statements, missing error-path logging, inconsistent log levels |
| `performance` | Queries inside loops, missing pagination, unbounded collection operations, sync I/O where async is available |

## Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `diff` | string | yes | — | Git diff in unified diff format |
| `rules` | array | no | `["security", "error-handling", "naming", "complexity"]` | Rule categories to enforce |
| `severity_threshold` | string | no | `"warning"` | Minimum severity to fail: `"error"`, `"warning"`, or `"info"` |
| `language` | string | no | `"auto"` | Language for context-aware analysis, or `"auto"` to detect |
| `context_files` | string | no | — | Additional source for broader context (signatures, types) |
| `max_findings` | integer | no | `50` | Cap on findings returned; prioritizes higher severity (1–200) |

## Use cases

## GitHub Actions Example

To use this prompt in a GitHub Action, you can create a workflow file like the following:

```yaml
name: CI Gate

on:
  pull_request:
    branches:
      - main

jobs:
  ci-gate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      
      - name: Install dependencies
        run: npm install

      - name: Run CI Gate
        run: |
          git diff HEAD^1 > diff.txt
          npx prompd run prompts/my-prompt.prmd --diff $(cat diff.txt)

## Use cases

- Pre-merge quality gate in GitHub Actions or GitLab CI
- Security scanning on pull request diffs
- Enforcing coding standards without a full linter setup
- Advisory code review on legacy codebases during migration
