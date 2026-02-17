# Fraud Risk Monitoring Dashboard
## Problem Statement
Financial transaction systems generate large volumes of data, making it difficult for fraud monitoring teams to quickly identify high-risk behavior.  
The objective of this project is to build an interactive analytics dashboard that highlights fraud trends, monitors key risk metrics, and enables faster investigation through data-driven insights.
## Overview
This project demonstrates an end-to-end fraud analytics workflow using Python and Power BI. The goal is to monitor transaction risk patterns, detect fraud trends, and provide business-level insights through interactive dashboards.

## Tools Used
- Python (Pandas, NumPy)
- Power BI
- Data Cleaning & EDA
- KPI Reporting & Visualization
## Data Preparation Workflow
The data pipeline was built using Python scripts to ensure clean and scalable analytics.

### Step 1 — Data Loading & Cleaning
- Loaded raw transaction dataset
- Handled missing values and data formatting
- Prepared structured tables for analysis

### Step 2 — KPI Engineering & Aggregation
- Calculated fraud rate metrics
- Created hourly transaction aggregations
- Generated amount-based risk buckets

### Step 3 — Power BI Export
- Exported clean datasets for visualization
- Ensured analytics-ready structure for dashboard modeling
## Dashboard Design
The dashboard was designed to provide a clear fraud monitoring experience with a business-focused layout:

- **Top Section:** KPI summary cards for quick risk overview
- **Middle Section:** Interactive hour filter (slicer)
- **Bottom Section:** Trend analysis and risk comparison visuals

The layout prioritizes clarity, interactivity, and fast decision-making.

## Key Features
### 🔹 Hourly Fraud Trend (Line Chart)
Displays fraud rate changes throughout the day to identify peak risk periods.
  ![Hourly Fraud Trend](Images/hourly-fraud-trend.png)

## 🔹 Amount Risk Analysis (Column Chart)
Highlights fraud distribution across different transaction amount ranges.
  ![Amount Risk Analysis](Images/amount-risk-analysis..png)

- KPI Monitoring (Transactions, Fraud Count, Fraud Rate)

  ![Dashboard Overview](Images/dashboard-overview.png)

## Business Value
This dashboard helps fraud and risk teams quickly identify high-risk transaction windows and patterns to support proactive monitoring.

## Author
Naveen Kumar Challa