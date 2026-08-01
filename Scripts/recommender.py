import pandas as pd
import numpy as np

# Loading the latest Sharpe Ratio report
latest_sharpe = pd.read_csv("../Reports/latest_sharpe_report.csv")

# Assigning Risk Grade
latest_sharpe["risk_grade"] = np.select(
    [
        latest_sharpe["rolling_sharpe"] >= 2,
        latest_sharpe["rolling_sharpe"] >= 1,
        latest_sharpe["rolling_sharpe"] < 1
    ],
    [
        "Low",
        "Moderate",
        "High"
    ],
    default="High"
)


def recommend_funds(risk_level):
    """
    Recommend the Top 3 mutual funds
    based on the selected risk appetite.
    """

    recommendations = (
        latest_sharpe[
            latest_sharpe["risk_grade"].str.lower() == risk_level.lower()
        ]
        .sort_values("rolling_sharpe", ascending=False)
        .head(3)
    )

    return recommendations


if __name__ == "__main__":

    risk = input("Enter Risk Appetite (Low/Moderate/High): ")

    print("\nTop 3 Recommended Funds:\n")

    print(recommend_funds(risk))