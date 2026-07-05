import pandas as pd

df = pd.read_csv("Data/Raw/08_investor_transactions.csv")

# Convert transaction_date to datetime
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

print(df.dtypes)

# Standardize transaction_type
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.lower()
    .replace({
        "sip": "SIP",
        "lumpsum": "Lumpsum",
        "redemption": "Redemption"
    })
)

# Verify the standardization
print(df["transaction_type"].unique())

# Standardize kyc_status
df["kyc_status"] = (
    df["kyc_status"]
    .str.strip()
    .str.lower()
    .replace({
        "verified": "Verified",
        "pending": "Pending"
    })
)

print(df["kyc_status"].unique())

# Validate transaction amount
print((df["amount_inr"] > 0).all())

# Check duplicate rows
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv("Data/Processed/08_investor_transactions_clean.csv", index=False)

print("Cleaned investor_transactions.csv saved successfully!")

#print(df.head(10))

#print(df.shape)

#print(df.columns)

#print(df.dtypes)

#print(df["age_group"].unique())

#print(df["transaction_type"].unique())

# Validate transaction amount
#print((df["amount_inr"] > 0).all())

#print(df["kyc_status"].unique())

print(
    df.duplicated(
        subset=["investor_id", "transaction_date", "amfi_code"]
    ).sum()
)

duplicates = df[df.duplicated(
    subset=["investor_id", "transaction_date", "amfi_code"],
    keep=False
)]

print(duplicates)

print(
    df.duplicated(
        subset=[
            "investor_id",
            "transaction_date",
            "amfi_code",
            "transaction_type"
        ]
    ).sum()
)