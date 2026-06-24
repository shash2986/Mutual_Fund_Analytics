import pandas as pd

# Load fund master dataset
fund_master = pd.read_csv("Data/Raw/01_fund_master.csv")

# Fund Houses
print("\n" + "=" * 50)
print("UNIQUE FUND HOUSES")
print("=" * 50)

print(fund_master["fund_house"].unique())
print("\nTotal Fund Houses:", fund_master["fund_house"].nunique())

# Categories
print("\n" + "=" * 50)
print("UNIQUE CATEGORIES")
print("=" * 50)

print(fund_master["category"].unique())
print("\nTotal Categories:", fund_master["category"].nunique())

# Sub Categories
print("\n" + "=" * 50)
print("UNIQUE SUB-CATEGORIES")
print("=" * 50)

print(fund_master["sub_category"].unique())
print("\nTotal Sub-Categories:", fund_master["sub_category"].nunique())

# Risk Categories
print("\n" + "=" * 50)
print("UNIQUE RISK CATEGORIES")
print("=" * 50)

print(fund_master["risk_category"].unique())
print("\nTotal Risk Categories:", fund_master["risk_category"].nunique())