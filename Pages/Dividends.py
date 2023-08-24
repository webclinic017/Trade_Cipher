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

st.markdown("<h1 style='text-align: center;'>BYOB is here with Trade Cipher! Bring Your Own Broker is the future!</h1>", unsafe_allow_html=True)

# Add divider line
st.markdown("---")

import streamlit as st
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

import certifi
import json

def get_jsonparsed_data(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

def main():
    st.title("Stock Dividend Calendar")

    url = ("https://financialmodelingprep.com/api/v3/stock_dividend_calendar?from=2020-06-01&to=2020-09-10&apikey=YOUR_API_KEY")
    st.write("Fetching data from:", url)

    try:
        data = get_jsonparsed_data(url)
        st.json(data)
    except Exception as e:
        st.error("An error occurred: " + str(e))

if __name__ == "__main__":
    main()
