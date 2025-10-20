# Test Results: graphql-schema-builder.prmd

**Source File:** `../prompd-base\real-world-prompts\api-integration\graphql-schema-builder.prmd`

**Test Date:** 2025-09-12 18:45:08

## Validation Results

- **Syntax Valid:** PASS
- **Parameter Types:** PASS
- **Compilation:** PASS
- **Execution:** PASS

### Compiled Output (First 500 chars)

```markdown
Warning: Required parameter 'service_name' not provided
Warning: Required parameter 'primary_entity' not provided
Warning: Required parameter 'framework' not provided
Warning: Required parameter 'database' not provided
<!-- PROMPD METADATA
assistant: null
author: null
context: null
description: Generates complete GraphQL schemas with resolvers, subscriptions, and
  security
id: graphql-schema-builder
inherits: null
inputs: {}
name: GraphQL Schema & Resolver Builder
parameters:
- default: null
  
... (truncated)
```

### LLM Response (First 1000 chars)

**Command Used:**
```bash
prompd run C:\git\github\Logikbug\prompd-base\real-world-prompts\api-integration\graphql-schema-builder.prmd --provider anthropic --model claude-3-haiku-20240307 -p service_name=TestApp -p primary_entity=test-value -p framework=express -p database=test-value
```

**LLM Output:**
```
+---------------------------------- Response from anthropic/claude-3-haiku-20240307 -----------------------------------+
| Here is the GraphQL schema and resolver implementation for the TestApp application based on the requirements you     |
| provided:                                                                                                            |
|                                                                                                                      |
| ```graphql                                                                                                           |
| # GraphQL Schema                                                                                                     |
|                                                                                                                      |
| ## Core Type Definition                                                                                              |
| type test-value {             
... (truncated)
```

## Assessment

✅ **PRODUCTION READY**: All tests passed - ready for registry deployment.
