# LME Edition - Newsletter Analysis

## Overview
This analysis tracks London Metal Exchange (LME) market dynamics and their relationship with broader financial markets. The analysis focuses on key base metals and their price movements in relation to economic indicators.

## Key Insights
- Tracking copper, aluminum, zinc, nickel, and other base metals
- Analyzing inventory levels and their impact on prices
- Examining correlations between metal prices and economic indicators
- Monitoring supply chain disruptions and geopolitical impacts

## Data Sources
- **LME Metals Data**: Various sources including FRED and direct LME feeds
- **Economic Indicators**: FRED database
- **Inventory Data**: LME warehouse stocks
- **Currency Data**: For currency-adjusted analysis

## Charts Generated
### Chart 1: Base Metals Price Index
- Copper prices (red)
- Aluminum prices (blue) 
- Zinc prices (green)
- Nickel prices (orange)

### Chart 2: Inventory Levels vs Prices
- LME warehouse stocks
- Price correlations with inventory changes

### Chart 3: Economic Correlations
- Base metals vs global GDP indicators
- Industrial production relationships

## Requirements
- pandas-datareader
- fredapi
- yfinance
- matplotlib
- seaborn
- plotly

## Setup
1. Create conda environment: `conda env create -f environment.yml`
2. Activate environment: `conda activate lme_edition`
3. Launch jupyter: `jupyter notebook analysis.ipynb`