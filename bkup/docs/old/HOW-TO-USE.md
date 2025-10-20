# How to Use Engineering Prompts

## Quick Start Guide

### 1. Run a Prompt with Parameters

```bash
# Basic usage - specify parameters inline
prompd compile real-world-prompts/api-integration/rest-endpoint-builder.prompd \
  --params endpoint_name="Order Management API" \
  resource_name="order" \
  framework="express" \
  database="postgresql"

# Using a params file (recommended)
prompd compile real-world-prompts/api-integration/rest-endpoint-builder.prompd \
  --params-file real-world-prompts/api-integration/params/saas-api.json
```

### 2. Run a Workflow

```bash
# Compile the complete engineering workflow
prompd compile pdflows/engineering-workflow.pdflow \
  --params feature_name="User Authentication System" \
  language="nodejs" \
  security_level="critical"
```

### 3. Run with Context Files

Context files allow prompts to analyze your existing code, documentation, and data files.

#### Method 1: CLI Context Files
```bash
# Pass context files via command line
prompd run real-world-prompts/security/owasp-security-audit.prompd \
  --params-file security-params.json \
  --meta:context ./src/auth.js \
  --meta:context ./config/database.yml \
  --meta:context ./package.json
```

#### Method 2: Header-Declared Context Files
For prompts that always expect specific files, declare them in the header:

```yaml
---
id: schema-analysis
name: Database Schema Analysis
context: [schema.sql, migrations/, seed-data.sql]
parameters:
  # ... your parameters
---
```

Then run normally - the prompt will automatically look for those files:
```bash
prompd run real-world-prompts/database/schema-analysis.prompd --params-file db-params.json
```

### 4. Chain Multiple Prompts

```bash
# Step 1: Architecture review
prompd compile real-world-prompts/api-integration/rest-endpoint-builder.prompd \
  --params-file api-params.json > architecture-output.md

# Step 2: Compile implementation based on architecture
prompd compile real-world-prompts/security/owasp-security-audit.prompd \
  --params application_type="api" \
  technology_stack="Node.js + Express + PostgreSQL"
```

---

## Available Prompt Categories

### 🔗 API Integration (`real-world-prompts/api-integration/`)
**REST Endpoint Builder** - Complete REST API with validation and security
```bash
prompd compile real-world-prompts/api-integration/rest-endpoint-builder.prompd \
  --params-file real-world-prompts/api-integration/params/saas-api.json
```

**GraphQL Schema Builder** - GraphQL APIs with resolvers and subscriptions
```bash
prompd compile real-world-prompts/api-integration/graphql-schema-builder.prompd \
  --params-file real-world-prompts/api-integration/params/ecommerce-graphql.json
```

### 🔐 Security (`real-world-prompts/security/`)
**OWASP Security Audit** - Comprehensive security assessment
```bash
prompd compile real-world-prompts/security/owasp-security-audit.prompd \
  --params application_type="web-app" \
  technology_stack="React + Node.js + PostgreSQL" \
  audit_scope="comprehensive"
```

### 🗄️ Database (`real-world-prompts/database/`)
**Schema Migration Builder** - Safe database migrations with rollback
```bash
prompd compile real-world-prompts/database/schema-migration-builder.prompd \
  --params migration_name="Add user preferences table" \
  database_type="postgresql" \
  migration_type="create_table" \
  environment="production"
```

### 📊 Data Science (`real-world-prompts/data-science/`)
**ML Pipeline Builder** - End-to-end machine learning pipeline
```bash
prompd compile real-world-prompts/data-science/ml-pipeline-builder.prompd \
  --params-file real-world-prompts/data-science/params/customer-churn-ml.json
```

**EDA Analysis Builder** - Comprehensive exploratory data analysis
```bash
prompd compile real-world-prompts/data-science/eda-analysis-builder.prompd \
  --params dataset_name="Customer Purchase Data" \
  analysis_focus="ml-preparation" \
  data_type="tabular" \
  target_variable="churn_flag"
```

### 💰 Finance (`real-world-prompts/finance/`)
**Financial Model Builder** - DCF, LBO, and financial forecasting models
```bash
prompd compile real-world-prompts/finance/financial-model-builder.prompd \
  --params-file real-world-prompts/finance/params/startup-dcf.json
```

### 📈 Marketing (`real-world-prompts/marketing/`)
**Campaign Analysis Builder** - Marketing attribution and ROI optimization
```bash
prompd compile real-world-prompts/marketing/campaign-analysis-builder.prompd \
  --params-file real-world-prompts/marketing/params/saas-campaign.json
```

---

## Pre-configured Parameter Files

### Common Configurations Available

#### API Integration
- `saas-api.json` - SaaS user management API
- `ecommerce-graphql.json` - E-commerce GraphQL API

#### Data Science  
- `customer-churn-ml.json` - Customer churn classification
- `sales-forecasting.json` - Time series forecasting
- `recommendation-system.json` - Collaborative filtering

#### Finance
- `startup-dcf.json` - Startup DCF valuation
- `growth-lbo.json` - Growth company LBO model
- `budget-forecast.json` - Annual budget planning

#### Marketing
- `saas-campaign.json` - B2B SaaS digital campaigns
- `ecommerce-attribution.json` - E-commerce attribution analysis

### Creating Custom Parameter Files

```json
{
  "parameter_name": "value",
  "required_param": "must_provide_value",
  "optional_param": "default_if_not_specified",
  "boolean_param": true,
  "array_param": ["option1", "option2", "option3"]
}
```

---

## Advanced Usage Patterns

### 1. Batch Processing Multiple Prompts

```bash
#!/bin/bash
# compile-api-suite.sh

# Compile REST API
prompd compile real-world-prompts/api-integration/rest-endpoint-builder.prompd \
  --params-file api-params.json > rest-api-implementation.md

# Compile GraphQL API  
prompd compile real-world-prompts/api-integration/graphql-schema-builder.prompd \
  --params-file graphql-params.json > graphql-implementation.md

# Compile Security Audit
prompd compile real-world-prompts/security/owasp-security-audit.prompd \
  --params application_type="api" \
  technology_stack="Node.js + GraphQL + PostgreSQL" > security-audit.md

echo "API suite compiled successfully!"
```

### 2. Environment-Specific Parameters

```bash
# Development environment
prompd compile real-world-prompts/database/schema-migration-builder.prompd \
  --params-file migration-params.json \
  --params environment="development" \
  requires_downtime=false

# Production environment  
prompd compile real-world-prompts/database/schema-migration-builder.prompd \
  --params-file migration-params.json \
  --params environment="production" \
  requires_downtime=true \
  is_destructive=false
```

### 3. Parameterized Workflows

```bash
# Complete feature development workflow
prompd compile pdflows/engineering-workflow.pdflow \
  --params feature_name="Payment Processing System" \
  language="nodejs" \
  security_level="critical" \
  scale_requirements="enterprise" \
  context_files='["payment-gateway.js", "transaction-model.js"]'
```

---

## Integration with Development Tools

### VS Code Integration
If using the Prompd IDE extension:

1. Open `.pdproj` file in Prompd IDE
2. Right-click on prompt file
3. Select "Compile with Parameters"
4. Fill in parameter form or select params file
5. Compiled output opens in new editor tab

### CLI Integration in Scripts

```bash
# Make executable
chmod +x compile-suite.sh

# Use in CI/CD pipeline
./compile-suite.sh

# Integrate with make
make api-docs:
	prompd compile api-docs.prompd --params-file production.json > docs/api.md
```

### Git Hooks Integration

```bash
# .git/hooks/pre-commit
#!/bin/bash

# Recompile API documentation on commit
if git diff --cached --name-only | grep -q "api/"; then
    prompd compile real-world-prompts/api-integration/rest-endpoint-builder.prompd \
      --params-file current-api-params.json > docs/api-spec.md
    git add docs/api-spec.md
fi
```

---

## Troubleshooting

### Common Issues

**"File not found" error:**
```bash
# Ensure you're in the project root
cd /path/to/prompd-engineering-prompts

# Use absolute paths if needed
prompd compile $(pwd)/real-world-prompts/api-integration/rest-endpoint-builder.prompd
```

**"Invalid parameter" error:**
```bash
# Check parameter names match the prompt definition
prompd validate real-world-prompts/api-integration/rest-endpoint-builder.prompd

# Verify params file format
cat real-world-prompts/api-integration/params/saas-api.json | jq '.'
```

**"Validation failed" error:**
Wait for Core Engine Team to fix the validator metadata bug (they're working on it).

### Getting Help

```bash
# List available parameters
prompd show real-world-prompts/api-integration/rest-endpoint-builder.prompd

# Validate prompt file
prompd validate real-world-prompts/api-integration/rest-endpoint-builder.prompd

# General help
prompd --help
```

---

## Best Practices

### 1. Parameter Organization
- Use descriptive parameter file names
- Group related parameters together
- Version parameter files for different environments

### 2. Output Management
```bash
# Create organized output structure
mkdir -p generated/{api,security,database}

prompd compile api-prompt.prompd --params-file params.json > generated/api/implementation.md
```

### 3. Documentation
- Document custom parameter combinations
- Keep examples of successful parameter files
- Track which prompts work well together

### 4. Version Control
```gitignore
# .gitignore
generated/
*.output.md
temp-params.json
```

But do commit:
```bash
# Keep in version control
real-world-prompts/
params/
HOW-TO-USE.md
```

---

## Examples by Use Case

### Building a New SaaS Feature
```bash
# 1. Architecture planning
prompd compile real-world-prompts/api-integration/rest-endpoint-builder.prompd \
  --params endpoint_name="Subscription Management" \
  resource_name="subscription" framework="express" database="postgresql"

# 2. Security review
prompd compile real-world-prompts/security/owasp-security-audit.prompd \
  --params application_type="api" technology_stack="Node.js + Express"

# 3. Database migration
prompd compile real-world-prompts/database/schema-migration-builder.prompd \
  --params migration_name="Add subscription tables" database_type="postgresql"
```

### Data Science Project
```bash
# 1. Exploratory analysis
prompd compile real-world-prompts/data-science/eda-analysis-builder.prompd \
  --params dataset_name="User Behavior Data" analysis_focus="ml-preparation"

# 2. ML pipeline
prompd compile real-world-prompts/data-science/ml-pipeline-builder.prompd \
  --params problem_type="classification" framework="scikit-learn"
```

### Financial Planning
```bash
# 1. Build financial model
prompd compile real-world-prompts/finance/financial-model-builder.prompd \
  --params model_type="dcf" company_stage="growth" industry="SaaS"

# 2. Marketing budget analysis
prompd compile real-world-prompts/marketing/campaign-analysis-builder.prompd \
  --params campaign_type="digital-ads" business_model="b2b-saas"
```

---

Remember: These prompts are designed to work together. Chain them for comprehensive project coverage!
