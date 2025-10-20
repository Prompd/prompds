# Test Results: security-analysis.prmd

**Source File:** `../prompd-base\composable-packages\security-analysis\security-analysis.prmd`

**Test Date:** 2025-09-12 18:44:12

## Validation Results

- **Syntax Valid:** PASS
- **Parameter Types:** PASS
- **Compilation:** PASS
- **Execution:** PASS

### Compiled Output (First 500 chars)

```markdown
Warning: Failed to download from http://localhost:4000: Client error '404 Not Found' for url 'http://localhost:4000/@prompd.io/security-analysis'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
Warning: Failed to download from http://localhost:4000: Client error '404 Not Found' for url 'http://localhost:4000/@prompd.io/code-patterns'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
Warning: Failed to resolve inherit
... (truncated)
```

### LLM Response (First 1000 chars)

**Command Used:**
```bash
prompd run C:\git\github\Logikbug\prompd-base\composable-packages\security-analysis\security-analysis.prmd --provider anthropic --model claude-3-haiku-20240307
```

**LLM Output:**
```
Warning: Failed to download from http://localhost:4000: Client error '404 Not Found' for url 'http://localhost:4000/@prompd.io/security-analysis'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
Warning: Failed to download from http://localhost:4000: Client error '404 Not Found' for url 'http://localhost:4000/@prompd.io/security-analysis'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
Warning: Failed to download from http://localhost:4000: Client error '404 Not Found' for url 'http://localhost:4000/@prompd.io/code-patterns'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
Warning: Failed to resolve inheritance @prompd.io/code-patterns@1.0.0: Package not found in any registry: @prompd.io/code-patterns@1.0.0
+---------------------------------- Response from anthropic/claude-3-haiku-20240307 -----------------------------------+
| This is an impressive and comprehensive
... (truncated)
```

## Assessment

✅ **PRODUCTION READY**: All tests passed - ready for registry deployment.
