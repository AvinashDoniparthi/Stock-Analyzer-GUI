import os
import pandas as pd
import matplotlib.pyplot as plt

STOCK_DATA_DIR = os.getcwd()
plt.style.use('ggplot')  # works out of the box

files = [f for f in os.listdir(STOCK_DATA_DIR) if f.endswith(".csv")]

for file in files:
    try:
        # Skip rows 1 and 2, first row is actual header
        df = pd.read_csv(
            os.path.join(STOCK_DATA_DIR, file),
            skiprows=[1,2],  # skip Ticker and extra Date row
            index_col=0,
            parse_dates=True
        )

        # Convert numeric columns
        numeric_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        df.dropna(inplace=True)

        # Daily % change
        df['Daily Change %'] = df['Close'].pct_change() * 100

        # Save analyzed CSV
        analyzed_file = file.replace('.csv', '_analyzed.csv')
        df.to_csv(os.path.join(STOCK_DATA_DIR, analyzed_file))
        print(f"✅ Successfully analyzed {file}")

        # Plot Close price
        plt.figure(figsize=(10,5))
        plt.plot(df.index, df['Close'], label='Close Price')
        plt.title(file.replace('.csv',''))
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

    except Exception as e:
        print(f"❌ Failed to analyze {file}: {e}")
