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

# ---- 1. SALES DISTRIBUTION ----
plt.figure(figsize=(8,5))
sns.histplot(df["Sales"], bins=50, kde=True, color="blue")
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.grid()
plt.savefig(f"{output_dir}/sales_distribution.png")
plt.close()

# ---- 2. SALES BY CATEGORY ----
category_sales = df.groupby("Category")[["Sales", "Profit"]].sum()

plt.figure(figsize=(8,5))
sns.barplot(x=category_sales.index, y=category_sales["Sales"], palette="viridis")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.grid()
plt.savefig(f"{output_dir}/sales_by_category.png")
plt.close()

# ---- 3. MONTHLY SALES TREND ----
df["Month"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12,6))
sns.lineplot(x=monthly_sales.index.astype(str), y=monthly_sales.values, marker="o", color="green")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid()
plt.savefig(f"{output_dir}/monthly_sales_trend.png")
plt.close()

# ---- 4. TOP 10 PERFORMING SUB-CATEGORIES ----
subcategory_sales = df.groupby("Sub-Category")[["Sales", "Profit"]].sum().sort_values(by="Sales", ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=subcategory_sales.index, y=subcategory_sales["Sales"], palette="coolwarm")
plt.title("Top 10 Sub-Categories by Sales")
plt.xlabel("Sub-Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid()
plt.savefig(f"{output_dir}/top_subcategories_sales.png")
plt.close()

# ---- 5. STATE-WISE SALES & PROFIT ----
state_sales = df.groupby("State")[["Sales", "Profit"]].sum().sort_values(by="Sales", ascending=False)

plt.figure(figsize=(14,6))
sns.barplot(x=state_sales.index, y=state_sales["Sales"], palette="coolwarm")
plt.title("State-wise Sales")
plt.xlabel("State")
plt.ylabel("Total Sales")
plt.xticks(rotation=90)
plt.grid()
plt.savefig(f"{output_dir}/state_sales.png")
plt.close()

plt.figure(figsize=(14,6))
sns.barplot(x=state_sales.index, y=state_sales["Profit"], palette="viridis")
plt.title("State-wise Profit")
plt.xlabel("State")
plt.ylabel("Total Profit")
plt.xticks(rotation=90)
plt.grid()
plt.savefig(f"{output_dir}/state_profit.png")
plt.close()

# ---- 6. PROFIT DISTRIBUTION ----
plt.figure(figsize=(8,5))
sns.histplot(df["Profit"], bins=50, kde=True, color="red")
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.grid()
plt.savefig(f"{output_dir}/profit_distribution.png")
plt.close()

# ---- 7. DISCOUNT IMPACT ON PROFIT ----
plt.figure(figsize=(8,5))
sns.scatterplot(x=df["Discount"], y=df["Profit"], alpha=0.5, color="purple")
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.grid()
plt.savefig(f"{output_dir}/discount_vs_profit.png")
plt.close()

# ---- 8. CORRELATION MATRIX ----
plt.figure(figsize=(8,6))
sns.heatmap(df[["Sales", "Profit", "Quantity", "Discount"]].corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Matrix")
plt.savefig(f"{output_dir}/correlation_matrix.png")
plt.close()

# ---- 9. TOP 10 CUSTOMERS BY SALES & PROFIT ----
top_customers = df.groupby("Customer Name")[["Sales", "Profit"]].sum().sort_values(by="Sales", ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=top_customers.index, y=top_customers["Sales"], palette="viridis")
plt.title("Top 10 Customers by Sales")
plt.xlabel("Customer Name")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid()
plt.savefig(f"{output_dir}/top_customers_sales.png")
plt.close()

print("✅ EDA script executed successfully! Check the 'output/' directory.")
