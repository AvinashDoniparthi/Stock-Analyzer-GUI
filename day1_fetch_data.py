import yfinance as yf
import pandas as pd
from datetime import datetime

# List of stocks you want to fetch
tickers = ["AAPL", "MSFT", "TSLA"]  # Add more tickers if you want

# Fetch data
for ticker in tickers:
    try:
        # Download data for last 30 days
        df = yf.download(ticker, period="30d", interval="1d")
        
        # Save CSV 
        filename = f"{ticker}_data.csv"
        df.to_csv(filename)
        print(f"✅ {ticker} data fetched and saved as {filename}")
    except Exception as e:
        print(f"❌ Failed to fetch {ticker}: {e}")

#Last fetch date
print(f"\nData last fetched: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
