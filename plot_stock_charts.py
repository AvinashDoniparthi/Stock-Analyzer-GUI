import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Use Seaborn style
sns.set_style("whitegrid")

# Load analyzed data
df = pd.read_csv("AAPL_data_analyzed.csv", index_col="Date", parse_dates=True)

# Plot Close Price and Moving Averages
plt.figure(figsize=(12,6))
plt.plot(df["Close"], label="Close Price", color="blue")
plt.plot(df["MA_5"], label="5-Day MA", color="orange")
plt.plot(df["MA_10"], label="10-Day MA", color="green")
plt.title("AAPL Stock Price with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend()
plt.tight_layout()
plt.show()

# Daily % Change Histogram
plt.figure(figsize=(10,5))
sns.histplot(df["Daily Change %"].dropna(), bins=20, kde=True, color="purple")
plt.title("Histogram of Daily % Change")
plt.xlabel("Daily Change %")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Optional: Close price over time with color gradient
plt.figure(figsize=(12,6))
plt.scatter(df.index, df["Close"], c=df["Close"], cmap="coolwarm", s=50)
plt.title("AAPL Close Price Scatter")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.colorbar(label="Price")
plt.tight_layout()
plt.show()
