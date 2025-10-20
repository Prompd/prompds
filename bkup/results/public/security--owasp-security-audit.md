# Test Results: owasp-security-audit.prmd

**Source File:** `../prompd-base\real-world-prompts\security\owasp-security-audit.prmd`

**Test Date:** 2025-09-12 18:45:48

## Validation Results

- **Syntax Valid:** PASS
- **Parameter Types:** PASS
- **Compilation:** PASS
- **Execution:** PASS

### Compiled Output (First 500 chars)

```markdown
Warning: Required parameter 'application_type' not provided
Warning: Required parameter 'technology_stack' not provided
Warning: Required parameter 'authentication_type' not provided
<!-- PROMPD METADATA
assistant: null
author: null
context: null
description: Comprehensive security audit following OWASP Top 10 and security best
  practices. Analyzes provided codebase and configuration files when available.
id: owasp-security-audit
inherits: null
inputs: {}
name: OWASP Security Audit & Penetratio
... (truncated)
```

### LLM Response (First 1000 chars)

**Command Used:**
```bash
prompd run C:\git\github\Logikbug\prompd-base\real-world-prompts\security\owasp-security-audit.prmd --provider anthropic --model claude-3-haiku-20240307 -p application_type=test-value -p technology_stack=test-value -p authentication_type=test-value
```

**LLM Output:**
```
+---------------------------------- Response from anthropic/claude-3-haiku-20240307 -----------------------------------+
| # OWASP Security Audit: test-value                                                                                   |
|                                                                                                                      |
| > **Context Files Usage**: Run with `--meta:context` to include source code, config files, and documentation:        |
| > ```bash                                                                                                            |
| > prompd run owasp-security-audit.prompd \                                                                           |
| >   --meta:context ./src/auth.js \                                                                                   |
| >   --meta:context ./config/database.yml \                                                                           |
| >   --meta:context ./package.j
... (truncated)
```

## Assessment

✅ **PRODUCTION READY**: All tests passed - ready for registry deployment.
