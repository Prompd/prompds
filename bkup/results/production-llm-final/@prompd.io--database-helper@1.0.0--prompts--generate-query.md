# Production Test: @prompd.io/database-helper@1.0.0/prompts/generate-query.prmd

**Date:** 2025-09-12 21:29:04
**Status:** PASS
**Parameters:** {'query_type': 'SELECT', 'table_name': 'users', 'database_type': 'postgresql'}

## LLM Response

```
+---------------------------------- Response from anthropic/claude-3-haiku-20240307 -----------------------------------+
| Here's an optimized SELECT query for the `users` table in a PostgreSQL database:                                     |
|                                                                                                                      |
| ```sql                                                                                                               |
| -- Optimized SELECT query for users                                                                                  |
| -- Database: postgresql                                                                                              |
|                                                                                                                      |
| SELECT *                                                                                                             |
| FROM users                                                                                                           |
| WHERE email = $1                                                                                                     |
|   AND password = $2                                                                                                  |
| ORDER BY created_at DESC                                                                                             |
| LIMIT 1;                                                                                                             |
| ```                                                                                                                  |
|                                                                                                                      |
| ## Performance Considerations                                                                                        |
|                                                                                                                      |
| 1. **Indexing**: To optimize the query performance, create indexes on the `email` and `password` columns:            |
|                                                                                                                      |
| ```sql                                                                                                               |
| CREATE INDEX ON users (email);                                                                                       |
| CREATE INDEX ON users (password);                                                                                    |
| ```                                                                                                                  |
|                                                                                                                      |
| 2. **Explain Plan Analysis**: Use the `EXPLAIN` statement to analyze the query execution plan and identify any       |
| potential bottlenecks:                                                                                               |
|                                                                                                                      |
| ```sql                                                                                                               |
| EXPLAIN SELECT * FROM users WHERE email = $1 AND password = $2 ORDER BY created_at DESC LIMIT 1;                     |
| ```                                                                                                                  |
|                                                                                                                      |
| 3. **Query Optimization Tips**:                                                                                      |
|    - Consider using a covering index that includes the `created_at` column to avoid the need for a separate sort     |
| operation.                                                                                                           |
|    - If the `users` table is large, consider partitioning it by date or another relevant column to improve query     |
| performance.                                                                                                         |
|                                                                                                                      |
| ## Security Notes                                                                                                    |
|                                                                                                                      |
| 1. **Parameter Binding**: Use parameterized queries to prevent SQL injection attacks. In this example, the `$1` and  |
| `$2` placeholders will be replaced with the actual values for `email` and `password` when the query is executed.     |
|                                                                                                                      |
| ```sql                                                                                                               |
| SELECT * FROM users WHERE email = $1 AND password = $2 ORDER BY created_at DESC LIMIT 1;                             |
| ```                                                                                                                  |
|                                                                                                                      |
| 2. **Input Sanitization**: Ensure that the input values for `email` and `password` are properly sanitized and        |
| validated before executing the query. This can be done using appropriate input validation libraries or custom        |
| functions.                                                                                                           |
|                                                                                                                      |
| 3. **Access Control**: Implement proper access control mechanisms to ensure that users can only access the data they |
| are authorized to view. Consider using row-level security or other access control policies to enforce this.          |
|                                                                                                                      |
| 4. **Error Handling**: Properly handle any errors that may occur during the query execution, such as database        |
| connection issues or syntax errors. Log the errors and provide appropriate error messages to the client, without     |
| exposing sensitive information.                                                                                      |
|                                                                                                                      |
| By following these best practices, you can create a secure and optimized SELECT query for the `users` table in a     |
| PostgreSQL database.                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------+

```
