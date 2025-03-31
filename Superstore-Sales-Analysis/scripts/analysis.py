import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/SampleSuperstore.csv")

# Check if the file is loaded
print(df.head()) 

# Convert 'Order Date' to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Remove duplicates
df.drop_duplicates(inplace=True)

# Sales by Category
category_sales = df.groupby("Category")[["Sales", "Profit"]].sum()

# Plot
plt.figure(figsize=(8,5))
sns.barplot(x=category_sales.index, y=category_sales["Sales"])
plt.title("Sales by Category")
plt.show()
