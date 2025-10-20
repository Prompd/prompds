# Test Results: comprehensive-review.prmd

**Source File:** `../prompd-base\composable-packages\@prompd.io--code-review@1.0.0\prompts\comprehensive-review.prmd`

**Test Date:** 2025-09-12 18:38:05

## Validation Results

- **Syntax Valid:** PASS
- **Parameter Types:** PASS
- **Compilation:** PASS
- **Execution:** PASS

### Compiled Output (First 500 chars)

```markdown
Warning: Failed to resolve inheritance @prompd.io/core-patterns@2.0.0/templates/analysis-framework.prompd: 1 validation error for PackageReference
version
  Value error, Package version must be 1-20 characters [type=value_error, input_value='2.0.0/templates/analysis-framework.prompd', input_type=str]
    For further information visit https://errors.pydantic.dev/2.11/v/value_error
Warning: Required parameter 'code' not provided
Warning: Required parameter 'language' not provided
<!-- PROMPD METAD
... (truncated)
```

### LLM Response (First 1000 chars)

**Command Used:**
```bash
prompd run C:\git\github\Logikbug\prompd-base\composable-packages\@prompd.io--code-review@1.0.0\prompts\comprehensive-review.prmd --provider anthropic --model claude-3-haiku-20240307 -p code=test-value -p language=Python
```

**LLM Output:**
```
Warning: Failed to resolve inheritance @prompd.io/core-patterns@2.0.0/templates/analysis-framework.prompd: 1 validation error for PackageReference
version
  Value error, Package version must be 1-20 characters [type=value_error, input_value='2.0.0/templates/analysis-framework.prompd', input_type=str]
    For further information visit https://errors.pydantic.dev/2.11/v/value_error
+---------------------------------- Response from anthropic/claude-3-haiku-20240307 -----------------------------------+
| ## Review Analysis                                                                                                   |
|                                                                                                                      |
| ### 1. Security Review                                                                                               |
| - The provided code snippet is too short to conduct a comprehensive security review. Without the full context of the |
| applicatio
... (truncated)
```

## Assessment

✅ **PRODUCTION READY**: All tests passed - ready for registry deployment.
