# Test Results: base-security-audit.prmd

**Source File:** `../prompd-base\composable-packages\@prompd.io--security-toolkit@1.0.0\prompts\base-security-audit.prmd`

**Test Date:** 2025-09-12 18:39:37

## Validation Results

- **Syntax Valid:** PASS
- **Parameter Types:** PASS
- **Compilation:** PASS
- **Execution:** PASS

### Compiled Output (First 500 chars)

```markdown
Warning: Required parameter 'application_name' not provided
<!-- PROMPD METADATA
assistant: ../../@prompd.io--core-patterns@2.0.0/assistants/penetration-tester.md
author: null
context: ../../@prompd.io--core-patterns@2.0.0/contexts/owasp-top-10.md
description: Performs a comprehensive security audit using OWASP standards and penetration
  testing methodology
id: security-audit
inherits: ../../@prompd.io--core-patterns@2.0.0/templates/analysis-framework.prmd
inputs: {}
name: Comprehensive Securit
... (truncated)
```

### LLM Response (First 1000 chars)

**Command Used:**
```bash
prompd run C:\git\github\Logikbug\prompd-base\composable-packages\@prompd.io--security-toolkit@1.0.0\prompts\base-security-audit.prmd --provider anthropic --model claude-3-haiku-20240307 -p application_name=TestApp
```

**LLM Output:**
```
+---------------------------------- Response from anthropic/claude-3-haiku-20240307 -----------------------------------+
| # Security Audit for TestApp                                                                                         |
|                                                                                                                      |
| ## Overview                                                                                                          |
| The purpose of this security audit is to comprehensively evaluate the security posture of the TestApp application.   |
| The key objectives are to identify any vulnerabilities or weaknesses, and provide actionable recommendations to      |
| enhance the overall security of the system.                                                                          |
|                                                                                                                      |
| ## Detailed Assessment        
... (truncated)
```

## Assessment

✅ **PRODUCTION READY**: All tests passed - ready for registry deployment.
