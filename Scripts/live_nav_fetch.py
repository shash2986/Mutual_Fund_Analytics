import requests
import pandas as pd

scheme_codes = [
    119551,  # SBI Bluechip
    120503,  # ICICI Bluechip
    118632,  # Nippon Large Cap
    119092,  # Axis Bluechip
    120841   # Kotak Bluechip
]

for code in scheme_codes:

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data["data"])

    filename = f"Data/Raw/nav_{code}.csv"

    df.to_csv(
        filename,
        index=False
        )

    print(f"Scheme {code} saved successfully!")

    #print(df.head())

    #print(response.status_code)