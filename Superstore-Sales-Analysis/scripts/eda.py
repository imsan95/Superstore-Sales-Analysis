import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure output directory exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Load dataset
df = pd.read_csv("data/SampleSuperstore.csv")

# Convert 'Order Date' to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Remove duplicates
df.drop_duplicates(inplace=True)

# Summary statistics
df.describe().to_csv(f"{output_dir}/summary_statistics.csv")

# Check for missing values
with open(f"{output_dir}/missing_values.txt", "w") as f:
    f.write(str(df.isnull().sum()))

# 1. Sales Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Sales"], bins=50, kde=True)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.savefig(f"{output_dir}/sales_distribution.png")  # Save plot
plt.close()

# 2. Sales by Category
category_sales = df.groupby("Category")[["Sales", "Profit"]].sum()

plt.figure(figsize=(8,5))
sns.barplot(x=category_sales.index, y=category_sales["Sales"])
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.savefig(f"{output_dir}/sales_by_category.png")  # Save plot
plt.close()

# 3. Monthly Sales Trend
df["Month"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12,6))
sns.lineplot(x=monthly_sales.index.astype(str), y=monthly_sales.values, marker="o")
plt.xticks(rotation=45)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid()
plt.savefig(f"{output_dir}/monthly_sales_trend.png")  # Save plot
plt.close()

print("EDA script executed successfully, check the 'output/' directory.")
