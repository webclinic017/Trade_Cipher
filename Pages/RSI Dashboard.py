import streamlit as st
import yfinance as yf
import ta
import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc

# Add divider line
st.markdown("---")

# Disclaimer
st.markdown("## Disclaimer")
st.markdown("Trading stocks involves risk. This app is for informational purposes only and does not constitute financial advice. Please exercise caution and do your own research before making any investment decisions.")

# Add divider line
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("Violet and Light Green Modern Gradient Financial Consultant Finance Animated Logo.png")

with col3:
    st.write(' ')

st.markdown("<h2 style='text-align: center; color: white;'>Select a dashboard to get started: </h2>" , unsafe_allow_html = True)

#st.markdown("<h1 style='text-align: center;'>BYOB is here with Trade Cipher! Bring Your Own Broker is the future!</h1>", unsafe_allow_html=True)

# Add divider line
st.markdown("---")

option = st.sidebar.selectbox("Which Dashboard?", ('Main Page', 'Trade', 'Model Performance Analysis', 'TC Social', 'Charts','Twitter DB','RSI Dashboard'), 3)

import streamlit as st
import yfinance as yf
import ta
import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc

# Centered title
st.markdown("<h1 style='text-align: center;'>Stock RSI Dashboard</h1>", unsafe_allow_html=True)

# Add divider line
st.markdown("---")

# Description of RSI
st.markdown("## What is the Relative Strength Index (RSI)?")
st.markdown("The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. "
            "It oscillates between 0 and 100 and is commonly used to identify overbought or oversold conditions in a stock. "
            "RSI values above 70 are generally considered overbought, while values below 30 are considered oversold.")

# How to search for RSI information
st.markdown("## How to Search for a Company's RSI Information")
st.markdown("1. Enter a stock symbol in the text input field on the left sidebar.")
st.markdown("2. Choose the start and end dates for the data range.")
st.markdown("3. Adjust the RSI period using the slider on the left sidebar.")
st.markdown("4. Select the desired chart type from the dropdown menu on the left sidebar.")
st.markdown("5. The stock's price chart and RSI chart will be displayed in the main section of the app based on your selections.")

# Add divider line
st.markdown("---")

# Sidebar inputs
st.sidebar.markdown("<h3 style='text-align: center;'>Stock Selection</h3>", unsafe_allow_html=True)
symbol = st.sidebar.text_input("Enter a symbol (e.g., AAPL, MSFT, SPY, WMT)")
today = datetime.date.today()
before = today - datetime.timedelta(days=700)
start_date = st.sidebar.date_input("Start date", before)
end_date = st.sidebar.date_input("End date", today)

if start_date < end_date:
    st.sidebar.success(f"Start date: {start_date}\n\nEnd date: {end_date}")
else:
    st.sidebar.error("Error: End date must be after start date.")

try:
    # Retrieve the stock data from the yfinance API
    stock_data = yf.download(symbol, start=start_date, end=end_date)

    # Calculate the RSI
    rsi_period = st.sidebar.slider("RSI period", min_value=1, max_value=50, value=14)
    rsi_indicator = ta.momentum.RSIIndicator(stock_data["Close"], window=rsi_period)
    rsi = rsi_indicator.rsi()

    # Chart type selection
    chart_type = st.sidebar.selectbox("Select chart type", ("Line", "Bar", "Area", "Candlestick"))

    # Display the results
    st.subheader(f"Stock symbol: {symbol}")
    st.write(f"Date range: {start_date} to {end_date}")
    st.write(f"RSI period: {rsi_period} days")

    # Choose chart type
    if chart_type == "Line":
        st.line_chart(stock_data["Close"])
        st.line_chart(rsi)
    elif chart_type == "Bar":
        st.bar_chart(stock_data["Close"])
        st.line_chart(rsi)
    elif chart_type == "Area":
        st.area_chart(stock_data["Close"])
        st.line_chart(rsi)
    elif chart_type == "Candlestick":
        # Convert the stock data to a format suitable for candlestick charting
        ohlc_data = stock_data[["Open", "High", "Low", "Close"]].reset_index()
        ohlc_data["Date"] = ohlc_data["Date"].map(mdates.date2num)

        # Create a subplot with the appropriate axis labels
        fig, ax = plt.subplots()
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")

        # Plot the candlestick chart
        candlestick_ohlc(ax, ohlc_data.values, width=0.6, colorup="g", colordown="r")

        # Format the x-axis dates
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
        fig.autofmt_xdate()

        # Add the RSI chart
        ax_rsi = ax.twinx()
        ax_rsi.plot(stock_data.index, rsi, color="purple")
        ax_rsi.axhline(30, color="green", linestyle="--")
        ax_rsi.axhline(70, color="red", linestyle="--")
        ax_rsi.set_ylabel("RSI")

        # Add a title
        plt.title(f"{symbol} Stock Price with RSI")

        # Display the chart
        st.pyplot(fig)

except Exception as e:
    st.error("Error: Unable to retrieve stock data. Please check the entered symbol and date range.")

# Add divider line
st.markdown("---")

st.markdown("""
<a href="https://click.linksynergy.com/fs-bin/click?id=8WC05bHq4DI&offerid=1207190.332&subid=0&type=4"><IMG border="0"   alt="Newegg" src="https://ad.linksynergy.com/fs-bin/show?id=8WC05bHq4DI&bids=1207190.332&subid=0&type=4&gridnum=1"></a>
""", unsafe_allow_html=True)
