import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Function to fetch data
def fetch_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

# Define a simple moving average crossover strategy
def moving_average_crossover(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['Price'] = data['Close']
    signals['Short_MA'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    signals['Long_MA'] = data['Close'].rolling(window=long_window, min_periods=1).mean()
    signals['Signal'] = 0.0
    signals['Signal'][short_window:] = np.where(signals['Short_MA'][short_window:] > signals['Long_MA'][short_window:], 1.0, 0.0)
    signals['Position'] = signals['Signal'].diff()
    return signals

# Streamlit app
st.title('Dynamic High Frequency Trading Strategy for Indian Stocks')

st.sidebar.header('Strategy Parameters')
symbol = st.sidebar.text_input('Stock Symbol (e.g., RELIANCE.NS)', 'RELIANCE.NS')
start_date = st.sidebar.date_input('Start Date', pd.to_datetime('2023-01-01'))
end_date = st.sidebar.date_input('End Date', pd.to_datetime('2023-12-31'))
short_window = st.sidebar.slider('Short Moving Average Window', 1, 50, 5)
long_window = st.sidebar.slider('Long Moving Average Window', 1, 50, 20)

if st.sidebar.button('Refresh Data'):
    data = fetch_data(symbol, start_date, end_date)
    signals = moving_average_crossover(data, short_window, long_window)

    # Plot the data
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(data.index, data['Close'], label='Price')
    ax.plot(signals.index, signals['Short_MA'], label='Short MA')
    ax.plot(signals.index, signals['Long_MA'], label='Long MA')

    # Plot buy signals
    ax.plot(signals.loc[signals['Position'] == 1.0].index, 
             signals['Short_MA'][signals['Position'] == 1.0],
             '^', markersize=10, color='g', lw=0, label='Buy Signal')

    # Plot sell signals
    ax.plot(signals.loc[signals['Position'] == -1.0].index, 
             signals['Short_MA'][signals['Position'] == -1.0],
             'v', markersize=10, color='r', lw=0, label='Sell Signal')

    ax.set_title(f'Moving Average Crossover Strategy for {symbol}')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()

    st.pyplot(fig)
else:
    st.write("Click 'Refresh Data' to load the stock data and apply the strategy.") 