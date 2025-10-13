# Financial Market Analysis Newsletter Projects

This repository contains Python-based analysis projects for financial market newsletters, focusing on various market indicators and economic metrics.

## Projects

### 1. Treasury Term Premium Analysis
Located in `TermPremium_Edition/`
- Analysis of the structural shift in Treasury term premium
- Decomposition of 10-year yield components
- Visualization of term premium trends and yield curve comparisons
- Data source: Federal Reserve Bank of New York (ACM Term Structure Model)

### 2. Bank of Japan Policy Analysis
Located in `BOJ_Edition/`
- Analysis of BOJ policy changes
- Market reaction assessment
- Daily changes visualization

## Requirements
- Python 3.x
- Required packages:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - pandas_datareader

## Data Sources
- Federal Reserve Economic Data (FRED)
- Bank of Japan Statistics
- Financial market data feeds

## Visualizations
Each analysis includes custom visualizations created using matplotlib and seaborn:
- Yield curve comparisons
- Term premium trends
- Component breakdowns
- Market reaction charts

## Usage
Each project folder contains a Jupyter notebook (`analysis.ipynb`) with:
- Detailed analysis steps
- Data retrieval and processing
- Visualization generation
- Key findings and interpretations

## Project Structure
```
Newsletter_Projects/
├── TermPremium_Edition/
│   ├── analysis.ipynb
│   ├── yield_curve_comparison.png
│   └── yield_components_comparison.png
├── BOJ_Edition/
│   ├── analysis.ipynb
│   ├── boj_daily_changes.png
│   └── boj_market_reaction.png
└── README.md
```

## Updates
Projects are updated regularly with new analysis and market insights.