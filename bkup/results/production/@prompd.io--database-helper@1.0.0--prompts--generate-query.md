# Test Results: @prompd.io\database-helper@1.0.0\prompts\generate-query.prmd

**Source File:** `..\prompd-base\production\@prompd.io\database-helper@1.0.0\prompts\generate-query.prmd`

**Test Date:** 2025-09-12 21:14:39

## Execution Results

- **Status:** PASS

### LLM Response

```
Warning: Required parameter 'query_type' not provided
Warning: Required parameter 'table_name' not provided
Warning: Required parameter 'database_type' not provided
+---------------------------------- Response from anthropic/claude-3-haiku-20240307 -----------------------------------+
| # Generate MySQL Query                                                                                               |
|                                                                                                                      |
| Create an optimized {{query_type}} query for the {{table_name}} table.                                               |
|                                                                                                                      |
| ## Query Requirements                                                                                                |
|                                                                                                                      |
| - **Type**: {{query_type}}                                                                                           |
| - **Table**: {{table_name}}                                                                                          |
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
| -- Optimized {{query_type}} query for {{table_name}}                                                                 |
| -- Database: MySQL                                                                                                   |
| ```                                                                                                                  |
|                                                                                                                      |
| ## Performance Considerations                                                                                        |
|                                                                                                                      |
| - Index recommendations for optimal query performance:                                                               |
|   - Create an index on the columns used in the `WHERE` clause to improve query speed.                                |
|   - Consider a composite index if multiple columns are used in the `WHERE` clause.                                   |
| - Explain plan analysis suggestions:                                                                                 |
|   - Run `EXPLAIN` on the query to identify potential performance bottlenecks.                                        |
|   - Analyze the execution plan and make adjustments based on the output.                                             |
| - Query optimization tips specific to MySQL:                                                                         |
|   - Check for unnecessary `DISTINCT`, `GROUP BY`, or `ORDER BY` clauses.                                             |
|   - Avoid using `SELECT *` and instead specify the required columns.                                                 |
|   - Use appropriate data types to minimize storage and improve performance.                                          |
|                                                                                                                      |
| ## Security Notes                                                                                                    |
|                                                                                                                      |
| - Parameter binding examples:                                                                                        |
|   ```sql                                                                                                             |
|   -- Example prepared statement                                                                                      |
|   PREPARE stmt FROM 'SELECT * FROM {{table_name}} WHERE column = ?';                                                 |
|   EXECUTE stmt USING @input_value;                                                                                   |
|   ```                                                                                                                |
| - Input sanitization requirements:                                                                                   |
|   - Validate and sanitize all user input to prevent SQL injection attacks.                                           |
|   - Use MySQL's built-in functions like `PREPARE` and `EXECUTE` to handle user input securely.                       |
| - Access control recommendations:                                                                                    |
|   - Grant the minimum required permissions to the database user executing the query.                                 |
|   - Implement row-level or column-level security if necessary.                                                       |
+----------------------------------------------------------------------------------------------------------------------+

```

