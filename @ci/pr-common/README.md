# @ci/pr-common

**Base PR Reviewer Templates for Automated Code Review**

A [Prompd](https://prompd.ai) package providing a reusable base template for automated pull request reviews. Use this as a foundation to build platform-specific PR reviewers for GitHub, GitLab, Bitbucket, or custom CI/CD systems.

## Overview

This package contains a structured prompt template that analyzes pull request diffs and returns comprehensive, actionable code review feedback in JSON format. It focuses on security, correctness, performance, maintainability, and test coverage.

## Features

- 🔍 **Multi-dimensional Analysis** — Security, correctness, performance, maintainability, tests
- 🎯 **Structured Output** — Returns valid JSON with standardized finding format
- ⚙️ **Configurable Focus** — Target specific review areas based on your needs
- 📊 **Severity Categorization** — CRITICAL, HIGH, MEDIUM, LOW, and PRAISE levels
- 🧪 **Test Coverage Assessment** — Evaluates test adequacy and suggests missing cases
- 🔒 **Security Risk Analysis** — Identifies vulnerabilities and risk levels
- 🏗️ **Inheritance-Ready** — Extend for platform-specific implementations

## Installation

```bash
prompd install @ci/pr-common
```

## Usage

### Basic Usage

```typescript
import { executePrompt } from 'prompd';

const review = await executePrompt('@ci/pr-common/prompts/base-pr-reviewer.prmd', {
  title: "Add user authentication",
  description: "Implements JWT-based authentication with refresh tokens",
  diff: `diff --git a/src/auth.ts b/src/auth.ts
new file mode 100644
index 0000000..1234567
--- /dev/null
+++ b/src/auth.ts
@@ -0,0 +1,42 @@
+export async function login(username: string, password: string) {
+  // implementation
+}`,
  base_branch: "main"
});

console.log(review);
```

### Inheriting for Platform-Specific Reviewers

Create `github-pr-reviewer.prmd`:

```yaml
---
id: github-pr-reviewer
name: "GitHub PR Reviewer"
version: 1.0.0
inherits: "@ci/pr-common@0.0.1/prompts/base-pr-reviewer.prmd"
parameters:
  - name: pr_number
    type: integer
    required: true
  - name: repository
    type: string
    required: true
---

# Additional GitHub-specific context or overrides
```

## Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `diff` | string | ✅ | - | Unified diff of the pull request |
| `title` | string | ✅ | - | Pull request title |
| `description` | string | ❌ | `""` | Pull request body/description |
| `base_branch` | string | ❌ | `"main"` | Target branch being merged into |
| `language` | string | ❌ | `"auto"` | Primary programming language |
| `review_focus` | array | ❌ | `["security", "correctness", "performance", "maintainability", "tests"]` | Areas to focus on |
| `max_findings` | integer | ❌ | `20` | Maximum number of findings to return |

## Output Format

The prompt returns a JSON object with this structure:

```json
{
  "summary": {
    "verdict": "APPROVE | REQUEST_CHANGES | COMMENT",
    "confidence": 0.95,
    "overview": "This PR implements JWT authentication with proper token handling and refresh logic.",
    "stats": {
      "files_changed": 3,
      "lines_added": 156,
      "lines_removed": 12,
      "critical_count": 0,
      "high_count": 1,
      "medium_count": 3,
      "low_count": 2,
      "praise_count": 2
    }
  },
  "findings": [
    {
      "id": "sec-001",
      "severity": "HIGH",
      "category": "security",
      "file": "src/auth.ts",
      "line": 23,
      "title": "Weak password hash configuration",
      "detail": "bcrypt rounds set to 8, which is below current OWASP recommendation of 12+",
      "suggestion": "Increase bcrypt rounds to 12: bcrypt.hash(password, 12)",
      "blocking": true
    }
  ],
  "test_coverage": {
    "has_tests": true,
    "tests_adequate": false,
    "missing_cases": [
      "Token expiration edge cases",
      "Concurrent refresh token usage"
    ]
  },
  "security": {
    "risk_level": "MEDIUM",
    "vulnerabilities": ["Weak cryptographic configuration"]
  }
}
```

## Review Categories

- **security** — Authentication, authorization, injection, cryptography, secrets
- **correctness** — Logic errors, edge cases, null handling, type safety
- **performance** — Inefficient algorithms, memory leaks, unnecessary computations
- **maintainability** — Code clarity, documentation, naming, modularity
- **tests** — Coverage, edge cases, test quality, integration tests
- **style** — Formatting, conventions (low priority)

## Severity Levels

| Severity | When to Use | Blocking |
|----------|-------------|----------|
| **CRITICAL** | Security vulnerabilities, data loss risks, production blockers | ✅ |
| **HIGH** | Major bugs, significant performance issues, broken functionality | ✅ |
| **MEDIUM** | Correctness issues, maintainability concerns, incomplete tests | ⚠️ |
| **LOW** | Style issues, minor optimizations, suggestions | ❌ |
| **PRAISE** | Excellent patterns, clever solutions, good practices | ❌ |

## Example Use Cases

### GitHub Actions Workflow

```yaml
name: AI Code Review
on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Get PR Diff
        id: diff
        run: |
          gh pr diff ${{ github.event.pull_request.number }} > pr.diff
      - name: Run AI Review
        run: |
          prompd exec @ci/pr-common/prompts/base-pr-reviewer.prmd \
            --param diff="$(cat pr.diff)" \
            --param title="${{ github.event.pull_request.title }}" \
            --param description="${{ github.event.pull_request.body }}"
```

### GitLab CI Pipeline

```yaml
ai_review:
  stage: review
  script:
    - git diff origin/$CI_MERGE_REQUEST_TARGET_BRANCH_NAME...HEAD > pr.diff
    - prompd exec @ci/pr-common/prompts/base-pr-reviewer.prmd
        --param diff="$(cat pr.diff)"
        --param title="$CI_MERGE_REQUEST_TITLE"
```

### Custom Review Focus

```typescript
// Security-focused review for sensitive code
const securityReview = await executePrompt('base-pr-reviewer.prmd', {
  diff: prDiff,
  title: prTitle,
  review_focus: ["security", "correctness"],
  max_findings: 50 // More findings for security reviews
});

// Performance-focused review for optimization PRs
const perfReview = await executePrompt('base-pr-reviewer.prmd', {
  diff: prDiff,
  title: prTitle,
  review_focus: ["performance", "correctness"]
});
```

## Configuration

### Temperature and Token Limits

The base template uses:
- **Temperature:** `0.1` (low randomness for consistent reviews)
- **Max Tokens:** `4096` (adjust based on your model)

Override these when inheriting:

```yaml
---
inherits: "@ci/pr-common@0.0.1/prompts/base-pr-reviewer.prmd"
temperature: 0.0
max_tokens: 8192
---
```

## Best Practices

1. **Filter by Severity** — Only comment on HIGH+ findings in production
2. **Track Metrics** — Log verdict distribution and finding counts over time
3. **Custom Categories** — Extend for domain-specific checks (accessibility, i18n, etc.)
4. **Human Review** — Always require human approval for CRITICAL changes
5. **Incremental Adoption** — Start with COMMENT mode, graduate to REQUEST_CHANGES
6. **Language Hints** — Set `language` parameter for better context-aware reviews

## Contributing

This is a Prompd package. To contribute:

1. Fork and clone this repository
2. Make your changes to `prompts/base-pr-reviewer.prmd`
3. Test with real PR diffs
4. Submit a pull request

## License

MIT

## Related Packages

- `@ci/github-reviewer` — GitHub-specific PR review implementation
- `@ci/gitlab-reviewer` — GitLab MR review implementation
- `@prompd/code-analysis` — General code quality analysis prompts

## Support

- 📖 [Prompd Documentation](https://prompd.ai/docs)
- 💬 [Community Forum](https://community.prompd.ai)
- 🐛 [Issue Tracker](https://github.com/prompd/packages/issues)

---

**Made with [Prompd](https://prompd.ai)** — The prompt package manager for AI-powered development tools.
