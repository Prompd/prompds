# @prompd.io/code-patterns

Code analysis foundation with language-agnostic patterns, security check frameworks, and performance analysis capabilities.

## Features

- **Inherits from**: `@prompd.io/base-patterns@2.1.0`
- **Multi-Language Support**: JavaScript, TypeScript, Python, Java, C#, C++, Go, Rust, PHP, Ruby, Swift, Kotlin, SQL, HTML, CSS
- **Security Analysis**: OWASP Top 10, injection attacks, authentication, authorization, cryptography
- **Performance Analysis**: Complexity, efficiency, memory, scalability, algorithms
- **Quality Assessment**: Maintainability, readability, testability, modularity, documentation
- **Language-Specific Patterns**: Framework-specific best practices and security patterns

## Usage

### Basic Code Analysis
```bash
prompd run code-patterns.prmd \
  --code_input "path/to/source.js" \
  --language "javascript" \
  --analysis_scope "comprehensive"
```

### Security-Focused Analysis
```bash
prompd run code-patterns.prmd \
  --code_input "$(cat vulnerable_code.py)" \
  --language "python" \
  --analysis_scope "security" \
  --security_focus '["injection", "authentication", "crypto"]'
```

### Performance Analysis
```bash
prompd run code-patterns.prmd \
  --code_input "performance_critical.cpp" \
  --language "cpp" \
  --analysis_scope "performance" \
  --performance_metrics '["complexity", "memory", "algorithms"]'
```

### Quality Assessment
```bash
prompd run code-patterns.prmd \
  --code_input "legacy_code.java" \
  --language "java" \
  --analysis_scope "quality" \
  --quality_standards '["maintainability", "documentation", "testability"]'
```

### Inheritance Usage
```yaml
---
name: "@yournamespace/security-scanner"
inherits: "@prompd.io/code-patterns@1.0.0"
parameters:
  - name: "compliance_standard"
    type: "string"
    enum: ["OWASP", "SANS", "CWE", "NIST"]
---
```

## Parameters

**Inherited from base-patterns:**
- `output_format`, `validation_level`, `context_scope`, `priority_level`, `custom_instructions`

**Code-specific parameters:**
- `code_input`: Code content, file path, or repository (required)
- `language`: Programming language or auto-detect
- `analysis_scope`: syntax, structure, security, performance, quality, comprehensive
- `security_focus`: Array of security concerns to prioritize
- `performance_metrics`: Array of performance aspects to analyze
- `quality_standards`: Array of code quality standards to apply
- `include_suggestions`: Include improvement suggestions and fixes
- `context_files`: Additional context files or dependencies

## Analysis Dimensions

### Security Analysis
- **Injection Attacks**: SQL, XSS, command, LDAP injection
- **Authentication**: Weak mechanisms, credential storage
- **Authorization**: Access control, privilege escalation
- **Cryptography**: Weak encryption, key management
- **Input Validation**: Boundary checks, sanitization
- **Output Encoding**: Data leakage prevention
- **Session Management**: Session security
- **Error Handling**: Information disclosure

### Performance Analysis
- **Complexity**: Cyclomatic and cognitive complexity
- **Efficiency**: Algorithm and resource optimization
- **Memory**: Leak detection, usage optimization
- **Scalability**: Concurrent access, bottlenecks
- **Caching**: Strategy optimization
- **Database**: Query and connection optimization
- **Network**: API and communication efficiency

### Quality Analysis
- **Maintainability**: Code organization and structure
- **Readability**: Clarity and self-documentation
- **Testability**: Test coverage and design
- **Modularity**: Separation of concerns
- **Documentation**: Inline and API documentation
- **Naming**: Meaningful identifiers
- **Duplication**: DRY principle adherence
- **Coupling**: Dependency management

## Language-Specific Features

### JavaScript/TypeScript
- Type safety analysis (TypeScript)
- Async/await pattern validation
- Event handling security
- Package dependency analysis

### Python
- PEP 8 compliance checking
- Import management
- Exception handling patterns
- Memory management analysis

### Java
- Object-oriented principle validation
- Thread safety analysis
- Spring security patterns
- Exception handling

### C#
- .NET best practice validation
- Async pattern analysis
- Entity Framework security
- Dependency injection patterns

### C++
- Memory management (RAII)
- Template usage analysis
- Buffer overflow prevention
- Smart pointer validation

### Go
- Goroutine management
- Error handling patterns
- Interface design
- Concurrency safety

## Sample Code

Includes `sample-code.js` with examples of:
- Security vulnerabilities (SQL injection)
- Performance issues (inefficient algorithms)
- Quality problems (unclear naming, missing error handling)
- Improved implementations demonstrating best practices

## Response Structure

- **Executive Summary**: Overall assessment and key findings
- **Security Assessment**: Vulnerability analysis and recommendations
- **Performance Assessment**: Bottleneck identification and optimization
- **Quality Assessment**: Maintainability and readability analysis
- **Improvement Suggestions**: Prioritized recommendations with code examples

This package serves as the foundation for all code analysis workflows in the Prompd ecosystem.