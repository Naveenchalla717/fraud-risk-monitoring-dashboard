import os
import pandas as pd

CLEAN_PATH = "data/processed/clean.csv"

def main():
    os.makedirs("outputs/powerbi", exist_ok=True)

    df = pd.read_csv(CLEAN_PATH)

    # 1) Sample transactions (Power BI friendly)
    sample = df.sample(n=min(20000, len(df)), random_state=42)
    sample.to_csv("outputs/powerbi/transactions_sample.csv", index=False)

    # 2) Amount bucket KPIs
    bucket = df.groupby("amount_bucket").agg(
        transactions=("amount", "count"),
        total_amount=("amount", "sum"),
        avg_amount=("amount", "mean"),
        fraud_count=("fraud_flag", "sum"),
        fraud_rate=("fraud_flag", "mean")
    ).reset_index()

    bucket.to_csv("outputs/powerbi/amount_buckets.csv", index=False)

    # 3) Hourly trend KPIs
    hourly = df.groupby("hour").agg(
        transactions=("amount", "count"),
        total_amount=("amount", "sum"),
        avg_amount=("amount", "mean"),
        fraud_count=("fraud_flag", "sum"),
        fraud_rate=("fraud_flag", "mean")
    ).reset_index()

    hourly.to_csv("outputs/powerbi/hourly_kpis.csv", index=False)

    print("✅ Power BI exports created in outputs/powerbi/")
    print("- transactions_sample.csv")
    print("- amount_buckets.csv")
    print("- hourly_kpis.csv")

if __name__ == "__main__":
    main()
