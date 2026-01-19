# Data Directory

This directory contains cached data files and outputs from the Japan Edition analysis.

## Files
- **yield_data_cache.pkl**: Cached FRED data to avoid repeated API calls
- **japan_treasury_flows.csv**: Processed Treasury holdings and flow data
- **chart_outputs/**: Directory for saved chart images

## Data Sources
- Federal Reserve Economic Data (FRED)
- U.S. Treasury Department (TIC Data)
- Bank of Japan publications

## Notes
- Data files are automatically generated when running the analysis
- Cache files help improve performance on subsequent runs
- All data sources are publicly available