'''import pandas as pd  #To read only 1 csv file

df = pd.read_csv("Data/Raw/01_fund_master.csv")

print("=" * 50)
print("Dataset: 01_fund_master.csv")

print("\nshape:")
print(df.shape)

print("\nData types;")
print(df.dtypes)

print("\nFirst 5 rows:")
print(df.head())

import os   #to find the exact folder path of the script
print(os.getcwd())'''


import pandas as pd
import os

# Get all CSV files from Data/Raw folder
files = os.listdir("Data/Raw")

# Loop through each file
for file in files:

    print("\n" + "=" * 50)
    print("Dataset:", file)

    # Read CSV file
    df = pd.read_csv("Data/Raw/" + file)

    # Print shape
    print("\nShape:")
    print(df.shape)

    # Print data types
    print("\nData Types:")
    print(df.dtypes)

    # Print first 5 rows
    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Records:")
    print(df.duplicated().sum())

    print("\nStatistical Summary:")
    print(df.describe())