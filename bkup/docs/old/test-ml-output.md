<!-- PROMPD METADATA
author: null
context: null
description: End-to-end ML pipeline with data preprocessing, training, validation,
  and deployment
id: ml-pipeline-builder
inputs: {}
name: Machine Learning Pipeline Builder
parameters:
- default: null
  description: Type of ML problem to solve
  error_message: null
  example: null
  max_value: null
  min_value: null
  name: problem_type
  pattern: null
  required: true
  type: !!python/object/apply:builtins.getattr
  - &id001 !!python/name:prompd.models.ParameterType ''
  - STRING
- default: null
  description: ML framework to use
  error_message: null
  example: null
  max_value: null
  min_value: null
  name: framework
  pattern: null
  required: true
  type: !!python/object/apply:builtins.getattr
  - *id001
  - STRING
- default: null
  description: Primary data source type
  error_message: null
  example: null
  max_value: null
  min_value: null
  name: data_source
  pattern: null
  required: true
  type: !!python/object/apply:builtins.getattr
  - *id001
  - STRING
- default: null
  description: Deployment environment
  error_message: null
  example: null
  max_value: null
  min_value: null
  name: deployment_target
  pattern: null
  required: true
  type: !!python/object/apply:builtins.getattr
  - *id001
  - STRING
- default: medium
  description: Size of dataset
  error_message: null
  example: null
  max_value: null
  min_value: null
  name: data_size
  pattern: null
  required: false
  type: !!python/object/apply:builtins.getattr
  - *id001
  - STRING
- default: null
  description: Target performance metric (accuracy, F1, etc.)
  error_message: null
  example: null
  max_value: null
  min_value: null
  name: performance_target
  pattern: null
  required: false
  type: !!python/object/apply:builtins.getattr
  - *id001
  - FLOAT
requires: []
response: null
system: null
tags: []
user: null
version: 1.0.0

-->

# Main Prompt Content

# {{imports.system}} ML Pipeline Development

## Project Specification
- **Problem Type**: {classification}
- **Framework**: {scikit-learn} 
- **Data Source**: {csv}
- **Deployment**: {real-time}
- **Data Size**: {{data_size}}
{{#if performance_target}}
- **Performance Target**: {0.90}
{{/if}}

Following {{imports.context.ml-best-practices}} for enterprise-grade implementation.

## Phase 1: Data Understanding & Preparation

### Data Ingestion Strategy for {csv}

{{#switch data_source}}
{{#case "csv"}}
```python
import pandas as pd
import numpy as np
from pathlib import Path

class DataIngester:
    def __init__(self, data_path: str):
        self.data_path = Path(data_path)
        
    def load_data(self) -> pd.DataFrame:
        \"\"\"Load and validate CSV data\"\"\"
        df = pd.read_csv(self.data_path)
        
        # Data quality checks
        print(f"Dataset shape: {df.shape}")
        print(f"Missing values: {df.isnull().sum().sum()}")
        print(f"Duplicates: {df.duplicated().sum()}")
        
        return df
        
    def data_quality_report(self, df: pd.DataFrame) -> dict:
        \"\"\"Generate data quality assessment\"\"\"
        return {
            'completeness': 1 - df.isnull().sum() / len(df),
            'uniqueness': df.nunique() / len(df),
            'data_types': df.dtypes.to_dict()
        }
```
{{/case}}
{{#case "database"}}
```python
import sqlalchemy as sa
import pandas as pd
from typing import Optional

class DatabaseIngester:
    def __init__(self, connection_string: str):
        self.engine = sa.create_engine(connection_string)
        
    def load_data(self, query: str, chunksize: Optional[int] = None) -> pd.DataFrame:
        \"\"\"Load data from database with optional chunking\"\"\"
        if chunksize and self.data_size in ['large', 'big-data']:
            return pd.read_sql(query, self.engine, chunksize=chunksize)
        else:
            return pd.read_sql(query, self.engine)
            
    def get_table_stats(self, table_name: str) -> dict:
        \"\"\"Get basic statistics about table\"\"\"
        query = f\"\"\"
        SELECT 
            COUNT(*) as row_count,
            COUNT(DISTINCT *) as unique_rows
        FROM {table_name}
        \"\"\"
        return pd.read_sql(query, self.engine).iloc[0].to_dict()
```
{{/case}}
{{/switch}}

### Feature Engineering Pipeline

Following {{imports.context.ml-best-practices}}, implement comprehensive feature processing:

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.impute import SimpleImputer

class FeatureProcessor:
    def __init__(self, problem_type: str = "{classification}"):
        self.problem_type = problem_type
        self.preprocessor = None
        
    def create_preprocessor(self, X: pd.DataFrame) -> ColumnTransformer:
        \"\"\"Create preprocessing pipeline based on data types\"\"\"
        
        # Identify column types
        numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
        categorical_features = X.select_dtypes(include=['object']).columns
        
        # Numeric pipeline
        numeric_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])
        
        # Categorical pipeline
        categorical_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
            ('onehot', OneHotEncoder(drop='first', sparse=False))
        ])
        
        # Combine pipelines
        preprocessor = ColumnTransformer([
            ('num', numeric_pipeline, numeric_features),
            ('cat', categorical_pipeline, categorical_features)
        ])
        
        self.preprocessor = preprocessor
        return preprocessor
        
    def engineer_features(self, X: pd.DataFrame) -> pd.DataFrame:
        \"\"\"Create domain-specific features\"\"\"
        X_engineered = X.copy()
        
        # Add interaction features for {classification}
        if self.problem_type == 'classification':
            # Create polynomial features for key numeric columns
            from sklearn.preprocessing import PolynomialFeatures
            poly = PolynomialFeatures(degree=2, include_bias=False)
            # Apply to subset of features to avoid curse of dimensionality
            
        elif self.problem_type == 'time-series':
            # Create time-based features
            if 'timestamp' in X.columns:
                X_engineered['hour'] = pd.to_datetime(X['timestamp']).dt.hour
                X_engineered['day_of_week'] = pd.to_datetime(X['timestamp']).dt.dayofweek
                X_engineered['month'] = pd.to_datetime(X['timestamp']).dt.month
                
        return X_engineered
```

## Phase 2: Model Development for {classification}

### Algorithm Selection Strategy

{{#switch problem_type}}
{{#case "classification"}}
**Classification Algorithm Selection for {scikit-learn}:**

```python
{{#switch framework}}
{{#case "scikit-learn"}}
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

class ModelSelector:
    def __init__(self):
        self.models = {
            'logistic_regression': LogisticRegression(random_state=42),
            'random_forest': RandomForestClassifier(n_estimators=100, random_state=42),
            'gradient_boosting': GradientBoostingClassifier(random_state=42),
            'svm': SVC(probability=True, random_state=42),
            'neural_network': MLPClassifier(random_state=42)
        }
        
    def get_baseline_model(self):
        \"\"\"Start with simple baseline\"\"\"
        return self.models['logistic_regression']
        
    def get_advanced_models(self):
        \"\"\"Get ensemble models for better performance\"\"\"
        return {k: v for k, v in self.models.items() 
                if k in ['random_forest', 'gradient_boosting']}
{{/case}}
{{#case "tensorflow"}}
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization

def create_neural_network(input_dim: int, num_classes: int) -> tf.keras.Model:
    \"\"\"Create neural network for classification\"\"\"
    model = Sequential([
        Dense(128, activation='relu', input_shape=(input_dim,)),
        BatchNormalization(),
        Dropout(0.3),
        
        Dense(64, activation='relu'),
        BatchNormalization(),
        Dropout(0.3),
        
        Dense(32, activation='relu'),
        Dropout(0.2),
        
        Dense(num_classes, activation='softmax')
    ])
    
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy', 'precision', 'recall']
    )
    
    return model
{{/case}}
{{/switch}}
```
{{/case}}
{{#case "regression"}}
**Regression Algorithm Selection:**

```python
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

class RegressionModels:
    def __init__(self):
        self.models = {
            'linear_regression': LinearRegression(),
            'ridge': Ridge(alpha=1.0),
            'lasso': Lasso(alpha=1.0),
            'random_forest': RandomForestRegressor(n_estimators=100, random_state=42),
            'gradient_boosting': GradientBoostingRegressor(random_state=42)
        }
        
    def evaluate_model(self, model, X_test, y_test):
        \"\"\"Comprehensive regression evaluation\"\"\"
        predictions = model.predict(X_test)
        
        return {
            'mse': mean_squared_error(y_test, predictions),
            'rmse': np.sqrt(mean_squared_error(y_test, predictions)),
            'mae': mean_absolute_error(y_test, predictions),
            'r2': r2_score(y_test, predictions)
        }
```
{{/case}}
{{/switch}}

### Model Training & Validation Pipeline

```python
from sklearn.model_selection import cross_val_score, GridSearchCV, TimeSeriesSplit
from sklearn.metrics import classification_report, confusion_matrix

class ModelTrainer:
    def __init__(self, problem_type: str = "{classification}"):
        self.problem_type = problem_type
        self.best_model = None
        self.cv_results = {}
        
    def train_with_cross_validation(self, X, y, models_dict):
        \"\"\"Train models with cross-validation\"\"\"
        
        # Choose CV strategy based on problem type
        if self.problem_type == 'time-series':
            cv = TimeSeriesSplit(n_splits=5)
        else:
            cv = 5
            
        results = {}
        
        for name, model in models_dict.items():
            print(f"Training {name}...")
            
            # Cross-validation
            cv_scores = cross_val_score(model, X, y, cv=cv, 
                                      scoring=self._get_scoring_metric())
            
            # Store results
            results[name] = {
                'cv_mean': cv_scores.mean(),
                'cv_std': cv_scores.std(),
                'cv_scores': cv_scores
            }
            
            print(f"{name} - CV Score: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")
            
        self.cv_results = results
        return results
        
    def hyperparameter_tuning(self, model, param_grid, X, y):
        \"\"\"Perform hyperparameter tuning\"\"\"
        grid_search = GridSearchCV(
            model, 
            param_grid, 
            cv=5, 
            scoring=self._get_scoring_metric(),
            n_jobs=-1
        )
        
        grid_search.fit(X, y)
        
        print(f"Best parameters: {grid_search.best_params_}")
        print(f"Best CV score: {grid_search.best_score_:.4f}")
        
        self.best_model = grid_search.best_estimator_
        return grid_search.best_estimator_
        
    def _get_scoring_metric(self):
        \"\"\"Get appropriate scoring metric based on problem type\"\"\"
        if self.problem_type == 'classification':
            return 'f1_weighted'
        elif self.problem_type == 'regression':
            return 'neg_mean_squared_error'
        else:
            return 'accuracy'
```

## Phase 3: Model Evaluation & Validation

### Comprehensive Evaluation Suite

```python
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import plot_confusion_matrix, plot_roc_curve

class ModelEvaluator:
    def __init__(self, problem_type: str = "{classification}"):
        self.problem_type = problem_type
        
    def comprehensive_evaluation(self, model, X_test, y_test, X_train=None, y_train=None):
        \"\"\"Complete model evaluation with visualizations\"\"\"
        results = {}
        
        # Predictions
        y_pred = model.predict(X_test)
        
        if self.problem_type == 'classification':
            results = self._classification_evaluation(model, X_test, y_test, y_pred)
        elif self.problem_type == 'regression':
            results = self._regression_evaluation(model, X_test, y_test, y_pred)
            
        # Feature importance (if available)
        if hasattr(model, 'feature_importances_'):
            results['feature_importance'] = self._plot_feature_importance(model)
            
        # Learning curves
        if X_train is not None and y_train is not None:
            results['learning_curves'] = self._plot_learning_curves(model, X_train, y_train)
            
        return results
        
    def _classification_evaluation(self, model, X_test, y_test, y_pred):
        \"\"\"Classification-specific evaluation\"\"\"
        from sklearn.metrics import accuracy_score, precision_recall_fscore_support
        
        results = {
            'accuracy': accuracy_score(y_test, y_pred),
            'classification_report': classification_report(y_test, y_pred),
            'confusion_matrix': confusion_matrix(y_test, y_pred)
        }
        
        # Plot confusion matrix
        plt.figure(figsize=(8, 6))
        plot_confusion_matrix(model, X_test, y_test)
        plt.title('Confusion Matrix')
        plt.show()
        
        # ROC curve for binary classification
        if len(np.unique(y_test)) == 2:
            plt.figure(figsize=(8, 6))
            plot_roc_curve(model, X_test, y_test)
            plt.title('ROC Curve')
            plt.show()
            
        return results
```

## Phase 4: Production Deployment for {real-time}

### Deployment Strategy

{{#switch deployment_target}}
{{#case "real-time"}}
**Real-time API Deployment:**

```python
from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
    
with open('preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        data = request.get_json()
        
        # Convert to DataFrame
        df = pd.DataFrame([data])
        
        # Preprocess
        X_processed = preprocessor.transform(df)
        
        # Make prediction
        prediction = model.predict(X_processed)
        probability = model.predict_proba(X_processed).max() if hasattr(model, 'predict_proba') else None
        
        return jsonify({
            'prediction': prediction[0].item(),
            'probability': probability.item() if probability else None,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**Docker Configuration:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```
{{/case}}
{{#case "batch"}}
**Batch Processing Pipeline:**

```python
import schedule
import time
from datetime import datetime

class BatchPredictionPipeline:
    def __init__(self, model_path, preprocessor_path):
        self.model = self._load_model(model_path)
        self.preprocessor = self._load_preprocessor(preprocessor_path)
        
    def run_batch_prediction(self):
        \"\"\"Run batch predictions on new data\"\"\"
        try:
            # Load new data
            data = self._load_new_data()
            
            if data is not None and not data.empty:
                # Preprocess
                X_processed = self.preprocessor.transform(data)
                
                # Predict
                predictions = self.model.predict(X_processed)
                
                # Save results
                self._save_predictions(data, predictions)
                
                print(f"Batch prediction completed at {datetime.now()}")
                
        except Exception as e:
            print(f"Batch prediction failed: {e}")
            # Log error, send alert, etc.
            
    def schedule_predictions(self):
        \"\"\"Schedule batch predictions\"\"\"
        schedule.every().day.at("02:00").do(self.run_batch_prediction)
        
        while True:
            schedule.run_pending()
            time.sleep(60)
```
{{/case}}
{{/switch}}

### Model Monitoring & Maintenance

```python
import logging
from datetime import datetime, timedelta

class ModelMonitor:
    def __init__(self, model, threshold_performance={0.90} if {0.90} else 0.85):
        self.model = model
        self.threshold = threshold_performance
        self.performance_history = []
        
    def monitor_performance(self, X_new, y_true):
        \"\"\"Monitor model performance on new data\"\"\"
        y_pred = self.model.predict(X_new)
        
        # Calculate performance
        current_performance = self._calculate_performance(y_true, y_pred)
        
        # Log performance
        self.performance_history.append({
            'timestamp': datetime.now(),
            'performance': current_performance
        })
        
        # Check if retraining is needed
        if current_performance < self.threshold:
            self._trigger_retraining_alert()
            
        return current_performance
        
    def detect_data_drift(self, X_new, X_reference):
        \"\"\"Detect data drift using statistical tests\"\"\"
        from scipy.stats import ks_2samp
        
        drift_detected = False
        drift_scores = {}
        
        for i in range(X_new.shape[1]):
            # Kolmogorov-Smirnov test
            ks_stat, p_value = ks_2samp(X_reference[:, i], X_new[:, i])
            
            drift_scores[f'feature_{i}'] = {
                'ks_statistic': ks_stat,
                'p_value': p_value,
                'drift_detected': p_value < 0.05
            }
            
            if p_value < 0.05:
                drift_detected = True
                
        if drift_detected:
            logging.warning("Data drift detected! Consider retraining the model.")
            
        return drift_scores
```

## Success Criteria & Validation

### Performance Benchmarks
{{#if performance_target}}
- **Target Performance**: {0.90}
{{/if}}
- **Baseline Comparison**: Outperform simple baseline by 15%+
- **Cross-validation**: Consistent performance across folds
- **Production Metrics**: Monitor for performance degradation

### Production Readiness Checklist
- [ ] Model artifacts properly versioned and stored
- [ ] API endpoints tested and documented  
- [ ] Monitoring and alerting configured
- [ ] Data drift detection implemented
- [ ] Rollback strategy defined
- [ ] Performance thresholds established
- [ ] Security and privacy requirements met
- [ ] Documentation complete

### Business Impact Assessment
- Quantify model's business value
- A/B testing framework for model comparison
- User feedback collection mechanism
- Regular business metric review

This ML pipeline follows {{imports.context.ml-best-practices}} and is designed for {real-time} deployment using {scikit-learn}. The implementation includes comprehensive evaluation, monitoring, and production deployment capabilities.