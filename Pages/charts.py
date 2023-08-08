# Import libraries
import streamlit as st
import pandas as pd
import yfinance as yf
import config
import streamlit as st
import plotly as pl
import requests as r
import pandas as pd
import base64
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import django as dj
import pandas as web
import datetime as dt
import mplfinance as mpf
import plotly.graph_objects as go
import js2py
from django.db import models

# Set title
st.title('Stock and Crypto Charts')

# Get stock symbol from user
ticker = st.text_input('Enter a stock/crypto symbol:', '')

# Create empty figure
fig = plt.figure()

# Download stock data
tickerData = yf.Ticker(ticker)

# Create streaming plot
def create_plot():
    df = tickerData.history(period="3mo")
    plt.plot(df['Close'])
    st.pyplot(fig)

# Run streaming plot
if st.checkbox('Show streaming plot'):
    create_plot()

# Create empty figure
fig = plt.figure()

# Download stock data
tickerData = yf.Ticker(ticker)

# Create streaming plot
def create_plot():
    df = tickerData.history(period="1d")
    plt.plot(df['Close'])
    st.pyplot()

import requests

import streamlit as st
import requests

# Set up the API request parameters
url = "https://seeking-alpha.p.rapidapi.com/market/get-realtime-quotes"
querystring = {"sa_ids": "612888,16123"}
headers = {
    "X-RapidAPI-Key": "62b008b623mshaf55ca1e208d945p1256acjsn8ca0e82661f6",
    "X-RapidAPI-Host": "seeking-alpha.p.rapidapi.com",
}

# Fetch data from the API
response = requests.get(url, headers=headers, params=querystring)
data = response.json()

# Display the data using Streamlit as HTML
st.title("Realtime Quotes")
st.write("API data from Seeking Alpha:")

# Check if the data is a list of dictionaries
if isinstance(data, list):
    html_data = "<ul>"
    for quote in data:
        symbol = quote.get("symbol", "N/A")
        last_price = quote.get("last_price", "N/A")
        html_data += f"<li><b>Symbol:</b> {symbol}, <b>Last Price:</b> {last_price}</li>"
    html_data += "</ul>"
    st.markdown(html_data, unsafe_allow_html=True)
else:
    st.write("Invalid data format")

