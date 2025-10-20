# AGENTS.md

Note: For a consolidated, up-to-date overview of repo guidelines and current status, see `prompd.md` at the repository root.

Guidance for AI coding agents (Claude Code, OpenAI Codex CLI, etc.) working in this repository. Keep changes minimal, consistent, and aligned with the Prompd composable prompt architecture.

## Purpose
- Define a consistent operating model for agents contributing to this repo.
- Standardize command verbs and documentation examples.
- Ensure high signal changes with strong security and quality defaults.

## Canonical CLI Verbs
Use these verbs and only these in docs, examples, and scripts:
- compile: Build provider-specific output from `.prompd` or `.pdflow` files.
- run: Execute a prompt/flow with runtime context flags (e.g., `--meta:context`) or start the interactive shell.
- validate: Check prompt/flow syntax and parameter schema.
- install | publish | list | search | cache: Package/registry operations as documented in `CLAUDE.md`.

Do not use: generate, execute, render.
- Replace generate → compile
- Replace execute → run
- Replace render → compile

## Repository Structure
- prompds/: Core engineering prompt templates (implementation, architecture, bug-fix, testing, master)
- real-world-prompts/: Domain prompts (API, database, security, data science, finance, marketing)
- pdflows/: Multi-step workflow definitions
- composable-packages/: Package-based components and manifests
- packages/ and packages-new/: Built/published `.pdpkg` artifacts
- engineering-prompts.pdproj: Project metadata

See `README.md` and `CLAUDE.md` for quick-start commands and context.

## Editing Conventions
- Scope: Make the smallest change that fully solves the asked task; avoid drive-by edits.
- Style: Match existing formatting and tone; keep examples practical and runnable.
- Paths: Prefer workspace-relative paths; when showing absolute examples, align with platform context.
- Cross-platform: Provide Bash examples; add PowerShell equivalents only when explicitly asked.
- Security: Never include secrets or sensitive data in examples; favor secure defaults.

## Prompt/Flow Guidelines
- Headers: Include `name`, `display_name`, `version`, `description`, `tags`, and `parameters` with `type`, `required`, `enum`/`default` where applicable.
- Parameters: Use clear names; prefer enums for constrained values (e.g., security levels, languages).
- Context: Only require `context` in headers when the prompt always needs those files; otherwise document `--meta:context` usage.
- Output: Prompts should describe complete, production-quality outputs; avoid placeholders like “implementation here”.
- Security Levels: Support `standard`, `high`, `critical` with explicit, escalating requirements.

## Validation & Testing
- Validate single file: `prompd validate <path/to/file.prompd>`
- Validate all: Iterate over `*.prompd` and `*.pdflow` and validate each.
- Compile smoke tests: Provide a minimal params file alongside new prompts to ensure compilation works.

## Parameters & Examples
- Params files: Place under a nearby `params/` directory when referenced (e.g., `real-world-prompts/api-integration/params/saas-api.json`).
- Naming: Use descriptive, environment-aware names (e.g., `production-api.json`, `dev-migration.json`).
- Consistency: Keep parameter names consistent across docs and prompt definitions.

## Documentation Rules
- Verbs: Use compile and run consistently (no generate/execute/render).
- Redundancy: Consolidate repeated examples; prefer referencing a single authoritative snippet.
- Links: Clearly mark cross-repo links; avoid dangling relative links that don’t exist locally.
- Examples: Favor concise, copy-pasteable commands with realistic values.

## Do / Don’t
- Do: 
  - Keep PRs/patches focused and reversible.
  - Update adjacent docs when changing verbs, paths, or parameters.
  - Add minimal working params files when introducing references in docs.
- Don’t:
  - Introduce unrelated refactors.
  - Change command verbs away from the canonical list.
  - Commit generated outputs or secrets.

## Common Commands (Authoritative Examples)
- Compile a core prompt:
  ```bash
  prompd compile prompds/code-implementation.prompd \
    --params component_name="Registry Auth Middleware" \
    language="nodejs" \
    security_level="critical"
  ```
- Compile a domain prompt with params file:
  ```bash
  prompd compile real-world-prompts/api-integration/rest-endpoint-builder.prompd \
    --params-file real-world-prompts/api-integration/params/saas-api.json
  ```
- Run with context files:
  ```bash
  prompd run real-world-prompts/security/owasp-security-audit.prompd \
    --params-file security-params.json \
    --meta:context ./src/auth.js \
    --meta:context ./config/database.yml
  ```
- Validate a prompt:
  ```bash
  prompd validate prompds/architecture-review.prompd
  ```
- Workflow (compile):
  ```bash
  prompd compile pdflows/engineering-workflow.pdflow \
    --params feature_name="User Authentication System" \
    language="nodejs" \
    security_level="critical"
  ```

## Adding New Prompts
- Start from an existing prompt with similar structure and adapt.
- Define parameters with clear types and defaults; document security/test expectations.
- Include a short, real params example in `params/` to validate locally.
- Update `README.md`/`HOW-TO-USE.md` with a single example if the prompt is user-facing.

## Quality Checklist (Pre-merge)
- Verbs follow canonical list (compile/run/validate).
- Examples compile locally (or are clearly marked if not available).
- No broken relative links or missing params files referenced.
- Security guidance matches the defined `security_level` tiers.
- Minimal, focused diff; surrounding docs updated if necessary.

## Contact & Ownership
- This repo is part of the Prompd ecosystem. For engine behavior and provider formats, refer to the Prompd CLI docs and the composable architecture notes in `COMPOSABLE-ARCHITECTURE.md` and `CLAUDE.md`.
