"""Load and clean the IBM Telco Customer Churn dataset.

Usage:
    from src.data_prep import load_clean_data
    df = load_clean_data()
"""
from pathlib import Path

import pandas as pd

RAW_PATH = Path(__file__).resolve().parents[1] / "data" / "raw" / "telco_customer_churn.csv"


def load_raw_data(path: Path = RAW_PATH) -> pd.DataFrame:
    """Read the raw CSV exactly as downloaded."""
    return pd.read_csv(path)


def load_clean_data(path: Path = RAW_PATH) -> pd.DataFrame:
    """Return a cleaned copy of the dataset.

    Cleaning steps:
    - TotalCharges is stored as text and contains blank strings for
      brand-new customers (tenure == 0); convert to numeric.
    - Churn is converted from "Yes"/"No" to 1/0 as the target column.
    - customerID is kept as an identifier but should not be used as a feature.

    Decide yourself how to handle the missing TotalCharges values
    (drop, fill with 0, or impute) and record the reasoning in the README.
    """
    df = load_raw_data(path)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"].str.strip(), errors="coerce")
    df["Churn"] = (df["Churn"] == "Yes").astype(int)
    return df


if __name__ == "__main__":
    data = load_clean_data()
    print(data.shape)
    print(data.isna().sum()[data.isna().sum() > 0])
    print(f"Churn rate: {data['Churn'].mean():.1%}")
