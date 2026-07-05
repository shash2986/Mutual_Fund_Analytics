-- ==========================================
-- 1. dim_date
-- ==========================================

CREATE TABLE dim_date (
    date DATE PRIMARY KEY,
    day INTEGER NOT NULL,
    month INTEGER NOT NULL,
    month_name TEXT NOT NULL,
    quarter TEXT NOT NULL,
    year INTEGER NOT NULL
)

-- ==========================================
-- 2. dim_fund
-- ==========================================

CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT NOT NULL,
    fund_house TEXT NOT NULL,
    category TEXT NOT NULL,
    plan TEXT NOT NULL
)

-- ==========================================
-- 3. fact_nav
-- ==========================================

CREATE TABLE fact_nav (
    amfi_code INTEGER,
    date DATE,
    nav REAL NOT NULL,

    PRIMARY KEY (amfi_code, date),

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code),

    FOREIGN KEY (date)
        REFERENCES dim_date(date)
)

-- ==========================================
-- 4. fact_transactions
-- ==========================================

CREATE TABLE fact_transactions (
    investor_id TEXT,
    date DATE,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL NOT NULL,
    state TEXT,
    city TEXT,
    city_tier TEXT,
    age_group TEXT,
    gender TEXT,
    annual_income_lakh REAL,
    payment_mode TEXT,
    kyc_status TEXT,

    PRIMARY KEY (
        investor_id,
        date,
        amfi_code,
        transaction_type
    ),

    FOREIGN KEY (date)
        REFERENCES dim_date(date),

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)
)

-- ==========================================
-- 5. fact_performance
-- ==========================================

CREATE TABLE fact_performance (
    amfi_code INTEGER PRIMARY KEY,

    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    benchmark_3yr_pct REAL,

    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL,

    std_dev_ann_pct REAL,
    max_drawdown_pct REAL,
    expense_ratio_pct REAL,

    morningstar_rating INTEGER,
    risk_grade TEXT,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)
)
-- ==========================================
-- 6. fact_aum
-- ==========================================

CREATE TABLE fact_aum (
    amfi_code INTEGER PRIMARY KEY,
    aum_crore REAL NOT NULL,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)
)