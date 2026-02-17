import os
import pandas as pd

CLEAN_PATH = "data/processed/clean.csv"

def main():
    os.makedirs("outputs/reports", exist_ok=True)

    df = pd.read_csv(CLEAN_PATH)

    # KPI Summary
    kpis = {
        "total_rows": len(df),
        "total_amount": df["amount"].sum(),
        "avg_amount": df["amount"].mean(),
        "fraud_rate": df["fraud_flag"].mean()
    }

    print("KPI Summary:")
    print(kpis)

    # Daily KPIs (using hour since dataset has no date)
    daily = df.groupby("hour").agg(
        transactions=("amount","count"),
        total_amount=("amount","sum"),
        fraud_count=("fraud_flag","sum"),
        fraud_rate=("fraud_flag","mean")
    ).reset_index()

    daily.to_csv("outputs/reports/daily_kpis.csv", index=False)

    print("✅ Reports saved in outputs/reports/")

if __name__ == "__main__":
    main()
