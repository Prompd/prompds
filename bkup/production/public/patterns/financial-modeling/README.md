# @prompd.io/financial-modeling

Advanced financial modeling and analysis package inheriting from data-patterns with specialized financial metrics, forecasting, and risk analysis capabilities.

## Features

- **Inherits from**: `@prompd.io/data-patterns@1.0.0` (includes all data analysis capabilities)
- **Financial Models**: DCF, Comparable, Precedent, LBO, Merger, Portfolio, Risk, Sensitivity, Monte Carlo
- **Valuation Methods**: Multiple valuation approaches with cross-validation
- **Risk Analytics**: VaR, CVaR, Sharpe, Sortino, Beta, Alpha, Correlation analysis
- **Scenario Analysis**: Bull/Base/Bear cases with Monte Carlo simulation
- **Industry Expertise**: Sector-specific metrics and benchmarking
- **Portfolio Management**: Asset allocation, optimization, and rebalancing

## Usage

### DCF Valuation Model
```bash
prompd run financial-modeling.prmd \
  --data_source "financial_statements.csv" \
  --model_type "dcf" \
  --time_horizon "5-year" \
  --scenario_analysis true
```

### Risk Analysis
```bash
prompd run financial-modeling.prmd \
  --data_source "portfolio_returns.csv" \
  --model_type "risk" \
  --risk_metrics '["var", "sharpe", "volatility", "beta"]' \
  --monte_carlo_simulations 5000
```

### Comparable Company Analysis
```bash
prompd run financial-modeling.prmd \
  --data_source "peer_companies.csv" \
  --model_type "comparable" \
  --industry_sector "technology" \
  --valuation_methods '["multiples", "dcf"]'
```

This package provides institutional-grade financial modeling capabilities with comprehensive risk analysis and valuation methodologies.