import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/SampleSuperstore.csv")

# Convert 'Order Date' to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Remove duplicates
df.drop_duplicates(inplace=True)

# Summary statistics
print(df.describe())

# Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

# 1. Sales Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Sales"], bins=50, kde=True)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# 2. Sales by Category
category_sales = df.groupby("Category")[["Sales", "Profit"]].sum()

plt.figure(figsize=(8,5))
sns.barplot(x=category_sales.index, y=category_sales["Sales"])
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

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
plt.show()
print("EDA script executed successfully")

plt.savefig("output/sales_distribution.png")
plt.savefig("output/sales_by_category.png")
plt.savefig("output/monthly_sales_trend.png")