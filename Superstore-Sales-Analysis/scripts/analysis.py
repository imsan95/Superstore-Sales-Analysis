import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure output directory exists
output_dir = "../output"
os.makedirs(output_dir, exist_ok=True)

# Load dataset
file_path = "../data/SampleSuperstore.csv"
try:
    df = pd.read_csv("data/SampleSuperstore.csv")
    print("✅ File loaded successfully!\n")
except FileNotFoundError:
    print(f"❌ File not found: {"data/SampleSuperstore.csv"}")
    exit()

# Display first 5 rows
print(df.head())

# Convert 'Order Date' to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Remove duplicates
df.drop_duplicates(inplace=True)

# Check for missing values
missing_values = df.isnull().sum()
print("\nMissing Values:\n", missing_values)

# Summary statistics
print("\nSummary Statistics:\n", df.describe())

# ---- SALES BY CATEGORY ----
category_sales = df.groupby("Category")[["Sales", "Profit"]].sum()

plt.figure(figsize=(8,5))
sns.barplot(x=category_sales.index, y=category_sales["Sales"], palette="viridis")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid()
plt.savefig(os.path.join(output_dir, "sales_by_category.png"))
plt.show()

# ---- SALES BY SUB-CATEGORY ----
subcategory_sales = df.groupby("Sub-Category")[["Sales", "Profit"]].sum().sort_values(by="Sales", ascending=False)

plt.figure(figsize=(12,6))
sns.barplot(x=subcategory_sales.index, y=subcategory_sales["Sales"], palette="coolwarm")
plt.title("Sales by Sub-Category")
plt.xlabel("Sub-Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid()
plt.savefig(os.path.join(output_dir, "sales_by_subcategory.png"))
plt.show()

# ---- MONTHLY SALES TREND ----
df["Month"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12,6))
sns.lineplot(x=monthly_sales.index.astype(str), y=monthly_sales.values, marker="o", color="blue")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid()
plt.savefig(os.path.join(output_dir, "monthly_sales_trend.png"))
plt.show()

# ---- PROFIT DISTRIBUTION ----
plt.figure(figsize=(8,5))
sns.histplot(df["Profit"], bins=50, kde=True, color="red")
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.grid()
plt.savefig(os.path.join(output_dir, "profit_distribution.png"))
plt.show()

# ---- STATE-WISE SALES & PROFIT ----
state_sales = df.groupby("State")[["Sales", "Profit"]].sum().sort_values(by="Sales", ascending=False)

plt.figure(figsize=(14,6))
sns.barplot(x=state_sales.index, y=state_sales["Sales"], palette="coolwarm")
plt.title("State-wise Sales")
plt.xlabel("State")
plt.ylabel("Total Sales")
plt.xticks(rotation=90)
plt.grid()
plt.savefig(os.path.join(output_dir, "state_sales.png"))
plt.show()

plt.figure(figsize=(14,6))
sns.barplot(x=state_sales.index, y=state_sales["Profit"], palette="viridis")
plt.title("State-wise Profit")
plt.xlabel("State")
plt.ylabel("Total Profit")
plt.xticks(rotation=90)
plt.grid()
plt.savefig(os.path.join(output_dir, "state_profit.png"))
plt.show()

print("\n✅ EDA completed. All analysis results are saved in the 'output' folder.")
