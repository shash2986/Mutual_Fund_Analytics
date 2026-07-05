# -----------------------------------
# 3. dim_fund
# -----------------------------------
import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///bluestock_mf.db")

with engine.begin() as conn:
    conn.execute(text("DELETE FROM fact_nav"))
    conn.execute(text("DELETE FROM fact_transactions"))
    conn.execute(text("DELETE FROM fact_performance"))
    conn.execute(text("DELETE FROM fact_aum"))
    conn.execute(text("DELETE FROM dim_date"))
    conn.execute(text("DELETE FROM dim_fund"))

print("Existing data cleared successfully!")

print("Database connected successfully!")

# Read cleaned scheme performance dataset
df = pd.read_csv("Data/Processed/07_scheme_performance_clean.csv")

print(df.head())

# Create dim_fund dataframe
dim_fund = df[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category",
        "plan"
    ]
]

print(dim_fund["amfi_code"].duplicated().sum())

# Load dim_fund into SQLite
dim_fund.to_sql(
    "dim_fund",
    con=engine,
    if_exists="append",
    index=False
)

print("dim_fund loaded successfully!")

# -----------------------------------
# 3. dim_date
# -----------------------------------

# Read cleaned datasets
nav_df = pd.read_csv("Data/Processed/02_nav_history_clean.csv")
trans_df = pd.read_csv("Data/Processed/08_investor_transactions_clean.csv")


nav_df["date"] = pd.to_datetime(nav_df["date"])

trans_df["transaction_date"] = pd.to_datetime(
    trans_df["transaction_date"]
)


all_dates = pd.concat([
    nav_df["date"],
    trans_df["transaction_date"]
])

all_dates = all_dates.drop_duplicates()

dim_date = pd.DataFrame({
    "date": all_dates
})

print(dim_date.head())
print(dim_date.shape)

# Create date attributes
dim_date["day"] = dim_date["date"].dt.day

dim_date["month"] = dim_date["date"].dt.month

dim_date["month_name"] = dim_date["date"].dt.month_name()

dim_date["quarter"] = dim_date["date"].dt.quarter

dim_date["year"] = dim_date["date"].dt.year

print(dim_date.head())
print(dim_date.shape)

# Load dim_date into SQLite
dim_date.to_sql(
    "dim_date",
    con=engine,
    if_exists="append",
    index=False
)

print("dim_date loaded successfully!")

# -----------------------------------
# 3. Load fact_nav
# -----------------------------------

nav_df = pd.read_csv("Data/Processed/02_nav_history_clean.csv")

fact_nav = nav_df[
    [
        "amfi_code",
        "date",
        "nav"
    ]
]

print(fact_nav.head())
print(fact_nav.shape)

fact_nav.to_sql(
    "fact_nav",
    con=engine,
    if_exists="append",
    index=False
)

print("fact_nav loaded successfully!")

# -----------------------------------
# 4. Load fact_transactions
# -----------------------------------

trans_df = pd.read_csv(
    "Data/Processed/08_investor_transactions_clean.csv"
)

trans_df.rename(
    columns={
        "transaction_date": "date"
    },
    inplace=True
)

print(trans_df.columns)

fact_transactions = trans_df[
    [
        "investor_id",
        "date",
        "amfi_code",
        "transaction_type",
        "amount_inr",
        "state",
        "city",
        "city_tier",
        "age_group",
        "gender",
        "annual_income_lakh",
        "payment_mode",
        "kyc_status"
    ]
]

print(fact_transactions.head())

print(fact_transactions.shape)

# Load fact_transactions into SQLite
fact_transactions.to_sql(
    "fact_transactions",
    con=engine,
    if_exists="append",
    index=False
)

print("fact_transactions loaded successfully!")

# -----------------------------------
# 5. fact_performance
# -----------------------------------

perf_df = pd.read_csv("Data/Processed/07_scheme_performance_clean.csv")

print(perf_df.columns)

# Create fact_performance dataframe

fact_performance = perf_df[
    [
        "amfi_code",
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct",
        "benchmark_3yr_pct",
        "alpha",
        "beta",
        "sharpe_ratio",
        "sortino_ratio",
        "std_dev_ann_pct",
        "max_drawdown_pct",
        "expense_ratio_pct",
        "morningstar_rating",
        "risk_grade"
    ]
]

print(fact_performance.head())
print(fact_performance.shape)

# Load fact_performance into SQLite

fact_performance.to_sql(
    "fact_performance",
    con=engine,
    if_exists="append",
    index=False
)

print("fact_performance loaded successfully!")

# -----------------------------------
# 5. fact_aum
# -----------------------------------

fact_aum = perf_df[
    [
        "amfi_code",
        "aum_crore"
    ]
]

print(fact_aum.head())
print(fact_aum.shape)

# Load fact_aum into SQLite

fact_aum.to_sql(
    "fact_aum",
    con=engine,
    if_exists="append",
    index=False
)

print("fact_aum loaded successfully!")

