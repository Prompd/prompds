# Test Results: generate-readme.prmd

**Source File:** `../prompd-base\composable-packages\@prompd.io--documentation@1.0.0\prompts\generate-readme.prmd`

**Test Date:** 2025-09-12 18:38:55

## Validation Results

- **Syntax Valid:** PASS
- **Parameter Types:** PASS
- **Compilation:** PASS
- **Execution:** PASS

### Compiled Output (First 500 chars)

```markdown
Warning: Required parameter 'project_name' not provided
Warning: Required parameter 'project_description' not provided
Warning: Required parameter 'language' not provided
<!-- PROMPD METADATA
assistant: null
author: null
context: null
description: Generate a comprehensive README.md file for a software project
id: generate-readme
inherits: null
inputs: {}
name: Generate README File
parameters:
- default: null
  description: Name of the project
  error_message: null
  example: null
  max_value: nu
... (truncated)
```

### LLM Response (First 1000 chars)

**Command Used:**
```bash
prompd run C:\git\github\Logikbug\prompd-base\composable-packages\@prompd.io--documentation@1.0.0\prompts\generate-readme.prmd --provider anthropic --model claude-3-haiku-20240307 -p project_name=TestApp -p project_description=test-value -p language=Python
```

**LLM Output:**
```
+---------------------------------- Response from anthropic/claude-3-haiku-20240307 -----------------------------------+
| # TestApp                                                                                                            |
|                                                                                                                      |
| ![Build Status](https://img.shields.io/github/workflow/status/your-username/TestApp/CI)                              |
| ![Version](https://img.shields.io/pypi/v/TestApp)                                                                    |
| ![License](https://img.shields.io/github/license/your-username/TestApp)                                              |
|                                                                                                                      |
| TestApp is a Python library that provides a simple and intuitive interface for testing your applications. It         |
| includes a variety of utilitie
... (truncated)
```

## Assessment

✅ **PRODUCTION READY**: All tests passed - ready for registry deployment.
