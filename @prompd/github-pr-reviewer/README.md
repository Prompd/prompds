# @prompd/github-pr-reviewer

🔍 **GitHub-native PR reviewer** for CI/CD pipelines. Extends `@prompd/base-pr-reviewer` with GitHub Reviews API and Checks API integration.

## ✨ Features

- 🎯 **GitHub Actions ready** — Drop-in integration with GitHub workflows
- 🔄 **Dual output format** — Review comments + Check run annotations  
- 🛡️ **Security-first** — Prioritizes vulnerabilities and attack vectors
- 📊 **Severity mapping** — Critical/High → failure, Medium → warning, Low → notice
- 🎨 **Language-aware** — Tailored rules for different programming languages
- ⚡ **Configurable focus** — Target specific review categories

## 🚀 Quick Start

### Install

```bash
prompd install @prompd/github-pr-reviewer
```

### Basic Usage

```javascript
import { prompd } from '@prompd/core';

const review = await prompd.run('@prompd/github-pr-reviewer', {
  diff: process.env.PR_DIFF,
  pr_number: parseInt(process.env.PR_NUMBER),
  repository: process.env.GITHUB_REPOSITORY,
  title: process.env.PR_TITLE,
  author: process.env.PR_AUTHOR
});

// Submit to GitHub
await github.rest.pulls.createReview({
  ...context.repo,
  pull_number: review.pr_number,
  ...review.review
});
```

## 🔧 GitHub Actions Integration

```yaml
name: Code Review
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      
      - name: Get PR diff
        id: diff
        run: |
          git diff origin/${{ github.base_ref }}..HEAD > pr.diff
          echo "diff<<EOF" >> $GITHUB_OUTPUT
          cat pr.diff >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT
      
      - name: AI Code Review
        uses: prompd/github-action@v1
        with:
          prompt: '@prompd/github-pr-reviewer'
          inputs: |
            {
              "diff": "${{ steps.diff.outputs.diff }}",
              "pr_number": ${{ github.event.pull_request.number }},
              "repository": "${{ github.repository }}",
              "title": "${{ github.event.pull_request.title }}",
              "author": "${{ github.event.pull_request.user.login }}",
              "review_focus": ["security", "performance", "correctness"]
            }
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## 📖 Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `diff` | string | ✅ | — | Unified diff output (git diff format) |
| `pr_number` | integer | ✅ | — | GitHub pull request number |
| `repository` | string | ✅ | — | Repository in `owner/repo` format |
| `title` | string | ✅ | — | Pull request title |
| `author` | string | ⚫ | — | PR author username |
| `description` | string | ⚫ | `""` | Pull request body/description |
| `base_branch` | string | ⚫ | `"main"` | Target branch name |
| `language` | string | ⚫ | `"auto"` | Primary programming language |
| `review_focus` | array | ⚫ | `["all"]` | Categories: `security`, `correctness`, `performance`, `maintainability`, `tests` |
| `max_findings` | integer | ⚫ | `20` | Maximum findings to report |

## 🎯 API Reference

### Output Format

```typescript
interface ReviewResult {
  // GitHub Reviews API format
  review: {
    commit_id: string;
    body: string;
    event: "APPROVE" | "REQUEST_CHANGES" | "COMMENT";
    comments: Array<{
      path: string;
      line: number;
      side: "RIGHT";
      body: string; // Markdown with severity badges
    }>;
  };
  
  // GitHub Checks API format  
  check_run: {
    conclusion: "success" | "failure" | "neutral";
    output: {
      title: string;
      summary: string;
      annotations: Array<{
        path: string;
        start_line: number;
        end_line: number;
        annotation_level: "failure" | "warning" | "notice";
        message: string;
        title: string;
      }>;
    };
  };
  
  // Review statistics
  stats: {
    critical: number;
    high: number; 
    medium: number;
    low: number;
    praise: number;
    verdict: "APPROVE" | "REQUEST_CHANGES" | "COMMENT";
  };
}
```

### Severity Mapping

| Severity | GitHub Event | Check Conclusion | Annotation Level | Badge |
|----------|--------------|------------------|------------------|-------|
| **CRITICAL** | `REQUEST_CHANGES` | `failure` | `failure` | 🔴 |
| **HIGH** | `REQUEST_CHANGES` | `failure` | `failure` | 🟠 |
| **MEDIUM** | `COMMENT` | `neutral` | `warning` | 🟡 |
| **LOW** | `COMMENT` | `success` | `notice` | 🔵 |
| **PRAISE** | `APPROVE` | `success` | `notice` | ✅ |

## ⚙️ Advanced Configuration

### Language-Specific Rules

```json
{
  "language": "typescript",
  "review_focus": ["security", "performance"],
  "custom_rules": {
    "typescript": {
      "enforce_strict_null_checks": true,
      "prefer_readonly_arrays": true,
      "no_any_types": "warning"
    }
  }
}
```

### Custom Context

```json
{
  "context": "This PR implements the user authentication system discussed in issue #123. Focus on security vulnerabilities and session management.",
  "linked_issues": ["#123", "#124"],
  "deployment_target": "production"
}
```

## 🐛 Troubleshooting

### Common Issues

**Large diffs timing out:**
```json
{
  "max_findings": 10,
  "review_focus": ["security", "critical-bugs"]
}
```

**Too many false positives:**
```json
{
  "severity_threshold": "medium",
  "confidence_threshold": 0.8
}
```

**Missing context:**
```json
{
  "description": "Detailed PR description with context",
  "context": "Additional context about the changes"
}
```

### Debug Mode

Set `PROMPD_DEBUG=true` to see detailed analysis steps and reasoning.

## 🤝 Contributing

Found a bug or want to improve the reviewer? 

1. **Issues** — Report bugs or request features
2. **Pull Requests** — Submit improvements
3. **Discussions** — Share feedback and ideas

## 📄 License

Licensed under ELv2 (Elastic License v2). See [LICENSE](LICENSE) for details.

## 🔗 Related Packages

- [`@prompd/base-pr-reviewer`](https://github.com/prompd/packages/tree/main/packages/base-pr-reviewer) — Base review logic
- [`@prompd/security-scanner`](https://github.com/prompd/packages/tree/main/packages/security-scanner) — Security-focused analysis
- [`@prompd/test-reviewer`](https://github.com/prompd/packages/tree/main/packages/test-reviewer) — Test quality assessment
