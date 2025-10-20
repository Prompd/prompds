# @prompd.io/data-patterns

Data analysis foundation patterns with Excel/CSV processing, statistical analysis, and database query frameworks.

## Features

- **Inherits from**: `@prompd.io/base-patterns@2.1.0`
- **Multi-Format Support**: Excel, CSV, JSON, SQL auto-detection
- **Statistical Analysis**: Descriptive, diagnostic, predictive, prescriptive, exploratory
- **Data Quality**: Missing value handling, outlier detection, consistency checks
- **Excel Processing**: Multi-worksheet, merged cells, charts, pivot tables
- **CSV Processing**: Auto-detect delimiters, encoding, large file handling
- **Database Integration**: SQL result analysis and optimization suggestions

## Usage

### Basic Data Analysis
```bash
prompd run data-patterns.prmd \
  --data_source "sales_data.csv" \
  --analysis_type "descriptive" \
  --statistical_measures '["mean", "median", "std", "correlation"]'
```

### Excel Analysis with Grouping
```bash
prompd run data-patterns.prmd \
  --data_source "financial_report.xlsx" \
  --analysis_type "diagnostic" \
  --grouping_columns '["department", "quarter"]' \
  --null_handling "interpolate"
```

### Inheritance Usage
```yaml
---
name: "@yournamespace/financial-analyzer"
inherits: "@prompd.io/data-patterns@1.0.0"
parameters:
  - name: "fiscal_year"
    type: "integer"
    required: true
---
```

## Parameters

**Inherited from base-patterns:**
- `output_format`, `validation_level`, `context_scope`, `priority_level`, `custom_instructions`

**Data-specific parameters:**
- `data_source`: Path to data file or content (required)
- `analysis_type`: descriptive, diagnostic, predictive, prescriptive, exploratory
- `data_format`: excel, csv, json, sql, auto-detect
- `statistical_measures`: Array of statistical calculations to perform
- `null_handling`: skip, interpolate, zero-fill, error
- `grouping_columns`: Columns for grouped analysis
- `target_columns`: Specific columns to analyze

## Analysis Types

- **Descriptive**: Summary statistics, distributions, quality assessment
- **Diagnostic**: Correlations, trends, anomalies, integrity checks
- **Predictive**: Trend projections, patterns, regression, seasonality
- **Prescriptive**: Recommendations, optimizations, action items
- **Exploratory**: Open-ended exploration, hypothesis generation

## File Processing

### Excel Files
- Multi-worksheet extraction
- Header row identification
- Merged cell handling
- Chart and pivot table processing
- Metadata extraction

### CSV Files
- Auto-detect delimiters and encoding
- Quoted field handling
- Large file optimization
- Date/time format processing

### Database Results
- Query validation
- Result set analysis
- Performance optimization
- Relationship identification

## Sample Data

Includes `sample-data.csv` with product sales data for testing and demonstration purposes.

This package serves as the foundation for all data analysis workflows in the Prompd ecosystem.