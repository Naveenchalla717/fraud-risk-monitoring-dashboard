import os
import pandas as pd
from scipy.io import arff

RAW_PATH = "data/raw/dataset_.arff"
OUT_PATH = "data/processed/clean.csv"

def main():
    os.makedirs("data/processed", exist_ok=True)

    print("Loading ARFF dataset...")

    data, meta = arff.loadarff(RAW_PATH)
    df = pd.DataFrame(data)

    # Fix column names
    df.columns = [c.lower() for c in df.columns]

    # Convert byte strings to normal
    for col in df.select_dtypes([object]).columns:
        df[col] = df[col].astype(str)

    # Rename class column
    df.rename(columns={"class": "fraud_flag"}, inplace=True)

    # Convert numeric columns
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["time"] = pd.to_numeric(df["time"], errors="coerce")

    # Map class labels to binary target
    fraud_map = {"otherwise": 0, "fraud": 1}
    raw_labels = df["fraud_flag"].str.strip().str.lower()
    df["fraud_flag"] = raw_labels.map(fraud_map)
    if df["fraud_flag"].isna().any():
        bad_values = sorted(raw_labels[df["fraud_flag"].isna()].dropna().unique())
        raise ValueError(f"Unexpected fraud_flag labels found: {bad_values}")
    df["fraud_flag"] = df["fraud_flag"].astype("int8")

    # Create extra features
    df["hour"] = (df["time"] // 3600) % 24

    df["amount_bucket"] = pd.cut(
        df["amount"],
        bins=[-1, 10, 50, 100, 200, 500, 1000, 10000, 999999],
        labels=["<=10", "10-50", "50-100", "100-200", "200-500", "500-1k", "1k-10k", "10k+"],
    )

    df.to_csv(OUT_PATH, index=False)

    print("Clean file created:", OUT_PATH)
    print(df.head())

if __name__ == "__main__":
    main()
