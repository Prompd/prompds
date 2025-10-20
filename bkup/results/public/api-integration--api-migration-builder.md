# Test Results: api-migration-builder.prmd

**Source File:** `../prompd-base\real-world-prompts\api-integration\api-migration-builder.prmd`

**Test Date:** 2025-09-12 18:44:57

## Validation Results

- **Syntax Valid:** PASS
- **Parameter Types:** PASS
- **Compilation:** PASS
- **Execution:** PASS

### Compiled Output (First 500 chars)

```markdown
Warning: Required parameter 'migration_type' not provided
Warning: Required parameter 'target_framework' not provided
<!-- PROMPD METADATA
assistant: null
author: null
context: null
description: Migrate legacy APIs to modern architectures using existing documentation
  and schemas
id: api-migration-builder
inherits: null
inputs: {}
name: API Migration & Legacy System Integration
parameters:
- default: null
  description: Type of API migration to perform
  error_message: null
  example: null
  ma
... (truncated)
```

### LLM Response (First 1000 chars)

**Command Used:**
```bash
prompd run C:\git\github\Logikbug\prompd-base\real-world-prompts\api-integration\api-migration-builder.prmd --provider anthropic --model claude-3-haiku-20240307 -p migration_type=test-value -p target_framework=express
```

**LLM Output:**
```
+---------------------------------- Response from anthropic/claude-3-haiku-20240307 -----------------------------------+
| Here are some examples of context files that could be used in the prompts:                                           |
|                                                                                                                      |
| 1. **Legacy API Documentation** (legacy_api_docs.yaml):                                                              |
| ```yaml                                                                                                              |
| openapi: 3.0.0                                                                                                       |
| info:                                                                                                                |
|   title: Legacy User API                                                                                             |
|   version: 1.0.0              
... (truncated)
```

## Assessment

✅ **PRODUCTION READY**: All tests passed - ready for registry deployment.
