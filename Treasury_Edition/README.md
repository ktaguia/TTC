# Treasury Edition: Interest Rate & Yield Curve Analysis

This analysis examines the U.S. Treasury market through comprehensive interest rate and yield curve analysis for newsletter publication.

## Analysis Framework

### Key Focus Areas
- **Treasury Yield Curves**: Current vs. historical yield curve shapes
- **Rate Environment**: Federal funds rate trajectory and impact
- **Term Structure**: Analysis of yield spreads across maturities
- **Market Signals**: Inversion patterns and recession indicators
- **Inflation Expectations**: TIPS vs. nominal yield analysis

### Data Sources
- **FRED API**: Federal Reserve Economic Data
  - Treasury rates (DGS3MO, DGS2, DGS5, DGS10, DGS30)
  - Federal funds rate (FEDFUNDS)
  - TIPS yields and breakeven inflation rates
- **Real-time market data**: Current treasury pricing

## Setup Instructions

### 1. Create Conda Environment
```bash
conda env create -f environment.yml
conda activate treasury_edition
```

### 2. Install Jupyter Kernel
```bash
python -m ipykernel install --user --name treasury_edition --display-name "Python (treasury_edition)"
```

### 3. Launch Analysis
```bash
jupyter notebook analysis.ipynb
```

## File Structure
```
Treasury_Edition/
├── analysis.ipynb          # Main analysis notebook
├── environment.yml         # Conda environment setup
├── README.md              # This file
└── data/                  # Data storage
    └── (auto-generated)   # FRED data cache
```

## Analysis Outputs

### Chart A: Yield Curve Evolution
- Current yield curve vs. historical averages
- Inversion detection and visualization
- Term premium analysis

### Chart B: Rate Environment Dashboard
- Federal funds rate trajectory
- Forward rate expectations
- Market-based recession indicators

### Chart C: Inflation Expectations
- TIPS breakeven inflation rates
- Real vs. nominal yield comparison
- Inflation risk premium analysis

## Newsletter Integration

- **Professional styling**: Sharp colors and clean formatting
- **Publication-ready charts**: High-resolution outputs
- **Executive summary**: Key insights and market implications
- **Data recency**: Current through latest trading day

---

*Treasury Edition Analysis - Newsletter Series*
*Data Sources: Federal Reserve (FRED), U.S. Treasury*