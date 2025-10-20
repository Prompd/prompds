# Test Results: base-prompt.prmd

**Source File:** `../prompd-base\examples\base-prompt.prmd`

**Test Date:** 2025-09-12 18:44:26

## Validation Results

- **Syntax Valid:** PASS
- **Parameter Types:** PASS
- **Compilation:** PASS
- **Execution:** PASS

### Compiled Output (First 500 chars)

```markdown
Warning: Required parameter 'topic' not provided
<!-- PROMPD METADATA
assistant: null
author: null
context: null
description: Foundational prompt for structured analysis
id: base-analysis-prompt
inherits: null
inputs: {}
name: Base Analysis Framework
parameters:
- default: null
  description: Topic to analyze
  error_message: null
  example: null
  max_value: null
  min_value: null
  name: topic
  pattern: null
  required: true
  type: string
- default: report
  description: Format of output
  e
... (truncated)
```

### LLM Response (First 1000 chars)

**Command Used:**
```bash
prompd run C:\git\github\Logikbug\prompd-base\examples\base-prompt.prmd --provider anthropic --model claude-3-haiku-20240307 -p topic=test-value
```

**LLM Output:**
```
+---------------------------------- Response from anthropic/claude-3-haiku-20240307 -----------------------------------+
| # Analysis Framework: test-value                                                                                     |
|                                                                                                                      |
| ## Objective                                                                                                         |
| This report provides a structured analysis of the "test-value" using the defined framework.                          |
|                                                                                                                      |
| ## Core Framework                                                                                                    |
|                                                                                                                      |
| ### 1. Overview               
... (truncated)
```

## Assessment

✅ **PRODUCTION READY**: All tests passed - ready for registry deployment.
