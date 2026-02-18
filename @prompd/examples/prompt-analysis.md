# System Prompt Analysis — Tool Execution Improvements

## Current System Prompt Analysis

### Strengths

1. **Clear XML structure** — The response format is well-defined and unambiguous.
2. **Plan Mode workflow** — The read-first-then-batch-writes pattern is efficient and gives you control over approvals.
3. **edit_file preference** — Prioritizing targeted search/replace over full file rewrites minimizes risk of data loss.
4. **Task decomposition** — The multi-file batching strategy (discover → report → batch → iterate) is solid.
5. **Strong guardrails** — Path security, command allowlists, and CDATA handling are well thought out.

### Areas for Improvement

#### 1. Ambiguity in "batch size" heuristics

The prompt says "Read 5-10 affected files at a time" but doesn't define when to pick 5 vs 10. A clearer heuristic:

- **≤5 files total**: Read all at once
- **6-15 files**: Batch in groups of 5
- **16+ files**: Batch in groups of 10

#### 2. No rollback / undo guidance

If an `edit_file` succeeds but produces incorrect output, there's no instruction to revert. A recommended pattern:

> "If a write produces an unintended result, read the file, identify the issue, and issue a corrective `edit_file`."

#### 3. `present_plan` is underutilized

The prompt describes `present_plan` but the workflow mostly batches writes directly. A clearer trigger:

> "Use `present_plan` when the task affects 3+ files or involves destructive operations (delete, overwrite, rename)."

#### 4. Error handling is vague

"If a tool fails, explain the error and try an alternative approach" — but there's no structured retry strategy. Recommended policy:

> Retry once with adjusted parameters, then use `ask_user` to get guidance from the user.

#### 5. No priority ordering for batched writes

When batching multiple writes, there's no guidance on ordering. For example, creating a new file should happen *before* editing another file that imports from it. Adding dependency-aware ordering would prevent transient broken states.

#### 6. Missing guidance on `ask_user` vs. making assumptions

The prompt says "Ask When Unclear" but doesn't define a threshold. Recommended rule:

> "If there are ≤2 reasonable interpretations and one is clearly more likely, proceed with it and note your assumption. If there are 3+ equally valid interpretations, use `ask_user`."

#### 7. CDATA usage could be more precise

The rule says "for content with special characters" but doesn't specify that CDATA should be used for *all* file content in `write_file` to be safe. Making CDATA the default for `<content>` fields would prevent edge-case XML parsing failures.

#### 8. No streaming/progress feedback for long operations

For tasks touching 20+ files, the user gets silence until the full batch is ready. Adding intermediate `<message>` guidance like "Report progress after each batch completes" is already there, but could be stronger — e.g., include file counts and estimated remaining batches.

## Summary of Recommended Changes

| Priority | Change | Impact |
|----------|--------|--------|
| 🔴 High | Add dependency-aware write ordering | Prevents broken intermediate states |
| 🔴 High | Define `present_plan` trigger conditions | Better UX for complex tasks |
| 🟡 Medium | Structured retry policy for tool failures | More robust error recovery |
| 🟡 Medium | Clearer `ask_user` threshold | Fewer unnecessary questions, fewer wrong assumptions |
| 🟢 Low | Default CDATA for all file content | Eliminates XML escaping edge cases |
| 🟢 Low | Explicit batch size rules | More predictable behavior |
