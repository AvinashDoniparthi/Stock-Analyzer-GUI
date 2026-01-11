import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

STOCK_DATA_DIR = "C:/Users/avich/Desktop/stock_analyzer"
stocks = ["AAPL", "MSFT", "TSLA"]

plt.figure(figsize=(14,7))

for stock in stocks:
    file_path = os.path.join(STOCK_DATA_DIR, f"{stock}_data.csv")
    if os.path.exists(file_path):
        df = pd.read_csv(
            file_path,
            skiprows=2,
            names=["Date","Close","High","Low","Open","Volume"],
            parse_dates=["Date"],
            index_col="Date"
        )
        plt.plot(df.index, df["Close"], label=stock)
    else:
        print(f"❌ File not found: {stock}_data.csv")

plt.title("Stock Close Price Comparison")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.legend()
plt.grid(True)

# Format x-axis to show fewer, rotated date labels
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45, ha='right')

plt.tight_layout()  # prevent clipping of labels
plt.show()
