# Test Results: document-patterns.prmd

**Source File:** `../prompd-base\composable-packages\document-patterns\document-patterns.prmd`

**Test Date:** 2025-09-12 18:42:39

## Validation Results

- **Syntax Valid:** PASS
- **Parameter Types:** PASS
- **Compilation:** PASS
- **Execution:** PASS

### Compiled Output (First 500 chars)

```markdown
Warning: Failed to download from http://localhost:4000: Client error '404 Not Found' for url 'http://localhost:4000/@prompd.io/document-patterns'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
Warning: Failed to download from http://localhost:4000: Client error '404 Not Found' for url 'http://localhost:4000/@prompd.io/base-patterns'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
Warning: Failed to resolve inherit
... (truncated)
```

### LLM Response (First 1000 chars)

**Command Used:**
```bash
prompd run C:\git\github\Logikbug\prompd-base\composable-packages\document-patterns\document-patterns.prmd --provider anthropic --model claude-3-haiku-20240307 -p document_input=test-value
```

**LLM Output:**
```
Warning: Failed to download from http://localhost:4000: Client error '404 Not Found' for url 'http://localhost:4000/@prompd.io/document-patterns'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
Warning: Failed to download from http://localhost:4000: Client error '404 Not Found' for url 'http://localhost:4000/@prompd.io/document-patterns'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
Warning: Failed to download from http://localhost:4000: Client error '404 Not Found' for url 'http://localhost:4000/@prompd.io/base-patterns'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
Warning: Failed to resolve inheritance @prompd.io/base-patterns@2.1.0: Package not found in any registry: @prompd.io/base-patterns@2.1.0
+---------------------------------- Response from anthropic/claude-3-haiku-20240307 -----------------------------------+
| Here are the key points regarding the D
... (truncated)
```

## Assessment

✅ **PRODUCTION READY**: All tests passed - ready for registry deployment.
