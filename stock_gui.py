import os
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, BooleanVar, Label
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import sys

# Helper to get path for files when running as EXE
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller EXE """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



# ---------------- CONFIG ----------------
STOCK_DATA_DIR = resource_path("stock_data")
AVAILABLE_STOCKS = ["AAPL", "MSFT", "TSLA"]

BG_COLOR = "#1e1e2f"
CARD_COLOR = "#2a2a40"
TEXT_COLOR = "#ffffff"

# ---------------- FUNCTIONS ----------------
def plot_selected_stocks():
    selected = [stock for stock, var in stock_vars.items() if var.get()]

    if not selected:
        messagebox.showwarning("No Selection", "Please select at least one stock")
        return

    plt.close("all")
    plt.figure(figsize=(15, 8))

    plotted = False

    for stock in selected:
        file_path = os.path.join(STOCK_DATA_DIR, f"{stock}_data.csv")

        if not os.path.exists(file_path):
            messagebox.showerror("Missing File", f"{stock}_data.csv not found")
            continue

        try:
            df = pd.read_csv(
                file_path,
                skiprows=2,
                names=["Date", "Close", "High", "Low", "Open", "Volume"],
                index_col="Date",
                parse_dates=["Date"],
                date_format="%Y-%m-%d"
            )
            df = df.apply(pd.to_numeric, errors="coerce")
            df = df.dropna(subset=["Close"])  # remove invalid Close
            df = df.sort_index()              # ensure chronological order
        except Exception as e:
            messagebox.showerror("Read Error", f"{stock}: {e}")
            continue

        if df.empty or "Close" not in df.columns:
            messagebox.showerror("Data Error", f"No valid 'Close' data for {stock}")
            continue

        plt.plot(df.index, df["Close"], label=stock)
        plotted = True

        # -------- Trend Box --------
        try:
            first = df["Close"].iloc[0]
            last = df["Close"].iloc[-1]
            pct_change = ((last - first) / first) * 100

            if pct_change > 0:
                trend_text = f"{stock} trend:\nUpward 📈\nChange: +{pct_change:.2f}%"
            elif pct_change < 0:
                trend_text = f"{stock} trend:\nDownward 📉\nChange: {pct_change:.2f}%"
            else:
                trend_text = f"{stock} trend:\nStable\nChange: 0.00%"

            plt.text(
                df.index[-1], df["Close"].iloc[-1],
                trend_text,
                fontsize=10, ha="right", va="bottom",
                bbox=dict(facecolor="white", alpha=0.5, boxstyle="round,pad=0.3")
            )
        except Exception:
            pass
        # ----------------------------

    if not plotted:
        return

    # -------- UNITS AND LABELS --------
    plt.title("Stock Closing Prices Over Time", fontsize=18, fontweight="bold")
    plt.xlabel("Time (Date)", fontsize=14)
    plt.ylabel("Price (USD)", fontsize=14)

    plt.gca().yaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, _: f"${x:,.2f}")
    )
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.4)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.show()

# ---------------- GUI ----------------
root = Tk()
root.title("Stock Analyzer")
root.geometry("1400x900")

# ---------- BACKGROUND IMAGE ----------
bg_image = Image.open(resource_path("bg_img.jpg"))
bg_image = bg_image.resize((1400, 900))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = bg_photo
# -------------------------------------

root.configure(bg=BG_COLOR)

# ---------------- STYLE ----------------
style = ttk.Style()
style.theme_use("default")

style.configure(
    "Title.TLabel",
    font=("Segoe UI", 24, "bold"),
    foreground=TEXT_COLOR,
    background=BG_COLOR
)

style.configure(
    "Card.TFrame",
    background=CARD_COLOR,
    padding=30
)

style.configure(
    "Stock.TCheckbutton",
    font=("Segoe UI", 14),
    foreground=TEXT_COLOR,
    background=CARD_COLOR
)

style.configure(
    "Big.TButton",
    font=("Segoe UI", 16, "bold"),
    padding=15
)

# ---------------- TITLE ----------------
title = ttk.Label(
    root,
    text="📈 Stock Analyzer Dashboard",
    style="Title.TLabel"
)
title.pack(pady=30)
title.lift()

# ---------------- CARD ----------------
card = ttk.Frame(root, style="Card.TFrame")
card.pack(pady=20)
card.lift()

subtitle = ttk.Label(
    card,
    text="Select stocks to analyze",
    font=("Segoe UI", 16, "bold"),
    foreground=TEXT_COLOR,
    background=CARD_COLOR
)
subtitle.pack(pady=(0, 20))
subtitle.lift()

# ---------------- CHECKBOXES ----------------
stock_vars = {}

for stock in AVAILABLE_STOCKS:
    var = BooleanVar(value=True)
    chk = ttk.Checkbutton(
        card,
        text=stock,
        variable=var,
        style="Stock.TCheckbutton"
    )
    chk.pack(anchor="w", pady=5)
    chk.lift()
    stock_vars[stock] = var

# ---------------- BUTTON ----------------
plot_button = ttk.Button(
    card,
    text="Plot Selected Stocks",
    style="Big.TButton",
    command=plot_selected_stocks
)
plot_button.pack(pady=30)
plot_button.lift()

root.mainloop()

