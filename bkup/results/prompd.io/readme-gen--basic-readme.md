# Test Results: basic-readme.prmd

**Source File:** `../prompd-base\composable-packages\@prompd.io--readme-gen@1.0.0\prompts\basic-readme.prmd`

**Test Date:** 2025-09-12 18:39:02

## Validation Results

- **Syntax Valid:** PASS
- **Parameter Types:** PASS
- **Compilation:** PASS
- **Execution:** PASS

### Compiled Output (First 500 chars)

```markdown
Warning: Required parameter 'project_name' not provided
Warning: Required parameter 'description' not provided
Warning: Required parameter 'language' not provided
<!-- PROMPD METADATA
assistant: null
author: null
context: null
description: Generate a clean, professional README file for any project
id: basic-readme
inherits: null
inputs: {}
name: Basic README Generator
parameters:
- default: null
  description: Name of the project
  error_message: null
  example: null
  max_value: null
  min_valu
... (truncated)
```

### LLM Response (First 1000 chars)

**Command Used:**
```bash
prompd run C:\git\github\Logikbug\prompd-base\composable-packages\@prompd.io--readme-gen@1.0.0\prompts\basic-readme.prmd --provider anthropic --model claude-3-haiku-20240307 -p project_name=TestApp -p description=test-value -p language=Python
```

**LLM Output:**
```
+---------------------------------- Response from anthropic/claude-3-haiku-20240307 -----------------------------------+
| This appears to be a basic README.md file for a project called "TestApp". Here's a breakdown of the sections:        |
|                                                                                                                      |
| 1. **Title**: The project is called "TestApp".                                                                       |
|                                                                                                                      |
| 2. **Description**: The project has a description of "test-value".                                                   |
|                                                                                                                      |
| 3. **Installation**: The installation instructions are provided, which involve running `npm install TestApp` in the  |
| terminal.                     
... (truncated)
```

## Assessment

✅ **PRODUCTION READY**: All tests passed - ready for registry deployment.
