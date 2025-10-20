# Test Results: rest-endpoint-builder.prmd

**Source File:** `../prompd-base\real-world-prompts\api-integration\rest-endpoint-builder.prmd`

**Test Date:** 2025-09-12 18:45:20

## Validation Results

- **Syntax Valid:** PASS
- **Parameter Types:** PASS
- **Compilation:** PASS
- **Execution:** PASS

### Compiled Output (First 500 chars)

```markdown
Warning: Required parameter 'endpoint_name' not provided
Warning: Required parameter 'resource_name' not provided
Warning: Required parameter 'framework' not provided
Warning: Required parameter 'database' not provided
<!-- PROMPD METADATA
assistant: null
author: null
context: null
description: Generates complete REST API endpoints with validation, documentation,
  and testing
id: rest-endpoint-builder
inherits: null
inputs: {}
name: REST API Endpoint Builder
parameters:
- default: null
  descri
... (truncated)
```

### LLM Response (First 1000 chars)

**Command Used:**
```bash
prompd run C:\git\github\Logikbug\prompd-base\real-world-prompts\api-integration\rest-endpoint-builder.prmd --provider anthropic --model claude-3-haiku-20240307 -p endpoint_name=TestApp -p resource_name=TestApp -p framework=express -p database=test-value
```

**LLM Output:**
```
+---------------------------------- Response from anthropic/claude-3-haiku-20240307 -----------------------------------+
| Here's a sample implementation of the REST API endpoint system for the TestApp management using Express and          |
| test-value:                                                                                                          |
|                                                                                                                      |
| ```javascript                                                                                                        |
| // server.js                                                                                                         |
| const express = require('express');                                                                                  |
| const mongoose = require('mongoose');                                                                                |
| const app = express();        
... (truncated)
```

## Assessment

✅ **PRODUCTION READY**: All tests passed - ready for registry deployment.
