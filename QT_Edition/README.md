# QT Edition: Quantitative Tightening Liquidity Analysis

This edition analyzes the liquidity dynamics during the Federal Reserve's Quantitative Tightening (QT) period, focusing on the reserve floor mechanism and funding stress indicators.

## Key Analysis Components

### Chart 1: IORB-EFFR Spread vs Bank Reserves
- **Primary Focus**: The reserve floor mechanism
- **Key Metric**: IORB-EFFR spread as stress indicator
- **Secondary Data**: Total bank reserves (liquidity cushion)
- **Insight**: Shows approach to reserve floor and banking system stress

### Chart 2: Funding Risk Multiplier
- **Primary Focus**: Credit/funding stress proxy
- **Key Metric**: High Yield Option-Adjusted Spread
- **Insight**: Repo/credit stress as liquidity drains

## Data Sources
- **FRED Series Used**:
  - `RESBALNS`: Reserve Balances with Federal Reserve Banks
  - `DFF`: Effective Federal Funds Rate
  - `IORB`: Interest Rate on Reserve Balances
  - `BAMLH0A0CM4FEDPR`: High Yield Credit Spread (funding stress proxy)

## Setup Instructions

### 1. Create Conda Environment
```bash
cd QT_Edition
conda env create -f environment.yml
conda activate qt_edition
```

### 2. Launch Jupyter
```bash
jupyter notebook analysis.ipynb
```

### 3. Run Analysis
Execute all cells to generate the dual-chart liquidity analysis.

## Analysis Period
- **Start**: June 1, 2022 (Beginning of current QT cycle)
- **End**: Latest available data
- **Focus**: Reserve floor dynamics and funding stress evolution

## Key Insights
The analysis reveals how QT's liquidity drain creates:
1. **Reserve Floor Pressure**: Measured by IORB-EFFR spread widening
2. **Funding Stress Multiplication**: Credit spreads responding to liquidity conditions
3. **Banking System Stress**: Observable through rate divergences

## Professional Features
- Real-time FRED data integration
- Dual-axis visualization for complex relationships
- Moving averages for signal smoothing
- Error handling with fallback data structure
- Professional styling and annotations