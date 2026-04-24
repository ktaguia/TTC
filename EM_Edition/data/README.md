# EM Edition Data Directory

## Overview
This directory contains data files used for Emerging Markets (EM) financial analysis. The notebook will automatically fetch most data from online sources, but this folder can be used to store:

## Expected Data Files
- **EM bond yield data** (CSV format)
- **Capital flow data** from central banks or international organizations
- **Currency exchange rate data** for major EM currencies
- **Alternative data sources** when APIs are unavailable

## Data Sources
The analysis primarily uses data from:
- **FRED API**: US Treasury yields, VIX, DXY
- **Yahoo Finance**: EM bond ETFs (EMB, EMHY, EMLC)
- **Sample data**: Generated when real data is unavailable

## File Formats
- CSV files with Date column and numeric data
- Date format: YYYY-MM-DD
- Column names should be descriptive (e.g., "EM_10Y_Yield", "Capital_Flows_USD")

## Notes
- The notebook includes fallback mechanisms when external data is unavailable
- Large data files (>10MB) should be compressed
- Always include data source attribution in file names or metadata