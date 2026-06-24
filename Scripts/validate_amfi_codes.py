import pandas as pd

# Load datasets
fund_master = pd.read_csv("Data/Raw/01_fund_master.csv")
nav_history = pd.read_csv("Data/Raw/02_nav_history.csv")

# Get unique AMFI codes
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Find missing codes
missing_codes = fund_codes - nav_codes

print("=" * 50)
print("AMFI CODE VALIDATION")
print("=" * 50)

print("\nTotal Fund Master Codes:", len(fund_codes))
print("Total NAV History Codes:", len(nav_codes))

print("\nMissing Codes:", missing_codes)

print("\nNumber of Missing Codes:", len(missing_codes))