# @public/api-patterns

API interaction foundation with REST endpoint analysis, authentication patterns, and API testing frameworks.

## Features

- **Inherits from**: `@prompd.io/base-patterns@2.1.0`
- **Multi-Protocol Support**: REST, GraphQL, SOAP, gRPC, WebHooks, OpenAPI
- **Authentication Methods**: API keys, Bearer tokens, OAuth, JWT, Basic auth, Custom
- **Security Analysis**: OWASP API Security Top 10, input validation, authorization
- **Performance Testing**: Load testing, response time analysis, throughput measurement
- **Documentation Generation**: Comprehensive API documentation with examples
- **Integration Patterns**: SDK analysis, client libraries, webhook implementation
- **Monitoring**: Health checks, uptime monitoring, error rate tracking

## Usage

### Basic API Analysis
```bash
prompd run api-patterns.prmd \
  --api_target "https://api.example.com/v1" \
  --api_type "rest" \
  --interaction_type "analyze"
```

### OpenAPI Specification Analysis
```bash
prompd run api-patterns.prmd \
  --api_target "openapi-spec.json" \
  --api_type "openapi" \
  --documentation_level "comprehensive" \
  --security_analysis true
```

### API Testing with Authentication
```bash
prompd run api-patterns.prmd \
  --api_target "https://secure-api.example.com" \
  --authentication_method "bearer-token" \
  --interaction_type "test" \
  --http_methods '["GET", "POST", "PUT", "DELETE"]'
```

### Performance Testing
```bash
prompd run api-patterns.prmd \
  --api_target "https://api.example.com/products" \
  --interaction_type "monitor" \
  --performance_testing true \
  --security_analysis true
```

### Inheritance Usage
```yaml
---
name: "@yournamespace/api-security-scanner"
inherits: "@public/api-patterns@1.0.0"
parameters:
  - name: "security_standard"
    type: "string"
    enum: ["OWASP", "NIST", "ISO27001"]
---
```

## Parameters

**Inherited from base-patterns:**
- `output_format`, `validation_level`, `context_scope`, `priority_level`, `custom_instructions`

**API-specific parameters:**
- `api_target`: API endpoint URL, OpenAPI spec, or documentation (required)
- `api_type`: rest, graphql, soap, grpc, webhook, openapi, auto-detect
- `authentication_method`: none, api-key, bearer-token, basic-auth, oauth, jwt, custom
- `interaction_type`: analyze, test, monitor, document, integrate, validate
- `http_methods`: Array of HTTP methods to focus on
- `security_analysis`: Perform security analysis of endpoints
- `performance_testing`: Include performance and load testing
- `documentation_level`: minimal, standard, comprehensive, detailed
- `request_headers`: Custom headers for API requests
- `test_data`: Sample test data for validation

## Interaction Types

- **Analyze**: Comprehensive API structure and capability analysis
- **Test**: Functional and security testing of endpoints
- **Monitor**: Health monitoring and performance tracking
- **Document**: Generate comprehensive API documentation
- **Integrate**: Assess integration patterns and SDK quality
- **Validate**: Validate API specifications and compliance

## Authentication Methods

### API Key
- Header-based: `X-API-Key`, `Authorization`
- Query parameter: `?api_key=value`
- Custom implementation patterns

### Bearer Token
- JWT tokens with validation
- OAuth access tokens
- Custom bearer implementations

### OAuth
- OAuth 1.0/2.0 flow analysis
- Scope and permission validation
- Token refresh mechanisms

### Basic Auth
- Username/password combinations
- Base64 encoding validation
- Security assessment

### Custom Authentication
- Proprietary authentication schemes
- Multi-factor authentication
- Custom header patterns

## Security Analysis

### OWASP API Security Top 10
- **API1**: Broken Object Level Authorization
- **API2**: Broken User Authentication
- **API3**: Excessive Data Exposure
- **API4**: Lack of Resources & Rate Limiting
- **API5**: Broken Function Level Authorization
- **API6**: Mass Assignment
- **API7**: Security Misconfiguration
- **API8**: Injection
- **API9**: Improper Assets Management
- **API10**: Insufficient Logging & Monitoring

### Security Testing Areas
- Input validation and sanitization
- Output encoding and data leakage
- Authentication mechanism security
- Authorization and access control
- Rate limiting and abuse prevention
- CORS configuration analysis
- HTTPS/TLS implementation
- API versioning security

## Performance Testing

### Metrics Analyzed
- **Response Time**: Average, median, 95th percentile
- **Throughput**: Requests per second capacity
- **Error Rate**: 4xx/5xx response frequency
- **Availability**: Uptime and reliability metrics
- **Scalability**: Load handling capabilities

### Testing Scenarios
- Normal load simulation
- Peak traffic simulation
- Stress testing beyond capacity
- Endurance testing over time
- Spike testing for sudden loads

## API Type-Specific Features

### REST APIs
- Resource modeling analysis
- HTTP method semantic validation
- Status code implementation review
- Content negotiation testing
- Caching strategy analysis

### GraphQL
- Schema introspection and documentation
- Query/mutation/subscription testing
- Type system validation
- N+1 query detection
- Resolver performance analysis

### SOAP
- WSDL parsing and validation
- Message format validation
- Envelope structure analysis
- Fault handling testing
- WS-Security implementation

### OpenAPI/Swagger
- Specification validation
- Code generation assessment
- Documentation quality review
- Schema validation testing
- Example verification

## Sample Files

### sample-api-spec.json
Complete OpenAPI 3.0 specification demonstrating:
- E-commerce API with products and orders
- JWT authentication
- Multiple HTTP methods
- Request/response schemas
- Error handling patterns
- Security definitions

## Response Structure

- **API Overview**: Type, base URL, version, authentication, endpoint count
- **Security Assessment**: Security rating, issues, recommendations
- **Performance Analysis**: Response times, rate limits, reliability
- **Integration Readiness**: Documentation quality, SDK availability, testing coverage
- **Detailed Documentation**: Comprehensive API documentation with examples

## Error Handling

- **Network Failures**: Timeout and connection error management
- **Authentication Failures**: Token expiration and renewal
- **Rate Limiting**: Backoff strategies and retry logic
- **API Changes**: Version detection and adaptation
- **Data Validation**: Malformed response handling

## Integration Capabilities

- Microservices architecture analysis
- API gateway integration patterns
- Third-party service integration
- Custom API development guidance
- Security auditing and compliance
- Performance optimization strategies

This package serves as the foundation for all API interaction workflows in the Prompd ecosystem.