import pandas as pd
import os

# Folder where your CSVs are saved
data_folder = r"C:\Users\avich\Desktop\stock_analyzer"
csv_files = [f for f in os.listdir(data_folder) if f.endswith("_data.csv")]

for csv_file in csv_files:
    filepath = os.path.join(data_folder, csv_file)
    try:
        # Read CSV without parsing header first
        raw_df = pd.read_csv(filepath, header=None)

        # First row is ticker repeated, second row is actual header
        raw_df.columns = raw_df.iloc[1]   # Set second row as header
        df = raw_df[2:].copy()            # Drop first two rows
        df.reset_index(drop=True, inplace=True)

        # Keep only the standard columns
        df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]

        # Convert Date to datetime and numeric columns to float
        df["Date"] = pd.to_datetime(df["Date"])
        for col in ["Open", "High", "Low", "Close", "Volume"]:
            df[col] = df[col].astype(float)

        # Set Date as index
        df.set_index("Date", inplace=True)

        # Calculate moving averages and daily % change
        df["MA_5"] = df["Close"].rolling(5).mean()
        df["MA_10"] = df["Close"].rolling(10).mean()
        df["Daily Change %"] = df["Close"].pct_change() * 100

        # Save analyzed CSV
        ticker = csv_file.split("_")[0]
        analyzed_file = os.path.join(data_folder, f"{ticker}_data_analyzed.csv")
        df.to_csv(analyzed_file)
        print(f"✅ {ticker} analyzed and saved as {analyzed_file}")

    except Exception as e:
        print(f"❌ Failed to analyze {csv_file}: {e}")
