# Import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

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