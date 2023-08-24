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
import pandas as pd
from urllib.request import urlopen
import certifi
import json
import plotly.express as px

def get_jsonparsed_data(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

def main():
    st.title("Stock Dividend Calendar")

    url = ("https://financialmodelingprep.com/api/v3/stock_dividend_calendar?from=2020-01-01&to=2023-12-31&apikey=7871663557cbf06ab075c5ba73a7098f")
    st.write("Fetching data from:", url)

    try:
        data = get_jsonparsed_data(url)
        df = pd.DataFrame(data)

        st.write("Dividend Data:")
        numeric_columns = df.select_dtypes(include=['number']).columns
        st.dataframe(df.style.highlight_max(axis=0), height=600)
        
        # Convert date column to datetime
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

        # Create a calendar heatmap using Plotly
        fig = px.scatter(df, x='date', y='symbol', text='amount', color='amount', 
                         color_continuous_scale='Viridis', title='Dividend Calendar')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='top center')
        fig.update_xaxes(type='category')

        st.plotly_chart(fig)
        
    except Exception as e:
        st.error("An error occurred: " + str(e))

if __name__ == "__main__":
    main()
