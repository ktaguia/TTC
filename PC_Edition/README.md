# PC Edition - Principal Component Analysis

## Overview
This analysis applies Principal Component Analysis (PCA) to financial markets, focusing on identifying the dominant factors driving market movements. The "PC" framework helps decompose complex market dynamics into their essential components.

## Key Analysis Areas
1. **Principal Components of Yield Curves**: Identifying level, slope, and curvature factors
2. **Cross-Asset Principal Components**: Understanding correlations across equity, bond, and commodity markets
3. **Factor Loading Analysis**: Determining which assets/sectors are most sensitive to each principal component
4. **Variance Explanation**: Quantifying how much market movement each component explains

## Key Insights
- PC1 typically captures broad market sentiment (level factor)
- PC2 often represents risk-on/risk-off dynamics (slope factor)
- PC3 and higher components capture more nuanced, sector-specific movements
- High PC loadings indicate strong factor sensitivity

## Data Sources
- **Treasury Yields**: Multiple maturities from FRED (DGS3MO, DGS2, DGS5, DGS10, DGS30)
- **Equity Indices**: S&P 500, Russell 2000, NASDAQ via Yahoo Finance
- **Currency Pairs**: Major FX rates (USD/EUR, USD/JPY, GBP/USD)
- **Commodities**: Gold, Oil, Copper prices

## Charts Generated
### Chart 1: Principal Components Decomposition
- Eigenvalue plot showing variance explained by each component
- Cumulative variance explanation

### Chart 2: Factor Loadings Heatmap
- Visual representation of how each asset loads on principal components
- Color-coded intensity for easy interpretation

### Chart 3: Principal Component Time Series
- Evolution of the first 3-4 principal components over time
- Overlay with major market events for context

## Requirements
- scikit-learn for PCA implementation
- pandas and numpy for data manipulation
- matplotlib and seaborn for visualization
- pandas-datareader for data fetching

## Usage
1. Set up the conda environment using `environment.yml`
2. Run the `analysis.ipynb` notebook
3. Charts and analysis will be automatically generated

## Environment Setup
The conda environment includes all necessary packages for PCA analysis and visualization.

## Notes
- PCA is performed on standardized data to ensure equal weighting
- Component interpretation requires domain knowledge of financial markets
- The analysis focuses on the most recent period for relevance to current market conditions
- Factor loadings are normalized for easier comparison across assets