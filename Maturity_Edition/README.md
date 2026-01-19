# Maturity Edition: Fixed Income Maturity Analysis

This edition focuses on analyzing fixed income securities, yield curves, duration risk, and maturity-based investment strategies.

## Overview

The Maturity Edition provides comprehensive analysis of:
- Yield curve dynamics and term structure
- Duration and convexity analysis
- Maturity laddering strategies
- Interest rate risk assessment
- Bond portfolio optimization

## Setup Instructions

### 1. Create Conda Environment
```bash
conda env create -f environment.yml
conda activate maturity_edition
```

### 2. Launch Jupyter Notebook
```bash
jupyter notebook analysis.ipynb
```

## Key Analysis Components

### Data Sources
- **FRED API**: Treasury yield curves, rates data
- **Yahoo Finance**: Bond ETF and individual bond data
- **Treasury Direct**: Government securities information

### Analysis Framework
- **Yield Curve Construction**: Building and analyzing term structures
- **Duration Calculations**: Modified duration and effective duration
- **Convexity Analysis**: Price sensitivity to yield changes
- **Maturity Strategies**: Laddering and barbell approaches

## File Structure
```
Maturity_Edition/
├── environment.yml          # Conda environment specification
├── analysis.ipynb          # Main analysis notebook
├── README.md              # This file
└── data/                  # Data storage (created automatically)
```

## Usage Notes

- Ensure conda environment is activated before running analysis
- Data is fetched automatically from APIs (internet connection required)
- Charts are optimized for newsletter publication
- All analysis uses daily data for accuracy