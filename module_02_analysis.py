# Module 02 - Data Analysis with Python
import pandas as pd
import numpy as np

df = pd.read_csv("retail_sales_raw.csv")
print("Dataset shape:", df.shape)
print("\nMissing values before cleaning:\n", df.isnull().sum())

df["Date"] = pd.to_datetime(df["Date"])
for col in ["Quantity", "Unit_Price", "Discount", "Customer_Rating"]:
    df[col] = df[col].fillna(df[col].median())

df = df.drop_duplicates().copy()
df["Gross_Sales"] = df["Quantity"] * df["Unit_Price"]
df["Net_Sales"] = df["Gross_Sales"] * (1 - df["Discount"])

print("\nMissing values after cleaning:\n", df.isnull().sum())
print("\nMean net sales:", round(np.mean(df["Net_Sales"]), 2))
print("\nSales by category:\n", df.groupby("Category")["Net_Sales"].sum())
print("\nSales by region:\n", df.groupby("Region")["Net_Sales"].sum())

df.to_csv("retail_sales_cleaned.csv", index=False)
print("\nCleaned data exported.")
