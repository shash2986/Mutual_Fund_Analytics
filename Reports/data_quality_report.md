# Data Quality Report

## Dataset Summary

Total Datasets Checked: 10

Checks Performed:
- Shape Analysis
- Data Type Validation
- Missing Value Check
- Duplicate Value Check
- Statistical Summary

## Findings

### Missing Values
- Dataset 04_monthly_sip_inflows.csv contains 12 missing values in yoy_growth_pct column.
- All other datasets contain 0 missing values.

### Duplicate Records
- No duplicate records found in any dataset.

### Data Types
- Data types appear appropriate across datasets.

### Overall Status
Datasets successfully loaded and validated.
Ready for data cleaning and transformation.

### AMFI Code Validation

- Total fund master codes checked: 40
- Total NAV history codes checked: 40
- Missing codes found: 0
- All AMFI codes from fund_master are present in nav_history.