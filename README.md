<<<<<<< HEAD

# 📈 Stock Analyzer Dashboard (Python GUI)

A desktop-based stock analysis application built using Python that allows users to visualize historical stock price trends using an interactive graphical interface.

---

## 📌 Project Overview

The Stock Analyzer Dashboard is a GUI-based application that reads historical stock data from CSV files and plots the closing price of selected stocks over time.  
The application is designed to be simple, visual, and user-friendly.

---

## ✨ Features

- Graphical user interface using Tkinter
- Multiple stock selection via checkboxes
- Line chart visualization of stock prices
- Proper units:
  - X-axis → Time (Date)
  - Y-axis → Price (USD)
- Dark-themed dashboard with background image
- Error handling for missing or invalid data
- Can be packaged as a standalone executable (.exe)

---

## 🛠 Technologies Used

- **Python 3**
- **Tkinter** – GUI framework
- **Pandas** – Data reading and processing
- **Matplotlib** – Plotting and visualization
- **Pillow (PIL)** – Background image handling
- **PyInstaller** – Executable generation

---

## 📂 Project Structure
stock_analyzer/

│

├── stock_gui.py # Main application file

├── bg_img.jpg # Background image for GUI

├── stock_data/ # Folder containing stock CSV files

│ ├── AAPL_data.csv

│ ├── MSFT_data.csv

│ └── TSLA_data.csv

├── README.md



## ▶️ How to Run the Application

### 1️⃣ (Optional) Create a virtual environment
python -m venv stock_env

stock_env\Scripts\activate

### 2️⃣ Install required libraries
pip install pandas matplotlib pillow

### 3️⃣ Run the program

## 📊 How the Application Works

1. Stock data is stored locally in CSV files.
2. The GUI allows users to select one or more stocks.
3. When the plot button is clicked:
   - The CSV files are read using Pandas.
   - Data is cleaned and converted to numeric format.
   - Closing prices are plotted using Matplotlib.
4. The chart displays:
   - Time (Date) on the X-axis
   - Price in USD on the Y-axis

---

## 🧾 CSV File Format

The application expects CSV files in the following structure:
Price,Close,High,Low,Open,Volume
Ticker,AAPL,AAPL,AAPL,AAPL,AAPL
Date,,,,,
2025-12-10,278.77,279.75,276.44,277.75,33038300

## 🏗 Creating an Executable (.exe)

### 1️⃣ Install PyInstaller
pip install pyinstaller

### 2️⃣ Generate the executable
pyinstaller --onefile --windowed stock_gui.py

### 3️⃣ Find the executable



## 🎯 Intended Use

- Learning GUI development with Python
- Understanding data visualization workflows
- Demonstrating CSV data processing
- Academic mini-project or portfolio project

---

## 🔮 Possible Enhancements

- Live stock data fetching
- More technical indicators
- Export charts as images
- Date range selection
- Interactive zoom and tooltips

---

## 📜 License / Attribution

This project **was created by Avinash D** for personal and educational purposes.  
All rights are reserved. No one else may claim authorship or redistribute this work as their own.

You are welcome to view and learn from this project, but any public use, reposting, or redistribution **must credit Avinash D**.

=======
# Stock-Analyzer-GUI
Python GUI to visualize and analyze stock prices
>>>>>>> 3e8c63a8db104b4e998b71b2c7c45311a32b7840
