# NB Edition: Treasury Market Ownership Analysis

This analysis focuses on the "Takeover" narrative - the shift in Treasury securities ownership from the Federal Reserve to private sector entities.

## Charts Included

### 1. The Hand-off Index (Ownership Shifts)
Visualizes the decline of Fed holdings against the rise of private sector ownership:
- **Fed's Footprint**: TREAST (Treasury Securities Held by the Federal Reserve)
- **The New Masters**: HNOTA (Households and Nonprofit Organizations; Treasury Securities)
- **Institutional Anchor**: LITLA (Life Insurance Companies; Treasury Securities)
- **Pension Anchor**: PENTLA (Pension Funds; Treasury Securities)

### 2. The Auction Fever (Tail Volatility)
Tracks auction demand and market stress through:
- **Bid-to-Cover Ratio**: BTCR10Y (10-Year Treasury Note Auctions)
- **Volatility Analysis**: Shows when the market experiences "indigestion"

## Data Sources
All data is sourced from the Federal Reserve Economic Data (FRED) database using the pandas-datareader library.

## Key Insights
The analysis reveals:
- The transition from Fed-dominated to private sector-dominated Treasury ownership
- Auction demand patterns that indicate market stress levels
- Volatility measures that serve as early warning indicators

## Usage
Run the Jupyter notebook to generate the latest analysis with current data from FRED.

## Requirements
- pandas
- numpy
- matplotlib
- seaborn
- pandas-datareader
- datetime