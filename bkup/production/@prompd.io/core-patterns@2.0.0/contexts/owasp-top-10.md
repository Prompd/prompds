# OWASP Top 10 2021 Web Application Security Risks

## A01:2021 – Broken Access Control
**Description**: Restrictions on authenticated users are not properly enforced
**Common Weaknesses**:
- Violation of principle of least privilege
- Bypassing access control checks
- Metadata manipulation (JWT tokens, cookies)
- CORS misconfiguration

## A02:2021 – Cryptographic Failures
**Description**: Failures related to cryptography which lead to sensitive data exposure
**Common Issues**:
- Transmitting data in clear text
- Using old or weak cryptographic algorithms
- Weak or default cryptographic keys
- Missing certificate validation

## A03:2021 – Injection
**Description**: User-supplied data is not validated, filtered, or sanitized
**Types Include**:
- SQL injection
- NoSQL injection
- Command injection
- LDAP injection

## A04:2021 – Insecure Design
**Description**: Missing or ineffective control design
**Characteristics**:
- Threat modeling failures
- Insecure design patterns
- Missing business logic validation
- Insufficient security controls

## A05:2021 – Security Misconfiguration
**Description**: Missing appropriate security hardening
**Common Examples**:
- Default configurations
- Incomplete or ad hoc configurations
- Open cloud storage
- Verbose error messages

## A06:2021 – Vulnerable and Outdated Components
**Description**: Using components with known vulnerabilities
**Risk Factors**:
- Unknown component versions
- Vulnerable, unsupported, or out-of-date software
- Irregular security scanning
- Delayed security updates

## A07:2021 – Identification and Authentication Failures
**Description**: Functions related to user identity and authentication
**Common Issues**:
- Permits brute force attacks
- Weak or well-known passwords
- Weak credential recovery processes
- Missing multi-factor authentication

## A08:2021 – Software and Data Integrity Failures
**Description**: Making assumptions about software updates and critical data
**Examples**:
- Unsigned software updates
- Insecure CI/CD pipelines
- Auto-update functionality
- Serialization/deserialization flaws

## A09:2021 – Security Logging and Monitoring Failures
**Description**: Insufficient logging and monitoring
**Consequences**:
- Audit events not logged
- Warnings and errors generate no logs
- Logs only stored locally
- No real-time alerting

## A10:2021 – Server-Side Request Forgery (SSRF)
**Description**: Fetching remote resources without validating user-supplied URL
**Attack Scenarios**:
- Port scanning internal services
- Data exfiltration
- Remote file inclusion
- Internal service compromise