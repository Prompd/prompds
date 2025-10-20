# Composable Prompt Architecture v2.0

> **NEXT CRITICAL**: This is the revolutionary architecture that makes Prompd the first truly composable AI prompt system

## Core Innovation

We've designed the **npm for AI prompts** - a complete composable architecture that enables:
- Package-based distribution with semantic versioning
- Inheritance and composition patterns
- Universal compilation to any AI provider
- Import/alias system for clean references
- Standardized package structure

## 1. Package Structure Standard

Every package follows a standardized folder structure:

```
@prompd.io/security-toolkit@2.0.0/
├── manifest.json              # Package metadata, dependencies, versions
├── prompts/                   # Main executable prompts (.prompd files)
├── contexts/                  # Environmental/background data (any format)
├── systems/                   # Core AI behavior instructions (.md/.txt)
├── assistants/                # Specialized AI roles/personas (.md/.txt)
├── tasks/                     # Specific operations to perform (.prompd)
├── workflows/                 # Multi-step processes (.pdflow files)
├── responses/                 # Response formatting/style guides (.md/.txt)
├── outputs/                   # Output structure templates (.md/.txt)
├── examples/                  # Few-shot examples (any format)
├── chains/                    # Chain-of-thought reasoning patterns (.md/.txt)
├── templates/                 # Reusable prompt templates (.prompd)
├── patterns/                  # Common prompt patterns (.md/.txt)
├── schemas/                   # Structured data definitions (.json/.yaml)
└── docs/                      # Usage documentation (.md)
```

## 2. Namespace & Versioning System

### Registry Namespaces
```yaml
# Official Prompd packages
@prompd.io/security-audit@2.0.0
@prompd.io/data-analysis@1.5.0

# Third-party official packages  
@microsoft.com/azure-patterns@2.1.0
@openai.com/function-calling@1.3.0

# User/organization packages
@username/custom-tools@1.0.0
```

### Multi-level Namespacing
Domain-based ownership with semantic versioning:
- **Domain**: Controls the namespace (`@prompd.io`, `@microsoft.com`)
- **Package**: The actual component (`security-audit`, `azure-patterns`)
- **Version**: Semantic versioning (`@2.0.0`, `@1.5.0`)

## 3. Import & Alias System

Clean reference system to avoid verbose namespace paths:

```yaml
---
id: advanced-security-audit
using: @prompd.io/security-toolkit@2.0.0
  prefix: security
using: @microsoft.com/azure-enterprise@1.5.0  
  prefix: azure

context:
  - @security/contexts/nodejs-app
  - @azure/contexts/enterprise-config

inherits: @security/prompts/base-audit
systems: @azure/systems/cloud-architect
---
```

### Package Reference Resolution
When a package is referenced without version, `@latest` is assumed:
```yaml
using: @prompd.io/security-toolkit  # Resolves to @latest
using: @prompd.io/security-toolkit@2.0.0  # Specific version
using: @prompd.io/security-toolkit@^2.0.0  # Semver range
```

## 4. Inheritance & Override System

Complete inheritance with surgical overrides:

```yaml
---
id: fintech-security-audit
inherits: @prompd.io/security-audit@2.0.0
context:
  - @prompd.io/fintech-context@1.2.0
overrides:
  system: "You are a PCI-DSS compliance expert auditing financial systems."
  parameters:
    - name: compliance_requirements
      default: ["PCI-DSS", "SOX", "FFIEC"]
  content:
    pre_analysis: |
      ## Regulatory Context
      Financial services require strict data protection...
    post_analysis: |
      {{{ parent.content }}}
      
      ## Financial Services Specific Requirements
      - Card data encryption verification
      - Transaction integrity audit
---
```

## 5. Context Composition System

Reusable context patterns across packages:

### Context File Declaration Methods

#### Method 1: CLI Context Files
```bash
prompd run @security/audit@2.0.0 \
  --meta:context ./src/auth.js \
  --meta:context ./config/database.yml \
  --meta:context ./package.json
```

#### Method 2: Header-Declared Context Files
```yaml
---
id: schema-analysis
context: [schema.sql, migrations/, seed-data.sql]
parameters:
  # ... parameters
---
```

### Text-Based Contexts
```
contexts/
├── nodejs-app.md          # Application context description
├── security-checklist.txt # Background information
└── compliance-reqs.md     # Regulatory requirements
```

### Binary File Support
```
contexts/
├── financial-data.xlsx    # Excel spreadsheets → CSV extraction
├── requirements.docx      # Word documents → text extraction  
├── architecture.png       # Images → vision API or description
├── config.json           # JSON → structured data injection
└── schema.yaml           # YAML → parsed configuration
```

## 6. Compilation System Architecture

### Two Compilation Targets

#### Default: Markdown Compiler
```bash
prompd compile @security/audit@2.0.0 -p target:"webapp"
# Outputs: Human-readable markdown with all contexts assembled
```

#### API: Provider-JSON Compiler
```bash  
prompd run @security/audit@2.0.0 -p target:"webapp" --provider anthropic --model claude-3-sonnet
# Behind scenes: Compiles to provider-specific JSON
```

### Compilation Pipeline

1. **Dependency Resolution**
   - Parse `using:` imports and versions
   - Resolve `inherits:` chains
   - Check for circular dependencies

2. **Asset Extraction**
   - Convert `.xlsx` → CSV tables
   - Extract `.docx` → plain text
   - Process `.pdf` → OCR text
   - Parse `.json/.yaml` → structured data

3. **Content Assembly**
   - Inject contexts from multiple sources
   - Merge inherited content with overrides
   - Apply few-shot examples and chains
   - Process parameter substitutions

4. **Target Generation**
   - **Markdown**: Human-readable debug format
   - **Provider JSON**: API-specific format (OpenAI, Anthropic, Google)

### Provider Schema System

```typescript
const providerSchemas = {
  "openai": {
    "gpt-4": { 
      model: "gpt-4", 
      messages: [{ role: "system", content: "..." }],
      temperature: 0.1 
    }
  },
  "anthropic": {
    "claude-3-sonnet": {
      model: "claude-3-sonnet-20240229",
      system: "...",
      messages: [{ role: "user", content: "..." }]
    }
  }
}
```

## 7. Command Interface

### Core Commands

```bash
# Compile to markdown (debug/review)
prompd compile @security/audit@2.0.0 -p target:"webapp" --output audit.md

# Execute against API  
prompd run @security/audit@2.0.0 -p target:"webapp" --provider anthropic --model claude-3-sonnet

# Compile to specific provider format
prompd compile @security/audit@2.0.0 -p target:"webapp" --to-provider-json anthropic --output api-call.json
```

### Extensible `--to` Parameter System (Output Formatters)

The `--to` parameter is a **pluggable formatter system** that can target any output format:

#### Core Formatters
```bash
# Default: Markdown (human-readable)
prompd compile @security/audit@2.0.0 --to-markdown --output review.md

# API Provider JSON formats
prompd compile @security/audit@2.0.0 --to-provider-json:anthropic --output claude.json
prompd compile @security/audit@2.0.0 --to-provider-json:openai --output gpt4.json
prompd compile @security/audit@2.0.0 --to-provider-json:google --output gemini.json

# Document formats
prompd compile @security/audit@2.0.0 --to-html --output report.html
prompd compile @security/audit@2.0.0 --to-pdf --output report.pdf
prompd compile @security/audit@2.0.0 --to-docx --output report.docx
```

#### Development Formatters
```bash
# API testing formats
prompd compile @security/audit@2.0.0 --to-curl-command --output test.sh
prompd compile @security/audit@2.0.0 --to-postman-collection --output tests.json
prompd compile @security/audit@2.0.0 --to-insomnia --output insomnia.json

# Integration formats
prompd compile @security/audit@2.0.0 --to-swagger-spec --output api.yaml
prompd compile @security/audit@2.0.0 --to-openapi --output openapi.json
prompd compile @security/audit@2.0.0 --to-graphql-schema --output schema.graphql
```

#### Future Extensibility
```bash
# Framework integrations
prompd compile @security/audit@2.0.0 --to-langchain-chain --output chain.py
prompd compile @security/audit@2.0.0 --to-langsmith-dataset --output dataset.json
prompd compile @security/audit@2.0.0 --to-prompt-flow --output azure-flow.json

# Deployment formats
prompd compile @security/audit@2.0.0 --to-lambda-function --output lambda.zip
prompd compile @security/audit@2.0.0 --to-edge-function --output worker.js
prompd compile @security/audit@2.0.0 --to-docker-compose --output docker-compose.yml

# UI components
prompd compile @security/audit@2.0.0 --to-react-component --output PromptUI.tsx
prompd compile @security/audit@2.0.0 --to-gradio-app --output app.py
prompd compile @security/audit@2.0.0 --to-streamlit --output dashboard.py
```

#### Formatter Plugin Architecture
```typescript
interface OutputFormatter {
  name: string
  format(compiled: CompiledPrompt): string | Buffer
  fileExtension: string
  mimeType: string
}

// Register new formatters
compiler.registerFormatter('my-format', new MyCustomFormatter())

// Use custom formatter
prompd compile @prompt@1.0.0 --to-my-format --output custom.out
```

This extensible system makes Prompd the **universal compiler for AI workflows** - one source template can target infinite output formats!

### Parameter System
```bash
# Short form parameters
prompd run @tools/converter@1.0.0 -p file:"data.csv" -p format:"json"

# Context files via CLI
prompd run @audit/security@2.0.0 --meta:context ./src/auth.js --meta:context ./config.yml

# Output control
prompd compile @tools/report@1.0.0 -p data:"sales.csv" --output report.md
prompd compile @tools/report@1.0.0 -p data:"sales.csv" -o report.md  # short form
```

## 8. File Format Support

### Text Extraction Pipeline
- **Excel (.xlsx)** → Tabular data extraction
- **Word (.docx)** → Plain text + formatting preservation
- **PDF (.pdf)** → OCR text extraction + table detection
- **PowerPoint (.pptx)** → Slide text + image descriptions
- **Images (.png/.jpg)** → Vision API analysis or alt-text
- **Code files (.js/.py/.sql)** → Syntax-aware inclusion
- **Config files (.json/.yaml/.env)** → Structured data parsing

### Context Injection Examples
```yaml
contexts:
  - @security/contexts/nodejs-patterns    # .md file
  - ./financial-data.xlsx                 # Excel → CSV extraction
  - ./requirements.docx                   # Word → text extraction
  - ./api-schema.json                     # JSON → structured injection
```

## 9. Network Effects & Ecosystem

### Composability Chain Reaction
1. **Base Templates** → Community creates specialized versions
2. **Context Libraries** → Reusable across thousands of prompts  
3. **Industry Overrides** → Compliance/regulatory variations
4. **Personal Customizations** → Individual workflow preferences

### Examples of Ecosystem Growth
```yaml
# Base prompt
@prompd.io/security-audit@1.0.0

# Industry specializations  
@fintech/pci-security-audit@1.0.0 inherits: @prompd.io/security-audit@1.0.0
@healthcare/hipaa-audit@1.0.0 inherits: @prompd.io/security-audit@1.0.0

# Company customizations
@mycompany/security-audit@1.0.0 inherits: @fintech/pci-security-audit@1.0.0
```

## 10. Revolutionary Impact

### What Makes This Different
This isn't just "better prompt storage" - it's **component architecture for AI**:

- **Composable**: Every prompt can inherit, extend, override
- **Versioned**: Complete dependency management like npm
- **Universal**: Compiles to any AI provider format
- **Extensible**: Plugin architecture for new providers/formats
- **Standardized**: Common folder structure and patterns

### Competitive Advantage
**No existing solution has:**
- ❌ Package-based inheritance system
- ❌ Multi-format context composition  
- ❌ Universal compilation pipeline
- ❌ Import/alias system for clean references
- ❌ Standardized package structure
- ❌ Complete development ecosystem (CLI + IDE + Registry)

### Network Effects
Every component becomes more valuable when it can be:
- **Inherited** by specialized versions
- **Composed** with complementary contexts
- **Extended** with custom overrides
- **Shared** across the ecosystem

This creates the **GitHub/npm for AI** - where every prompt becomes a building block for more sophisticated systems.

## 11. Advanced Compiler Architecture

### Pipeline-Based Architecture (Extensible & Maintainable)

```typescript
interface CompilerPipeline {
  stages: CompilerStage[]
  execute(input: PrompdSource): CompilationResult
}

abstract class CompilerStage {
  abstract process(context: CompilationContext): void
  abstract getName(): string
}

class PrompdCompiler {
  constructor() {
    this.pipeline = new CompilerPipeline([
      new LexicalAnalysisStage(),      // Parse YAML + Handlebars + Markdown
      new DependencyResolutionStage(),  // Resolve using: and inherits:
      new SemanticAnalysisStage(),      // Validate parameters and references
      new AssetExtractionStage(),       // Extract binary files to text
      new TemplateProcessingStage(),    // Process Handlebars templates
      new CodeGenerationStage(),        // Generate target format
    ])
  }
}
```

### Cross-Platform Implementation

#### Python Implementation
```python
class CompilerStage(ABC):
    @abstractmethod
    def process(self, ctx: CompilationContext) -> None:
        pass

class PrompdCompiler:
    def __init__(self):
        self.pipeline = CompilerPipeline([
            LexicalAnalysisStage(),
            DependencyResolutionStage(),
            # ... additional stages
        ])
```

#### Go Implementation
```go
type CompilerStage interface {
    Process(ctx *CompilationContext) error
    GetName() string
}

type PrompdCompiler struct {
    pipeline *CompilerPipeline
}
```

## 12. Compiler-IDE Integration

### Language Server Protocol (LSP) Architecture

The IDE needs a **Prompd Language Server** for real-time development experience:

```typescript
interface PrompdLanguageServer {
  // Parse .prompd files with YAML + Handlebars-like + Markdown
  parseDocument(uri: string): PrompdDocument
  
  // Resolve dependency chains in real-time
  resolveDependencies(document: PrompdDocument): DependencyGraph
  
  // Live compilation preview without full execution
  compilePreview(document: PrompdDocument): CompilationResult
  
  // IntelliSense support
  provideCompletions(position: Position): CompletionItem[]
  provideHover(position: Position): HoverInfo
  provideDiagnostics(document: PrompdDocument): Diagnostic[]
}
```

### Multi-Language Syntax Highlighting

Single `.prompd` file contains multiple languages:

```yaml
---
# YAML syntax highlighting for frontmatter
using: @prompd.io/security@2.0.0
  prefix: security
parameters:
  - name: target
    type: string
---

# Markdown + Template syntax highlighting
# Security Analysis: {{target}}

> Context: @security/contexts/{{framework}}

## Analysis Results  
{{{ parent.content }}}

```sql
-- SQL syntax highlighting in code blocks
SELECT * FROM vulnerabilities WHERE severity = 'CRITICAL'
```
```

### IntelliSense Features

**Package Autocomplete:**
```yaml
using: @prompd.io/secu|  # IDE suggests: security-audit@2.0.0, security-toolkit@1.5.0
```

**Path Completion:**  
```yaml
context: @security/cont|  # IDE suggests: contexts/, then specific files
```

**Parameter IntelliSense:**
```yaml
# IDE knows inherited parameters from parent prompts
{{target}}  # Autocomplete shows: target, framework, compliance_level
```

### Real-Time Error Detection

```yaml
---
using: @prompd.io/nonexistent@1.0.0  # ❌ Package not found
  prefix: missing

inherits: @missing/prompts/audit      # ❌ Circular dependency detected  
context: @missing/contexts/invalid    # ❌ Context file doesn't exist
---

# {{unknown_param}}                   # ❌ Parameter not defined
```

### Live Compilation Preview

**IDE Layout:**
- **Left Pane**: Source `.prompd` file with syntax highlighting
- **Right Pane**: Live-compiled markdown preview  
- **Bottom Panel**: Compilation errors and warnings
- **Side Panel**: Dependencies tree and parameter overrides

### Template Syntax Processing

Uses Handlebars-like syntax for familiar developer experience:
- `{{variable}}` - Parameter substitution
- `{{{ parent.content }}}` - Unescaped inheritance content
- `{{#if condition}}...{{/if}}` - Conditional blocks
- `{{#each array}}...{{/each}}` - Loop constructs

## 13. Security & Package Trust

### Package Signing & Verification
- Packages signed with publisher's key
- Registry verifies signatures on upload
- CLI verifies signatures on install
- Checksum validation for integrity

### Namespace Ownership
- Domain-based verification (like npm scope ownership)
- Reserved namespaces for official packages
- Organization verification for enterprise namespaces

## 14. Versioning & Dependency Resolution

### Semantic Versioning
```yaml
using: @prompd.io/security@2.0.0     # Exact version
using: @prompd.io/security@^2.0.0    # Compatible with 2.x.x
using: @prompd.io/security@~2.0.0    # Compatible with 2.0.x
using: @prompd.io/security@latest    # Latest stable version
```

### Dependency Conflict Resolution
- Follows npm-style resolution algorithm
- Warns on incompatible peer dependencies
- Lockfile support for reproducible builds

## 15. Implementation Roadmap

### Phase 1: Core Compilation Pipeline
- [ ] Basic YAML + Markdown parsing
- [ ] Parameter substitution
- [ ] Markdown output formatter
- [ ] Provider JSON formatters (OpenAI, Anthropic)

### Phase 2: Package Management
- [ ] Registry package upload/download
- [ ] Namespace reservation system
- [ ] Package versioning and search
- [ ] README.md rendering on registry

### Phase 3: Advanced Features
- [ ] Full inheritance system
- [ ] Context composition with file extraction
- [ ] Import/alias resolution
- [ ] Language Server Protocol for IDE

### Phase 4: Ecosystem Growth
- [ ] Plugin architecture for formatters
- [ ] Community package guidelines
- [ ] Enterprise features (private registries)
- [ ] Integration with existing tools (LangChain, etc.)

---

**Status**: This architecture is ready for implementation. The Core Engine team needs to build the compilation pipeline, Registry team needs the package management system, and IDE team needs the Language Server Protocol implementation for syntax highlighting and IntelliSense support.

This is the foundation that transforms Prompd from a prompt tool into the **operating system for composable AI workflows**.

**Industry Impact**: When major players like LangChain adopt this as their prompt infrastructure, it becomes the de facto standard for AI prompt engineering.