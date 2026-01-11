import pandas as pd

# Load CSV with multi-level columns
df = pd.read_csv("AAPL_data.csv", header=[0,1], index_col=0)
df.index.name = "Date"

# Print columns to check
print("Columns before renaming:", df.columns)

# Flatten columns properly
df.columns = ["Close", "High", "Low", "Open", "Volume"]

print("Columns after renaming:", df.columns)
print("\nFirst 5 rows:")
print(df.head())

# Daily % change
df["Daily Change %"] = df["Close"].pct_change() * 100

# Moving averages
df["MA_5"] = df["Close"].rolling(window=5).mean()
df["MA_10"] = df["Close"].rolling(window=10).mean()

# Highest & lowest close price
highest_close = df["Close"].max()
lowest_close = df["Close"].min()

print("\nStatistics:")
print(f"Highest Close: {highest_close}")
print(f"Lowest Close: {lowest_close}")

# Save analyzed data
df.to_csv("AAPL_data_analyzed.csv")
print("\nAnalyzed data saved to AAPL_data_analyzed.csv")
