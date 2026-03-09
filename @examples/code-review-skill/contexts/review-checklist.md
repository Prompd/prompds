# Code Review Checklist

## Security
- [ ] No hardcoded secrets or API keys
- [ ] Input validation on all external data
- [ ] SQL/NoSQL injection protection
- [ ] XSS prevention in rendered output
- [ ] Authentication and authorization checks

## Error Handling
- [ ] All errors are caught and handled appropriately
- [ ] Error messages do not leak internal details
- [ ] Async operations have proper error boundaries
- [ ] Resource cleanup in error paths (connections, file handles)

## Performance
- [ ] No unnecessary database queries in loops
- [ ] Proper use of indexes for frequent queries
- [ ] Large datasets are paginated
- [ ] Caching applied where appropriate

## Code Quality
- [ ] Functions have a single responsibility
- [ ] Variable and function names are descriptive
- [ ] No dead code or commented-out blocks
- [ ] Complex logic has explanatory comments
