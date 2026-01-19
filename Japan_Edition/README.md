# Japan Edition - Newsletter Analysis

## Overview
This analysis tracks Japanese capital flows and the "Gravity Well" effect that has traditionally kept Japanese capital invested in US Treasuries. It focuses on two key metrics:

1. **The Yield Gap (The Incentive to Stay)**: Comparing hedged US Treasury yields vs Japanese Government Bond yields
2. **The Repatriation Pulse**: Tracking actual capital flows through Japanese holdings of US Treasuries

## Key Insights
- When hedged US yields fall below Japan yields, expect capital repatriation
- Red bars in the net flows chart indicate money leaving US Treasuries
- Sustained outflows coinciding with BoJ rate hikes confirm the repatriation trend

## Data Sources
- **US 10-Year Treasury Yield**: FRED Symbol `DGS10`
- **Japan 10-Year Government Bond Yield**: FRED Symbol `IRLTLT01JPM156N`  
- **Japanese Treasury Holdings**: Multiple symbols attempted (TICGJ, JPNASSETS, TICS3FJ)

## Charts Generated
### Chart 1: The Yield Gap - The Incentive to Stay
- US 10-Year Treasury Yield (blue)
- Japan 10-Year Government Bond Yield (red)
- Hedged US 10-Year Yield (green, dashed) - approximated with 2.5% hedging cost

### Chart 2: The Repatriation Pulse
- Japanese Holdings of US Treasuries (bar chart)
- Monthly Net Flows (green = purchases, red = sales)

## Requirements
- pandas-datareader
- pandas
- matplotlib
- seaborn
- numpy

## Usage
1. Activate the `japan_edition` conda environment
2. Run the `analysis.ipynb` notebook
3. Charts will be automatically generated and displayed

## Environment Setup
The conda environment includes all necessary packages for data fetching and visualization.

## Notes
- The hedging cost is approximated at 2.5% - for more precision, actual FX forward rates would be needed
- If FRED Treasury holdings data is unavailable, sample data is generated for demonstration
- Large outflows are annotated in the net flows chart for easy identification