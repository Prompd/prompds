# @prompd.io/security-analysis

Specialized security analysis package inheriting from code-patterns with advanced vulnerability detection, threat modeling, and security compliance capabilities.

## Features

- **Inherits from**: `@prompd.io/code-patterns@1.0.0` (includes all code analysis capabilities)
- **Security Standards**: OWASP, SANS, CWE, NIST, ISO27001, SOC2, PCI-DSS, GDPR
- **Threat Modeling**: STRIDE analysis, attack surface mapping, risk assessment
- **Vulnerability Detection**: SAST, DAST, IAST with severity classification
- **Compliance Checking**: Automated compliance validation against standards
- **Penetration Testing**: Security testing scenarios and attack simulation
- **Advanced Metrics**: Security KPIs, vulnerability trends, security debt

## Usage

### OWASP Security Analysis
```bash
prompd run security-analysis.prmd \
  --code_input "webapp_source.js" \
  --security_standard "OWASP" \
  --threat_modeling true \
  --vulnerability_severity "medium"
```

### Comprehensive Security Assessment
```bash
prompd run security-analysis.prmd \
  --code_input "enterprise_app/" \
  --security_standard "NIST" \
  --compliance_check true \
  --security_domains '["authentication", "authorization", "crypto", "data-protection"]'
```

### Penetration Testing Analysis
```bash
prompd run security-analysis.prmd \
  --code_input "api_endpoints.py" \
  --penetration_testing true \
  --attack_vectors '["injection", "xss", "broken-auth", "sensitive-exposure"]'
```

## Enhanced Parameters

**Inherited from code-patterns:**
- All base code analysis parameters plus security-focused extensions

**Security-specific parameters:**
- `security_standard`: OWASP, SANS, CWE, NIST, ISO27001, SOC2, PCI-DSS, GDPR
- `threat_modeling`: Comprehensive STRIDE threat analysis
- `vulnerability_severity`: Minimum severity level to report
- `compliance_check`: Automated compliance validation
- `penetration_testing`: Include penetration testing scenarios
- `security_domains`: Focused security analysis areas
- `attack_vectors`: Specific attack patterns to analyze

## Security Standards

### OWASP Top 10 (2021)
- A01: Broken Access Control
- A02: Cryptographic Failures
- A03: Injection
- A04: Insecure Design
- A05: Security Misconfiguration
- A06: Vulnerable Components
- A07: Authentication Failures
- A08: Data Integrity Failures
- A09: Security Logging Failures
- A10: Server-Side Request Forgery

### SANS Top 25
- Insecure Interaction Between Components
- Risky Resource Management
- Porous Defenses

### CWE Classification
- CWE-79: Cross-site Scripting
- CWE-89: SQL Injection
- CWE-20: Improper Input Validation
- Plus comprehensive CWE coverage

## Threat Modeling

### STRIDE Analysis
- **Spoofing**: Identity verification weaknesses
- **Tampering**: Data integrity vulnerabilities
- **Repudiation**: Non-repudiation failures
- **Information Disclosure**: Data exposure risks
- **Denial of Service**: Availability threats
- **Elevation of Privilege**: Authorization bypasses

### Attack Surface Mapping
- Entry point identification
- Trust boundary analysis
- Asset inventory and classification
- Data flow security assessment

## Security Domains

### Authentication & Authorization
- Multi-factor authentication analysis
- Role-based and attribute-based access control
- Privilege escalation detection
- Session management security

### Input Validation & Injection Prevention
- SQL injection detection and prevention
- XSS vulnerability assessment
- Command injection analysis
- LDAP and XML injection checks

### Cryptographic Security
- Algorithm strength assessment
- Key management evaluation
- Certificate validation
- Secure hashing practices

### Data Protection & Privacy
- GDPR compliance validation
- PCI-DSS requirements
- Data classification and handling
- Privacy by design principles

## Vulnerability Detection

### Static Analysis (SAST)
- Taint analysis for data flow security
- Control flow vulnerability assessment
- Pattern matching for known vulnerabilities
- False positive reduction

### Dynamic Analysis (DAST)
- Runtime security testing
- Fuzz testing for input validation
- Memory safety assessment
- Real-time vulnerability detection

### Interactive Testing (IAST)
- Combined static and dynamic analysis
- Code coverage for security tests
- Contextual vulnerability validation

## Compliance Frameworks

### Regulatory Compliance
- **GDPR**: Privacy and data protection
- **PCI-DSS**: Payment card security
- **SOC 2**: Service organization controls
- **HIPAA**: Healthcare information protection

### Industry Standards
- **ISO 27001**: Information security management
- **NIST Cybersecurity Framework**: Risk management
- **OWASP ASVS**: Application security verification

## Response Structure

### Executive Security Summary
- Overall security rating and compliance status
- Critical vulnerability count and priority
- Immediate action requirements
- Business risk assessment

### Detailed Vulnerability Report
- Severity-based vulnerability classification
- CWE mapping and CVSS scoring
- Exploitation scenarios and impact analysis
- Specific remediation recommendations

### Threat Model Results
- STRIDE analysis findings
- Attack surface assessment
- Risk matrix with likelihood and impact
- Security architecture recommendations

### Compliance Assessment
- Standards-based compliance scoring
- Gap analysis and remediation roadmap
- Control implementation status
- Audit readiness assessment

This package provides enterprise-grade security analysis capabilities built on the solid foundation of code-patterns while adding specialized security expertise.