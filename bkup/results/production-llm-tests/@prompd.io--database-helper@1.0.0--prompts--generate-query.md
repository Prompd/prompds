# LLM Test Results: @prompd.io\database-helper@1.0.0\prompts\generate-query.prmd

**Source:** ..\prompd-base\production\@prompd.io\database-helper@1.0.0\prompts\generate-query.prmd
**Date:** 2025-09-12 21:19:31
**Status:** PASS

## LLM Response

```
Warning: Required parameter 'query_type' not provided
Warning: Required parameter 'table_name' not provided
Warning: Required parameter 'database_type' not provided
+---------------------------------- Response from anthropic/claude-3-haiku-20240307 -----------------------------------+
| # Generate MySQL Query                                                                                               |
|                                                                                                                      |
| Create an optimized SELECT query for the users table.                                                                |
|                                                                                                                      |
| ## Query Requirements                                                                                                |
|                                                                                                                      |
| - **Type**: SELECT                                                                                                   |
| - **Table**: users                                                                                                   |
| - **Columns**: *                                                                                                     |
| - **Conditions**:                                                                                                    |
| - **Database**: MySQL                                                                                                |
|                                                                                                                      |
| ## Best Practices to Follow                                                                                          |
|                                                                                                                      |
| 1. **Security**: Use parameterized queries to prevent SQL injection                                                  |
| 2. **Performance**: Include appropriate indexing suggestions                                                         |
| 3. **Clarity**: Write readable, well-formatted SQL                                                                   |
| 4. **Validation**: Include input validation recommendations                                                          |
| 5. **Error Handling**: Suggest proper error handling approaches                                                      |
|                                                                                                                      |
| ## Generated Query                                                                                                   |
|                                                                                                                      |
| ```sql                                                                                                               |
| -- Optimized SELECT query for users                                                                                  |
| -- Database: MySQL                                                                                                   |
| SELECT *                                                                                                             |
| FROM users                                                                                                           |
| WHERE 1=1                                                                                                            |
|   AND username = ?                                                                                                   |
|   AND email = ?                                                                                                      |
| ```                                                                                                                  |
|                                                                                                                      |
| ## Performance Considerations                                                                                        |
|                                                                                                                      |
| - Index recommendations:                                                                                             |
|   - Create an index on the `username` and `email` columns for efficient filtering.                                   |
| - Explain plan analysis:                                                                                             |
|   - The query should utilize the `username` and `email` indexes, resulting in a fast lookup.                         |
| - Query optimization tips:                                                                                           |
|   - Avoid using `SELECT *` in production code; specify the required columns instead.                                 |
|   - Consider pagination or limiting the result set if retrieving a large number of records.                          |
|                                                                                                                      |
| ## Security Notes                                                                                                    |
|                                                                                                                      |
| - Parameter binding examples:                                                                                        |
|   ```php                                                                                                             |
|   $stmt = $pdo->prepare("SELECT * FROM users WHERE username = ? AND email = ?");                                     |
|   $stmt->execute([$username, $email]);                                                                               |
|   $result = $stmt->fetchAll();                                                                                       |
|   ```                                                                                                                |
| - Input sanitization requirements:                                                                                   |
|   - Validate `$username` and `$email` inputs to prevent SQL injection.                                               |
| - Access control recommendations:                                                                                    |
|   - Ensure the application user has the necessary permissions to access the `users` table.                           |
|   - Implement row-level security policies if required.                                                               |
+----------------------------------------------------------------------------------------------------------------------+

```
