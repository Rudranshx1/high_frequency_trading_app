# 📈 Dynamic High Frequency Trading Strategy for Indian Stocks

A **Streamlit-based trading application** that implements a **Moving
Average Crossover Strategy** using stock data from **Yahoo Finance
(yfinance)**. The app allows users to dynamically adjust strategy
parameters and visualize buy/sell signals on Indian stocks.

------------------------------------------------------------------------

## 🚀 Features

-   📊 **Fetch Indian Stock Data**
    -   Uses **Yahoo Finance (yfinance)** API to fetch historical stock
        prices.
-   ⚡ **Dynamic Parameter Selection**
    -   Adjustable **short** and **long moving average windows**.\
    -   Custom **date range** selection.\
    -   Select **any NSE stock symbol** (e.g., `RELIANCE.NS`).
-   🔄 **Moving Average Crossover Strategy**
    -   Generates **Buy (▲)** and **Sell (▼)** signals when short MA
        crosses long MA.\
    -   Displays stock price with **technical indicators**.
-   📉 **Interactive Visualization**
    -   Line plot of stock price, short MA, long MA.\
    -   Buy signals marked in **green ▲**.\
    -   Sell signals marked in **red ▼**.

------------------------------------------------------------------------

## 🖥️ UI Layout

-   **Sidebar Controls**
    -   Stock symbol input (e.g., `RELIANCE.NS`).\
    -   Date range selectors.\
    -   Sliders for **short MA** and **long MA**.\
    -   Refresh button to reload data.
-   **Main Panel**
    -   Interactive chart with price, moving averages, and buy/sell
        signals.

------------------------------------------------------------------------

## ⚙️ Technical Implementation

-   **Data Source** → `yfinance` for stock price data.\
-   **Strategy** → Moving Average Crossover.
    -   Buy signal when **Short MA \> Long MA**.\
    -   Sell signal when **Short MA \< Long MA**.\
-   **Visualization** → `matplotlib` integrated with **Streamlit**.

------------------------------------------------------------------------

## 📦 Installation

Clone this repository:

``` bash
git clone https://github.com/your-username/hft-indian-stocks.git
cd hft-indian-stocks
```

Install dependencies:

``` bash
pip install streamlit yfinance pandas numpy matplotlib
```

Run the app:

``` bash
streamlit run app.py
```

------------------------------------------------------------------------

## 🔮 Future Enhancements

-   🔔 Add **real-time data streaming**\
-   📊 Backtesting framework for performance evaluation\
-   🤖 Integration with **machine learning-based strategies**\
-   💹 Portfolio optimization and risk management tools

------------------------------------------------------------------------

## 🧑‍💻 Developer

**Rudransh Kumar Ahluwalia**\
MBA FinTech
