# Test Results: @prompd.io\data-science-toolkit@1.0.0\prompts\ml-pipeline-builder.prmd

**Source File:** `..\prompd-base\production\@prompd.io\data-science-toolkit@1.0.0\prompts\ml-pipeline-builder.prmd`

**Test Date:** 2025-09-12 21:14:33

## Execution Results

- **Status:** PASS

### LLM Response

```
Warning: Failed to resolve inheritance @prompd.io/core-patterns@2.0.0/templates/implementation-framework.prompd: 1 validation error for PackageReference
version
  Value error, Package version must be 1-20 characters [type=value_error, input_value='2.0.0/templates/implementation-framework.prompd', input_type=str]
    For further information visit https://errors.pydantic.dev/2.11/v/value_error
Warning: Required parameter 'problem_type' not provided
Warning: Required parameter 'data_source' not provided
Warning: Required parameter 'deployment_target' not provided
+---------------------------------- Response from anthropic/claude-3-haiku-20240307 -----------------------------------+
| Here is a comprehensive ML pipeline development project specification for the express framework:                     |
|                                                                                                                      |
| # Express ML Pipeline Development                                                                                    |
|                                                                                                                      |
| ## Project Specification                                                                                             |
| - **Problem Type**: {{problem_type}}                                                                                 |
| - **Framework**: express                                                                                             |
| - **Data Source**: {{data_source}}                                                                                   |
| - **Deployment**: {{deployment_target}}                                                                              |
| - **Data Size**: medium                                                                                              |
| {{#if performance_target}}                                                                                           |
| - **Performance Target**: {{performance_target}}                                                                     |
| {{/if}}                                                                                                              |
|                                                                                                                      |
| Following {{imports.context.ml-best-practices}} for enterprise-grade implementation.                                 |
|                                                                                                                      |
| ## Phase 1: Data Understanding & Preparation                                                                         |
|                                                                                                                      |
| ### Data Ingestion Strategy for {{data_source}}                                                                      |
|                                                                                                                      |
| {{#switch data_source}}                                                                                              |
| {{#case "csv"}}                                                                                                      |
| ```python                                                                                                            |
| import pandas as pd                                                                                                  |
| import numpy as np                                                                                                   |
| from pathlib import Path                                                                                             |
|                                                                                                                      |
| class DataIngester:                                                                                                  |
|     def __init__(self, data_path: str):                                                                              |
|         self.data_path = Path(data_path)                                                                             |
|                                                                                                                      |
|     def load_data(self) -> pd.DataFrame:                                                                             |
|         """Load and validate CSV data"""                                                                             |
|         df = pd.read_csv(self.data_path)                                                                             |
|                                                                                                                      |
|         # Data quality checks                                                                                        |
|         print(f"Dataset shape: {df.shape}")                                                                          |
|         print(f"Missing values: {df.isnull().sum().sum()}")                                                          |
|         print(f"Duplicates: {df.duplicated().sum()}")                                                                |
|                                                                                                                      |
|         return df                                                                                                    |
|                                                                                                                      |
|     def data_quality_report(self, df: pd.DataFrame) -> dict:                                                         |
|         """Generate data quality assessment"""                                                                       |
|         return {                                                                                                     |
|             'completeness': 1 - df.isnull().sum() / len(df),                                                         |
|             'uniqueness': df.nunique() / len(df),                                                                    |
|             'data_types': df.dtypes.to_dict()                                                                        |
|         }                                                                                                            |
| ```                                                                                                                  |
| {{/case}}                                                                                                            |
| {{#case "database"}}                                                                                                 |
| ```python                                                                                                            |
| import sqlalchemy as sa                                                                                              |
| import pandas as pd                                                                                                  |
| from typing import Optional                                                                                          |
|                                                                                                                      |
| class DatabaseIngester:                                                                                              |
|     def __init__(self, connection_string: str):                                                                      |
|         self.engine = sa.create_engine(connection_string)                                                            |
|                                                                                                                      |
|     def load_data(self, query: str, chunksize: Optional = None) -> pd.DataFrame:                                     |
|         """Load data from database with optional chunking"""                                                         |
|         if chunksize and self.data_size in ['large', 'big-data']:                                                    |
|             return pd.read_sql(query, self.engine, chunksize=chunksize)                                              |
|         else:                                                                                                        |
|             return pd.read_sql(query, self.engine)                                                                   |
|                                                                                                                      |
|     def get_table_stats(self, table_name: str) -> dict:                                                              |
|         """Get basic statistics about table"""                                                                       |
|         query = f"""                                                                                                 |
|         SELECT                                                                                                       |
|             COUNT(*) as row_count,                                                                                   |
|             COUNT(DISTINCT *) as unique_rows                                                                         |
|         FROM {table_name}                                                                                            |
|         """                                                                                                          |
|         return pd.read_sql(query, self.engine).iloc[0].to_dict()                                                     |
| ```                                                                                                                  |
| {{/case}}                                                                                                            |
| {{/switch}}                                                                                                          |
|                                                                                                                      |
| ### Feature Engineering Pipeline                                                                                     |
|                                                                                                                      |
| Following {{imports.context.ml-best-practices}}, implement comprehensive feature processing:                         |
|                                                                                                                      |
| ```python                                                                                                            |
| from sklearn.pipeline import Pipeline                                                                                |
| from sklearn.compose import ColumnTransformer                                                                        |
| from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder                                        |
| from sklearn.impute import SimpleImputer                                                                             |
|                                                                                                                      |
| class FeatureProcessor:                                                                                              |
|     def __init__(self, problem_type: str = "{{problem_type}}"):                                                      |
|         self.problem_type = problem_type                                                                             |
|         self.preprocessor = None                                                                                     |
|                                                                                                                      |
|     def create_preprocessor(self, X: pd.DataFrame) -> ColumnTransformer:                                             |
|         """Create preprocessing pipeline based on data types"""                                                      |
|                                                                                                                      |
|         # Identify column types                                                                                      |
|         numeric_features = X.select_dtypes(include=['int64', 'float64']).columns                                     |
|         categorical_features = X.select_dtypes(include=['object']).columns                                           |
|                                                                                                                      |
|         # Numeric pipeline                                                                                           |
|         numeric_pipeline = Pipeline([                                                                                |
|             ('imputer', SimpleImputer(strategy='median')),                                                           |
|             ('scaler', StandardScaler())                                                                             |
|         ])                                                                                                           |
|                                                                                                                      |
|         # Categorical pipeline                                                                                       |
|         categorical_pipeline = Pipeline([                                                                            |
|             ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),                                   |
|             ('onehot', OneHotEncoder(drop='first', sparse=False))                                                    |
|         ])                                                                                                           |
|                                                                                                                      |
|         # Combine pipelines                                                                                          |
|         preprocessor                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------+

```

