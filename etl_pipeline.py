import pandas as pd

df = pd.read_csv("sales_data.csv")

print("Raw Data:\n", df)

df = df.drop_duplicates()
df["amount"] = pd.to_numeric(df["amount"])

region_sales = df.groupby("region")["amount"].sum().reset_index()

print("\nTransformed Data:\n", region_sales)

region_sales.to_csv("region_sales_output.csv", index=False)
