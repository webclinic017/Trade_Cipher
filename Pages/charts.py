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
st.title('Streaming Stock Market Charts')

# Get stock symbol from user
ticker = st.text_input('Enter a stock symbol:', '')

# Create empty figure
fig = plt.figure()

# Download stock data
tickerData = yf.Ticker(ticker)

# Create streaming plot
def create_plot():
    df = tickerData.history(period="1mo")
    plt.plot(df['Close'])
    st.pyplot()

# Run streaming plot
if st.checkbox('Show streaming plot'):
    create_plot()

# Set title
st.title('Streaming Stock Market Charts')

# Get stock symbol from user
ticker = st.text_input('Enter a stock symbol:', '')

# Create empty figure
fig = plt.figure()

# Download stock data
tickerData = yf.Ticker(ticker)

# Create streaming plot
def create_plot():
    df = tickerData.history(period="3mo")
    plt.plot(df['Close'])
    st.pyplot()

# Run streaming plot
if st.checkbox('Show streaming plot'):
    create_plot()
