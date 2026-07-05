# Mutual Fund Analytics - Data Dictionary

## Overview

This document describes the tables, columns, data types, and business meaning of the SQLite star schema used in the Mutual Fund Analytics project.

---

# Table: dim_fund

| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | INTEGER | Unique identifier for each mutual fund scheme |
| scheme_name | TEXT | Name of the mutual fund scheme |
| fund_house | TEXT | Asset Management Company (AMC) |
| category | TEXT | Mutual fund category (Large Cap, Mid Cap, etc.) |
| plan | TEXT | Investment plan (Regular or Direct) |

---

# Table: dim_date

| Column | Data Type | Description |
|--------|-----------|-------------|
| date | DATE | Calendar date |
| day | INTEGER | Day of the month |
| month | INTEGER | Month number |
| month_name | TEXT | Name of the month |
| quarter | INTEGER | Quarter of the year |
| year | INTEGER | Calendar year |

---

# Table: fact_nav

| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | INTEGER | Unique identifier of the mutual fund scheme |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value (NAV) of the scheme on the given date |

---

# Table: fact_transactions

| Column | Data Type | Description |
|--------|-----------|-------------|
| investor_id | TEXT | Unique identifier of the investor |
| date | DATE | Transaction date |
| amfi_code | INTEGER | Mutual fund scheme identifier |
| transaction_type | TEXT | Type of transaction (SIP, Redemption, Lumpsum) |
| amount_inr | REAL | Transaction amount in Indian Rupees |
| state | TEXT | State of the investor |
| city | TEXT | City of the investor |
| city_tier | TEXT | City classification (T30/B30) |
| age_group | TEXT | Age group of the investor |
| gender | TEXT | Gender of the investor |
| annual_income_lakh | REAL | Annual income in lakhs |
| payment_mode | TEXT | Mode of payment |
| kyc_status | TEXT | KYC verification status |

---

# Table: fact_performance

| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | INTEGER | Mutual fund scheme identifier |
| return_1yr_pct | REAL | One-year return percentage |
| return_3yr_pct | REAL | Three-year return percentage |
| return_5yr_pct | REAL | Five-year return percentage |
| benchmark_3yr_pct | REAL | Three-year benchmark return |
| alpha | REAL | Alpha performance metric |
| beta | REAL | Beta risk metric |
| sharpe_ratio | REAL | Risk-adjusted return using Sharpe Ratio |
| sortino_ratio | REAL | Downside risk-adjusted return |
| std_dev_ann_pct | REAL | Annualized standard deviation |
| max_drawdown_pct | REAL | Maximum observed loss percentage |
| expense_ratio_pct | REAL | Annual expense ratio |
| morningstar_rating | INTEGER | Morningstar fund rating |
| risk_grade | TEXT | Risk category of the scheme |

---

# Table: fact_aum

| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | INTEGER | Mutual fund scheme identifier |
| aum_crore | REAL | Assets Under Management (AUM) in crores |

---

## Summary

The Mutual Fund Analytics project uses a star schema consisting of two dimension tables (`dim_fund`, `dim_date`) and four fact tables (`fact_nav`, `fact_transactions`, `fact_performance`, `fact_aum`). This structure enables efficient analytical SQL queries and dashboard development in Power BI.

