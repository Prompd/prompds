# System Prompt Analysis — Prompd Planner (Plan Mode)

## Current System Prompt Analysis

### Strengths

1. **Strict planning/execution separation** — The two-phase model (plan first, execute after approval) prevents accidental mutations and gives the user full control over what gets changed.
2. **Clear XML response format** — The required `<response>` wrapper with `<message>`, `<tool_calls>`, and `<done>` elements is unambiguous and machine-parseable.
3. **`edit_file` over `write_file` preference** — Prioritizing targeted search/replace over full file rewrites minimizes risk of data loss and makes diffs reviewable.
4. **Plan presentation via `present_plan`** — Centralizing the plan in a dedicated tool call (with CDATA) ensures the user sees a structured review modal rather than inline chat noise.
5. **Strong guardrails** — Path security (no `..` or absolute paths), command allowlists, and CDATA handling are well thought out.
6. **Three approval tiers** — Refine / Apply (review each) / Apply (trust) gives users the right level of control for their comfort level.
7. **Thorough .prmd format specification** — The frontmatter rules are explicit enough to prevent common YAML/markdown boundary errors.

### Areas for Improvement

#### 1. Ambiguity in "batch size" heuristics

The prompt references reading "5-10 affected files at a time" in the task decomposition context but doesn't define when to pick 5 vs 10. A clearer heuristic:

- **≤5 files total**: Read all at once
- **6-15 files**: Batch in groups of 5
- **16+ files**: Batch in groups of 10

#### 2. No rollback / undo guidance

If an `edit_file` succeeds but produces incorrect output, there's no instruction to revert. A recommended pattern:

> "If a write produces an unintended result, read the file, identify the issue, and issue a corrective `edit_file`."

#### 3. `present_plan` trigger conditions are implicit

The prompt says to always present a plan, but it's unclear whether trivially small tasks (e.g., fixing a typo in one file) warrant the full plan workflow or could be handled with a lighter confirmation. A clearer trigger:

> "Use `present_plan` for all tasks. For single-file, single-edit tasks, the plan can be abbreviated to a Summary and one Step."

#### 4. Error handling is vague

"If a tool fails, explain the error and try an alternative approach" — but there's no structured retry strategy. Recommended policy:

> Retry once with adjusted parameters. If it fails again, use `ask_user` to get guidance from the user.

#### 5. No priority ordering for batched writes

When batching multiple writes in execution, there's no guidance on ordering. For example, creating a new file should happen *before* editing another file that imports from it. Adding dependency-aware ordering would prevent transient broken states.

#### 6. Missing guidance on `ask_user` vs. making assumptions

The prompt says to use `ask_user` when things are ambiguous but doesn't define a threshold. Recommended rule:

> "If there are ≤2 reasonable interpretations and one is clearly more likely, proceed with it and note your assumption. If there are 3+ equally valid interpretations, use `ask_user`."

#### 7. CDATA usage could be more precise

The rule says "for content with special characters" but doesn't specify that CDATA should be used for *all* file content in `write_file` and `present_plan` to be safe. Making CDATA the default for all `<content>` fields would prevent edge-case XML parsing failures.

#### 8. No streaming/progress feedback for long operations

For tasks touching 20+ files, the user gets silence until the full plan is ready. Adding intermediate `<message>` guidance like "After reading each batch, emit a brief progress message with file counts and estimated remaining exploration" would improve UX.

#### 9. Redundant rule numbering for CDATA

Rule 5 in the "CRITICAL RULES" section says "Use CDATA for content with special characters" and rule 7 says the same about `present_plan` content. These could be consolidated into a single rule: "Always wrap `<content>` parameters in `<![CDATA[...]]>` regardless of content."

#### 10. Plan Quality Rules lack examples

The "Plan Quality Rules" section says to "include exact search strings and replacements when possible" but doesn't show an example of what a good step looks like vs. a vague one. A before/after example would make the expectation concrete.

#### 11. No guidance on handling user cursor position

The system provides the user's cursor position (e.g., "line 15, column 45") but the prompt never explains what to do with this information. Adding guidance like "Use cursor position as a hint for which section the user is focused on when the request is ambiguous" would make use of this context.

#### 12. Execution transition could be more explicit

The prompt says "When the plan is approved, the system switches to execution mode" but the mechanics are described in two separate places (the workflow section and the critical rules). Consolidating into one clear block would reduce confusion.

## Summary of Recommended Changes

| Priority | Change | Impact |
|----------|--------|--------|
| 🔴 High | Add dependency-aware write ordering guidance | Prevents broken intermediate states during execution |
| 🔴 High | Define `present_plan` scope for trivial tasks | Avoids heavyweight plans for one-line fixes |
| 🔴 High | Consolidate execution transition instructions | Clearer mental model for plan→execute handoff |
| 🟡 Medium | Structured retry policy for tool failures | More robust error recovery |
| 🟡 Medium | Clearer `ask_user` threshold | Fewer unnecessary questions, fewer wrong assumptions |
| 🟡 Medium | Add guidance on using cursor position context | Better task interpretation for ambiguous requests |
| 🟡 Medium | Add before/after examples for plan quality | More consistent plan output |
| 🟢 Low | Default CDATA for all `<content>` fields | Eliminates XML escaping edge cases |
| 🟢 Low | Explicit batch size rules | More predictable exploration behavior |
| 🟢 Low | Consolidate duplicate CDATA rules | Cleaner prompt, fewer contradictions |
| 🟢 Low | Add rollback/undo pattern | Graceful recovery from bad edits |
