# @prompd.io/document-patterns

Document processing foundation for Word, PDF, PowerPoint analysis with content extraction and multi-format processing capabilities.

## Features

- **Inherits from**: `@prompd.io/base-patterns@2.1.0`
- **Multi-Format Support**: Word, PDF, PowerPoint, HTML, RTF, Markdown, Text
- **Content Extraction**: Text, structure, metadata, images, tables
- **Advanced Analysis**: Language detection, sentiment analysis, entity extraction
- **Format Preservation**: Maintain original formatting and structure information
- **OCR Capabilities**: Text extraction from scanned documents and images
- **Table Processing**: Structured data extraction and analysis
- **Media Handling**: Image description and embedded object processing

## Usage

### Basic Document Analysis
```bash
prompd run document-patterns.prmd \
  --document_input "business_report.pdf" \
  --document_type "pdf" \
  --extraction_scope "comprehensive"
```

### Word Document Processing
```bash
prompd run document-patterns.prmd \
  --document_input "contract.docx" \
  --document_type "word" \
  --content_analysis '["structure", "key-content", "entities"]' \
  --table_processing "structured"
```

### PDF with OCR
```bash
prompd run document-patterns.prmd \
  --document_input "scanned_document.pdf" \
  --document_type "pdf" \
  --image_processing "ocr" \
  --extract_media true
```

### PowerPoint Analysis
```bash
prompd run document-patterns.prmd \
  --document_input "presentation.pptx" \
  --document_type "powerpoint" \
  --content_analysis '["structure", "key-content", "images"]' \
  --format_preservation true
```

### Inheritance Usage
```yaml
---
name: "@yournamespace/contract-analyzer"
inherits: "@prompd.io/document-patterns@1.0.0"
parameters:
  - name: "contract_type"
    type: "string"
    enum: ["employment", "service", "nda", "purchase"]
---
```

## Parameters

**Inherited from base-patterns:**
- `output_format`, `validation_level`, `context_scope`, `priority_level`, `custom_instructions`

**Document-specific parameters:**
- `document_input`: Document file path, content, or binary data (required)
- `document_type`: auto-detect, word, pdf, powerpoint, text, markdown, html, rtf
- `extraction_scope`: text-only, structure, metadata, comprehensive, minimal
- `content_analysis`: Array of analysis types to perform
- `format_preservation`: Preserve original formatting information
- `language_detection`: Detect and analyze document language
- `extract_media`: Extract embedded images and media
- `table_processing`: ignore, text, structured, detailed
- `image_processing`: ignore, list, describe, ocr, detailed

## Content Analysis Types

- **Structure**: Document hierarchy, sections, cross-references
- **Key Content**: Summaries, findings, action items, statistics
- **Language**: Primary/secondary languages, terminology, readability
- **Sentiment**: Tone analysis, emotional language, confidence markers
- **Entities**: People, places, organizations, dates, contact info
- **Themes**: Main topics, keyword density, categorization
- **Formatting**: Styles, fonts, colors, layout information
- **Images**: Visual content descriptions and analysis
- **Tables**: Structured data extraction and relationships

## Format-Specific Features

### Microsoft Word (.docx, .doc)
- Styles and template analysis
- Track changes and comments
- Form field extraction
- Embedded object handling

### PDF Documents
- Text layer extraction
- OCR for scanned content
- Form field identification
- Annotation extraction
- Security analysis

### PowerPoint (.pptx, .ppt)
- Slide content and structure
- Speaker notes extraction
- Animation analysis
- Master slide templates
- Multimedia handling

### HTML Documents
- Semantic structure analysis
- Link extraction
- Meta tag information
- CSS analysis

## Processing Options

### Table Processing
- **Ignore**: Skip table content
- **Text**: Convert to readable text
- **Structured**: Extract as CSV/JSON
- **Detailed**: Complete analysis with formatting

### Image Processing
- **Ignore**: Skip image content
- **List**: Enumerate images found
- **Describe**: Generate descriptions
- **OCR**: Extract text from images
- **Detailed**: Comprehensive analysis

## Response Structure

- **Document Summary**: Type, pages, word count, language, dates
- **Structure Analysis**: Hierarchy, sections, cross-references
- **Key Content**: Summaries, main points, action items
- **Content Themes**: Topics, keywords, technical terms
- **Extracted Content**: Full text, tables, images, metadata
- **Quality Assessment**: Organization, readability, accessibility

## Sample Document

Includes `sample-document.md` demonstrating:
- Business document structure
- Tables and financial data
- Technical specifications
- Project planning elements
- Multiple content types and formatting

## Error Handling

- **Corrupted Files**: Partial extraction with issue reporting
- **Password Protection**: Credential requests or status reporting
- **Large Documents**: Chunked processing with progress
- **Unsupported Formats**: Alternative processing suggestions
- **OCR Failures**: Limitation reporting and alternatives

## Integration Capabilities

- Content management systems
- Document classification workflows
- Legal document processing
- Research paper analysis
- Business document automation
- Compliance and audit documentation

This package serves as the foundation for all document processing workflows in the Prompd ecosystem.