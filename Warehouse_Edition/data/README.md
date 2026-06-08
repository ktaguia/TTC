# Warehouse Edition Data Directory

## Overview
This directory contains data files used for Warehouse Edition analysis. The notebook can pull data from external sources, and this folder is available for local datasets that support the edition.

## Expected Data Files
- Warehouse utilization or inventory series in CSV format
- Freight, logistics, or regional storage indicators
- Supporting macro data used alongside warehouse metrics
- Exported data snapshots when APIs are unavailable

## File Formats
- CSV files with a `Date` column and numeric data columns
- Date format: `YYYY-MM-DD`
- Column names should be descriptive and source-aligned

## Notes
- Keep raw and cleaned datasets clearly named
- Large files should be compressed when practical
- Include source attribution in file names or companion notes