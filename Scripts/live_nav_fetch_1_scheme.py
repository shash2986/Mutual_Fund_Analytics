import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

print(data.keys())

print(data["meta"])

print(data["data"][0])

df = pd.DataFrame(data["data"])

print(df.head())

df.to_csv(
    "Data/Raw/live_nav_hdfc_top100.csv",
    index=False
)

print("CSV saved successfully!")