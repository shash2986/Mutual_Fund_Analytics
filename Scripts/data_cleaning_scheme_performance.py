import pandas as pd

# Read dataset
df = pd.read_csv("Data/Raw/07_scheme_performance.csv")

#checking the anomalies  
print(df.isnull().sum())

print(df.duplicated().sum())

print(df["expense_ratio_pct"].describe())

print(df["risk_grade"].unique())

# Validate return columns are numeric
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print(df[return_columns].dtypes)

# Standardize risk_grade
df["risk_grade"] = (
    df["risk_grade"]
    .str.strip()
    .str.lower()
    .replace({
        "low": "Low",
        "moderate": "Moderate",
        "moderately high": "Moderately High",
        "high": "High",
        "very high": "Very High"
    })
)

# Verify
print(df["risk_grade"].unique())

# Validate expense ratio
print(df["expense_ratio_pct"].between(0.1, 2.5).all())

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv("Data/Processed/07_scheme_performance_clean.csv", index=False)

print("Cleaned scheme_performance.csv saved successfully!")

# Display first 10 rows
#print(df.head(10))

# Dataset shape
#print(df.shape)

# Column names
#print(df.columns)

# Data types
#print(df.dtypes)

print(df["amfi_code"].duplicated().sum())