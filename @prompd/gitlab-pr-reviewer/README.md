# @prompd/gitlab-pr-reviewer

MR review skill for GitLab CI pipelines. Extends `@prompd/base-pr-reviewer` and maps all findings to the GitLab Discussions API format — producing inline discussion threads, an approval state action, and label automation instructions ready to apply via the GitLab REST API.

Each finding becomes a discussion entry with a `position` object targeting the specific file and line. Approval state is set to `unapprove` whenever any critical or high finding exists; `approve` is only produced when the diff is fully clean. Label automation removes `approved` and adds `needs-security-review` when warranted.

## Parameters

All parameters from `@prompd/base-pr-reviewer` are inherited and available. The following parameters are added by this package:

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `diff` | string | yes | — | Unified diff output of the merge request (git diff format) |
| `language` | string | no | `"auto"` | Primary programming language for language-specific rules |
| `review_focus` | array | no | `["all"]` | Categories to focus on: `security`, `style`, `logic`, `tests`, `all` |
| `severity_threshold` | string | no | `"low"` | Minimum severity to include: `low`, `medium`, `high`, `critical` |
| `context` | string | no | — | Additional MR context (title, description, linked issue) |
| `merge_request_iid` | number | yes | — | GitLab merge request internal ID (iid) |
| `project_id` | number | yes | — | GitLab project ID |

## Example

Input:

```json
{
  "diff": "diff --git a/src/auth/login.py b/src/auth/login.py\n...",
  "language": "python",
  "severity_threshold": "medium",
  "merge_request_iid": 87,
  "project_id": 12345
}
```

Output:

```json
{
  "approval_action": "unapprove",
  "discussions": [
    {
      "body": "**[CRITICAL] Security: SQL Injection**\n\nUser input is concatenated directly into the SQL query string. An attacker can manipulate the query to bypass authentication or exfiltrate data.\n\n**Suggestion:** Use parameterized queries.\n\n```suggestion\nresult = db.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n```",
      "position": {
        "base_sha": "",
        "head_sha": "",
        "start_sha": "",
        "new_path": "src/auth/login.py",
        "new_line": 42,
        "position_type": "text"
      }
    }
  ],
  "labels_to_add": ["needs-security-review"],
  "labels_to_remove": ["approved"],
  "mr_note": "Review complete. 1 critical security finding blocks merge. See inline comments."
}
```

## Install

```
prompd install @prompd/gitlab-pr-reviewer
```
