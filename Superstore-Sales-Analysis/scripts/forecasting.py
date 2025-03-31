import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

# Load dataset
df = pd.read_csv("data/SampleSuperstore.csv")

# Convert 'Order Date' to datetime and aggregate sales by date
df["Order Date"] = pd.to_datetime(df["Order Date"])
df = df.groupby("Order Date")["Sales"].sum().reset_index()

# Rename columns to match Prophet's expected format
df.columns = ["ds", "y"]

# Initialize and fit the Prophet model
model = Prophet()
model.fit(df)

# Create future dataframe for predictions
future = model.make_future_dataframe(periods=90)  # Predict next 90 days
forecast = model.predict(future)

# Plot the forecast
plt.figure(figsize=(12, 6))
model.plot(forecast)
plt.title("Sales Forecasting for the Next 90 Days")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid()
plt.savefig("output/sales_forecast.png")  # Save the forecast plot
plt.show()

print("Forecasting script executed successfully. Forecast plot saved in output folder.")

# Save forecasted data
forecast.to_csv("output/sales_forecast.csv", index=False)
print("Forecast data saved as 'output/sales_forecast.csv'")
