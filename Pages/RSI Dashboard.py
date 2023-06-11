 # Import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import random
import time
from urllib.request import urlopen
import matplotlib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pylab
from mplfinance.original_flavor import candlestick_ohlc
from pandas.core.common import flatten
from tabulate import tabulate
import yfinance as yf # https://pypi.org/project/yfinance/
import ta as ta
from ta import add_all_ta_features
from ta.utils import dropna
from ta.trend import MACD
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands

import yfinance as yf
import datetime
import streamlit as st
import ta

# Define the Streamlit app
st.sidebar.title("Stock RSI Dashboard")

symbol = st.sidebar.text_input("Enter stock symbol (e.g. AAPL for Apple):", "AAPL")
start_date = st.sidebar.date_input("Start date:", value=datetime.date(2015, 1, 1))
end_date = st.sidebar.date_input("End date:", value=datetime.date.today())
rsi_period = st.sidebar.slider("RSI period:", min_value=1, max_value=50, value=14)

# Retrieve the stock data from the yfinance API
stock_data = yf.download(symbol, start=start_date, end=end_date)

# Calculate the RSI
rsi_indicator = ta.momentum.RSIIndicator(stock_data["Close"], window=rsi_period)
rsi = rsi_indicator.rsi()

# Display the results
st.title("Stock RSI Dashboard")

st.write(f"## Stock symbol: {symbol}")
st.write(f"### Date range: {start_date} to {end_date}")
st.write(f"### RSI period: {rsi_period} days")

st.line_chart(stock_data["Close"])
st.line_chart(rsi)

# Display the results
st.title("Stock RSI Dashboard")

st.write(f"## Stock symbol: {symbol}")
st.write(f"### Date range: {start_date} to {end_date}")
st.write(f"### RSI period: {rsi_period} days")

st.line_chart(stock_data["Close"])
st.line_chart(rsi)

###########
# sidebar #
###########
option = st.sidebar.selectbox('Select one symbol', ( 'AAPL', 'MSFT',"SPY",'WMT'))
import datetime
today = datetime.date.today()
before = today - datetime.timedelta(days=700)
start_date = st.sidebar.date_input('Start date', before)
end_date = st.sidebar.date_input('End date', today)
if start_date < end_date:
    st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.sidebar.error('Error: End date must fall after start date.')
