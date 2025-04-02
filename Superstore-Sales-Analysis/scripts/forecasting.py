import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet
import os

# Ensure output directory exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Load dataset
df = pd.read_csv("data/SampleSuperstore.csv")

# Convert 'Order Date' to datetime and aggregate sales by date
df["Order Date"] = pd.to_datetime(df["Order Date"])
df = df.groupby("Order Date")["Sales"].sum().reset_index()

# Handle missing values (if any)
df = df.dropna()

# Rename columns to match Prophet's expected format
df.columns = ["ds", "y"]

# Initialize Prophet model with seasonality
model = Prophet(yearly_seasonality=True, daily_seasonality=False, weekly_seasonality=True)
model.add_seasonality(name="quarterly", period=90, fourier_order=8)

# Fit the model
model.fit(df)

# Create future dataframe for predictions (next 90 days)
future = model.make_future_dataframe(periods=90)

# Generate forecast
forecast = model.predict(future)

# ---- PLOT FORECAST ----
plt.figure(figsize=(12, 6))
model.plot(forecast)
plt.title("Sales Forecasting for the Next 90 Days")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid()
plt.savefig(f"{output_dir}/sales_forecast.png")  # Save the forecast plot
plt.close()

# ---- PLOT COMPONENTS ----
fig = model.plot_components(forecast)
plt.savefig(f"{output_dir}/forecast_components.png")
plt.close()

# Save forecast data
forecast.to_csv(f"{output_dir}/sales_forecast.csv", index=False)

print("✅ Forecasting script executed successfully. Check 'output/' folder for results.")
