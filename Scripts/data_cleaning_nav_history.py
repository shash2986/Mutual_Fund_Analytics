import pandas as pd

df = pd.read_csv("Data/Raw/02_nav_history.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Check the updated data types
print(df.dtypes)

# Sort by amfi_code and date
df = df.sort_values(by=["amfi_code", "date"])

# Display the first 10 rows
print(df.head(10))

# Check missing values in each column
print(df.isnull().sum())

df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Check duplicate rows
print(df.duplicated().sum())

df = df.drop_duplicates()

#print(df.shape)

# Validate NAV values
print((df["nav"] > 0).all())

# Save cleaned dataset
df.to_csv("Data/Processed/02_nav_history_clean.csv", index=False)

print("Cleaned nav_history.csv saved successfully!")

#print(df.head())

#print(df.shape)

#print(df.columns)

#print(df.dtypes)