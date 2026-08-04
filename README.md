# Mutual Fund Analytics

A comprehensive Data Analytics project developed to analyze Indian Mutual Fund data using Python, SQL, SQLite, Power BI, and advanced financial analytics.

The project covers the complete analytics pipeline—from data ingestion and cleaning to exploratory data analysis (EDA), performance evaluation, dashboard creation, and advanced risk metrics.

---

## Project Objectives

- Build an end-to-end Mutual Fund Analytics solution.
- Perform data cleaning and preprocessing.
- Analyze mutual fund performance using financial metrics.
- Develop interactive Power BI dashboards.
- Calculate advanced risk metrics such as VaR, CVaR, Sharpe Ratio, and HHI.
- Generate actionable investment insights through analytics and visualizations.

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn, Power BI |
| Database | SQLite |
| SQL | SQLite SQL |
| Development Environment | Visual Studio Code, Jupyter Notebook |
| Version Control | Git & GitHub |

---

## Project Workflow

```
Raw Data
     │
     ▼
Data Ingestion
     │
     ▼
Data Cleaning
     │
     ▼
Exploratory Data Analysis (EDA)
     │
     ▼
Performance Analytics
     │
     ▼
Power BI Dashboard
     │
     ▼
Advanced Analytics
     │
     ▼
Reports & Recommendations
```

---

## Project Structure

```
Mutual_Fund_Analytics/
│
├── Dashboard/
├── Data/
│   ├── Raw/
│   └── Clean/
├── Notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
├── Reports/
├── Scripts/
├── SQL/
├── README.md
└── requirements.txt
```

---

## Datasets Used

The project uses multiple mutual fund datasets to perform end-to-end analytics.

| Dataset | Description |
|----------|-------------|
| Fund Master | Basic information about mutual fund schemes |
| NAV History | Historical Net Asset Value (NAV) data |
| Scheme Performance | Returns across different investment horizons |
| Investor Transactions | SIP, Lumpsum, and Redemption transactions |
| Portfolio Holdings | Mutual fund portfolio allocation |
| Benchmark Indices | Benchmark index performance |

---

## Project Modules

### Task 1 – Data Ingestion
- Loaded raw CSV datasets.
- Stored datasets in SQLite database.
- Verified data quality and schema.

### Task 2 – Data Cleaning
- Removed duplicates and missing values.
- Standardized column names and data types.
- Generated cleaned datasets.

### Task 3 – Exploratory Data Analysis (EDA)
- Fund distribution analysis.
- Investor demographic analysis.
- Transaction trend analysis.
- Portfolio composition analysis.

### Task 4 – Performance Analytics
- CAGR calculation.
- Annualized Volatility.
- Beta calculation.
- Alpha calculation.
- Tracking Error.
- Benchmark comparison.

### Task 5 – Power BI Dashboard
- Interactive performance dashboard.
- Benchmark comparison.
- Portfolio allocation.
- Investor analytics.

### Task 6 – Advanced Analytics & Risk Metrics
- Historical Value at Risk (VaR 95%)
- Conditional Value at Risk (CVaR)
- Rolling 90-Day Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Mutual Fund Recommendation Engine
- Herfindahl-Hirschman Index (HHI)

---

## Project Modules

### Task 1 – Data Ingestion
- Loaded raw CSV datasets.
- Stored datasets in SQLite database.
- Verified data quality and schema.

### Task 2 – Data Cleaning
- Removed duplicates and missing values.
- Standardized column names and data types.
- Generated cleaned datasets.

### Task 3 – Exploratory Data Analysis (EDA)
- Fund distribution analysis.
- Investor demographic analysis.
- Transaction trend analysis.
- Portfolio composition analysis.

### Task 4 – Performance Analytics
- CAGR calculation.
- Annualized Volatility.
- Beta calculation.
- Alpha calculation.
- Tracking Error.
- Benchmark comparison.

### Task 5 – Power BI Dashboard
- Interactive performance dashboard.
- Benchmark comparison.
- Portfolio allocation.
- Investor analytics.

### Task 6 – Advanced Analytics & Risk Metrics
- Historical Value at Risk (VaR 95%)
- Conditional Value at Risk (CVaR)
- Rolling 90-Day Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Mutual Fund Recommendation Engine
- Herfindahl-Hirschman Index (HHI)

---

## Project Deliverables

- Advanced_Analytics.ipynb
- EDA_Analysis.ipynb
- Performance_Analytics.ipynb
- recommender.py
- var_cvar_report.csv
- investor_cohort_report.csv
- sip_continuity_report.csv
- hhi_concentration_report.csv
- latest_sharpe_report.csv
- rolling_sharpe_chart.png

---

## Key Insights

- Historical VaR and CVaR help identify downside investment risk across mutual fund schemes.
- Rolling 90-Day Sharpe Ratio highlights changes in risk-adjusted performance over time.
- Investor Cohort Analysis reveals investment behavior based on the year of first investment.
- SIP Continuity Analysis identifies investors who are at risk of discontinuing their SIPs.
- The Recommendation Engine suggests suitable mutual funds based on investor risk appetite.
- HHI Concentration Analysis measures portfolio diversification and identifies highly concentrated portfolios.

---

## How to Run the Project

### Clone the repository

```bash
git clone https://github.com/shash2986/Mutual_Fund_Analytics
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Launch Jupyter Notebook

```bash
jupyter notebook
```

Open the notebooks in the `Notebooks` folder and execute the cells sequentially.

---

## Author

**Shashank S**

- GitHub: https://github.com/shash2986
- LinkedIn: https://www.linkedin.com/in/shashank-s-884ba6333/

---

If you found this project useful, feel free to explore the repository and provide your feedback.