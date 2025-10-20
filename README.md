# Prompd Engineering Prompts

## 🎯 Purpose
This is a meta-Prompd project that produces high-quality prompts for our engineering team. By using Prompd to compile prompts for Prompd development, we're dogfooding our own platform while ensuring consistency and quality across all development tasks.

## 🚀 Quick Start

```bash
# Navigate to the project
cd C:\git\github\Logikbug\prompd-engineering-prompts

# Compile a prompt for implementing a new feature
prompd compile code-implementation.prompd \
  --params component_name="Registry Auth Middleware" \
  language="nodejs" \
  security_level="critical"

# Compile a bug fix prompt
prompd compile bug-fix.prompd \
  --params bug_description="Token validation fails intermittently" \
  affected_component="Auth System" \
  severity="high"
```

## 📁 Available Prompts

### 1. Code Implementation (`code-implementation.prompd`)
**Purpose:** Compile precise implementation prompts with security and best practices built-in

**Use Cases:**
- Building new features
- Implementing components
- Creating APIs
- Writing utilities

**Key Features:**
- Language-specific best practices
- Security level configuration (standard/high/critical)
- Testing requirements
- Anti-pattern prevention

### 2. Architecture Review (`architecture-review.prompd`)
**Purpose:** Compile prompts for system design and architecture analysis

**Use Cases:**
- New system design
- Architecture refactoring
- Security reviews
- Performance optimization
- Integration planning

**Key Features:**
- Scale-aware (prototype/production/enterprise)
- Review type selection
- Comprehensive checklists
- Deliverable specifications

### 3. Bug Fix (`bug-fix.prompd`)
**Purpose:** Compile focused debugging and fix prompts

**Use Cases:**
- Critical production issues
- Bug resolution
- Performance problems
- Security vulnerabilities

**Key Features:**
- Severity-based approach
- Root cause analysis focus
- Regression prevention
- Critical issue protocol

### 4. Integration Testing (`integration-testing.prompd`)
**Purpose:** Compile comprehensive testing strategy prompts

**Use Cases:**
- Unit test creation
- Integration testing
- E2E test design
- Performance testing
- Security testing

**Key Features:**
- Coverage targets
- Test scope selection
- CI/CD integration
- Best practices enforcement

### 5. Master Prompt (`master-prompt.prompd`)
**Purpose:** Meta-prompt to help select the right prompt for any task

**Use Cases:**
- Task analysis
- Prompt selection
- Workflow coordination
- Team assignment

## 🔧 Integration with Development Workflow

### For Individual Developers:
1. Identify your task type
2. Select appropriate prompt template
3. Compile prompt with specific parameters
4. Use compiled prompt with Claude instance
5. Implement solution following prompt guidelines

### For Team Coordination:
1. Lead Coordinator identifies tasks from sprint
2. Compile appropriate prompts for each task
3. Assign prompts to team instances
4. Track implementation progress
5. Validate against prompt requirements

## 💡 Best Practices

### DO:
- ✅ Use specific, detailed parameters
- ✅ Chain prompts for complex tasks
- ✅ Include security_level for any user-facing code
- ✅ Set testing_required=true for production code
- ✅ Reference existing code patterns via context_files

### DON'T:
- ❌ Skip security considerations
- ❌ Ignore testing requirements
- ❌ Use generic descriptions
- ❌ Forget to specify language/platform
- ❌ Bypass the architecture review for major changes

## 🔄 Workflow Examples

### Example 1: Implementing a New Registry Endpoint

```bash
# Step 1: Architecture Review
prompd compile architecture-review.prompd \
  --params system_component="Package Versioning API" \
  review_type="new_design" \
  scale_requirements="production"

# Step 2: Implementation
prompd compile code-implementation.prompd \
  --params component_name="Package Versioning API" \
  language="nodejs" \
  security_level="high" \
  context_files='["registry/routes/packages.js", "registry/models/package.js"]'

# Step 3: Testing
prompd compile integration-testing.prompd \
  --params test_scope="integration" \
  component="Package Versioning API" \
  coverage_target=85
```

### Example 2: Critical Bug Fix

```bash
# Compile comprehensive bug fix prompt
prompd compile bug-fix.prompd \
  --params bug_description="Memory leak in package validation causing server crashes" \
  affected_component="Package Validator" \
  severity="critical" \
  error_message="FATAL ERROR: Reached heap limit Allocation failed"
```

## 📊 Prompt Parameter Reference

### Common Parameters Across All Prompts:
- `component_name` / `system_component` / `affected_component`: The specific part being worked on
- `severity` / `security_level`: Importance and security requirements
- `test_scope` / `testing_required`: Testing expectations

### Security Levels:
- `standard`: Basic security practices
- `high`: Enhanced security with validation
- `critical`: Maximum security, includes audit logging, rate limiting

### Scale Requirements:
- `prototype`: Proof of concept, local development
- `production`: 1000+ users, high availability
- `enterprise`: 10,000+ users, multi-region, 99.9% SLA

## 🚀 Advanced Usage

### Parameterized Bulk Compilation
Create a params file for repeated use:

```json
// registry-params.json
{
  "language": "nodejs",
  "security_level": "high",
  "testing_required": true,
  "context_files": ["registry/server.js", "registry/auth.js"]
}
```

```bash
prompd compile code-implementation.prompd --params-file registry-params.json \
  --params component_name="Rate Limiter Middleware"
```

### Custom Templates
Extend existing prompts for specific needs:

```yaml
---
extends: code-implementation
id: cli-command-implementation
name: CLI Command Implementation
parameters:
  - name: command_name
    type: string
    required: true
  - name: cli_platform
    type: string
    enum: [python, go, nodejs]
    required: true
---

# Additional CLI-specific requirements...
```

## 🎯 Success Metrics

Track the effectiveness of prompts by measuring:
- Implementation speed
- Bug density
- Security issue frequency
- Test coverage achieved
- Code review iterations needed

## 🔮 Future Enhancements

- [ ] AI-powered prompt parameter suggestion
- [ ] Historical prompt effectiveness tracking
- [ ] Team-specific prompt customization
- [ ] Automated prompt chaining for workflows
- [ ] Integration with CI/CD for automated prompt generation

## 📚 Related Documentation

- [Prompd CLI Documentation](../prompd-cli/docs/CLI.md)
- [Format Specification](../prompd-cli/docs/FORMAT.md)
- [Team Coordination Guide](../CLAUDE.md)
- [Architecture Vision](../PROMPD-VISION.md)

---

*Remember: We're building the operating system for the AI internet. Every prompt, every line of code, every decision matters. Use these prompts to maintain the highest standards.*
