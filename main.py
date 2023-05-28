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

import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("Violet and Light Green Modern Gradient Financial Consultant Finance Animated Logo.png")

with col3:
    st.write(' ')

st.markdown("<h2 style='text-align: center; color: white;'>Select a dashboard to get started: </h2>" , unsafe_allow_html = True)

st.title('BYOB is here with Trade Cipher! Bring Your Own Broker is the future!')

st.markdown("""
<a href="https://click.linksynergy.com/fs-bin/click?id=8WC05bHq4DI&offerid=1207190.332&subid=0&type=4"><IMG border="0"   alt="Newegg" src="https://ad.linksynergy.com/fs-bin/show?id=8WC05bHq4DI&bids=1207190.332&subid=0&type=4&gridnum=1"></a>
""", unsafe_allow_html=True)

option = st.sidebar.selectbox("Which Dashboard?", ('Main Page', 'Trade', 'Model Performance Analysis', 'TC Social', 'Charts','Twitter DB','RSI Dashboard'), 3)

st.markdown("""
<a target="_blank" href="https://shareasale.com/r.cfm?b=1517949&amp;u=3574798&amp;m=57542&amp;urllink=&amp;afftrack="><img src="https://static.shareasale.com/image/57542/generic-728x90-green_00.jpg" border="0" alt="Buy Gold and Silver" /></a>
""", unsafe_allow_html=True)


st.sidebar.header("Trade Cipher Tools")

st.sidebar.header("Stock and Crypto Watchlist")

import streamlit as st
import plotly.graph_objects as go

# Define a header for the app
st.header("Stock/Crypto Watchlist")

# Create an empty list to store the watchlist
watchlist = []

# Define a function to add symbols to the watchlist
def add_to_watchlist(symbol):
    watchlist.append(symbol.upper())
    return f"{symbol.upper()} added to watchlist."

# Use a form to collect input from users
with st.form("Add Symbol"):
    st.write("Enter a stock or crypto symbol to add to your watchlist:")
    new_symbol = st.text_input("Symbol")
    add_button = st.form_submit_button("Add")

# Add new symbols to the watchlist
if new_symbol and add_button:
    result = add_to_watchlist(new_symbol)
    st.success(result)

# Display the current watchlist
if watchlist:
    st.header("My Watchlist")

    # Use icons to represent different symbols
    for symbol in watchlist:
        if "BTC" in symbol:
            st.image("btc.png", width=30)
        elif "ETH" in symbol:
            st.image("eth.png", width=30)
        else:
            st.write(symbol)

    # Use data visualization to provide insights about the watchlist
    fig = go.Figure()
    for symbol in watchlist:
        fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6], name=symbol.upper()))

    fig.update_layout(title="Price Trend")
    st.plotly_chart(fig)
else:
    st.warning("Your watchlist is empty.")

# Add custom CSS to style the app
st.markdown(
    """
    <style>
    body {
        font-family: Arial, Helvetica, sans-serif;
    }
    h1, h2, h3, h4, h5, h6 {
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.text("Watch Bloomberg Video 24/7")

st.sidebar.video('https://www.youtube.com/watch?v=DxmDPrfinXY')

st.sidebar.text("Watch CNBC Live 24/7")

st.sidebar.video('https://www.youtube.com/watch?v=9NyxcX3rhQs')

st.markdown("""
<a href="https://click.linksynergy.com/fs-bin/click?id=8WC05bHq4DI&offerid=817940.369&subid=0&type=4"><IMG border="0"   alt="Microsoft365 for Business" src="https://ad.linksynergy.com/fs-bin/show?id=8WC05bHq4DI&bids=817940.369&subid=0&type=4&gridnum=16"></a>
""", unsafe_allow_html=True)

import streamlit as st

option = st.selectbox("Select a dashboard below...", ('Main Page','News','Trade', 'Model Performance Analysis', 'TC Social', 'Charts', 'Twitter DB', 'RSI Dashboard'))

if option == 'Main Page':
    st.title('Welcome to Trade Cipher!')

    from PIL import Image

    image = Image.open('S&P500.png')

    st.image(image , use_column_width = True)

    st.markdown("""
    Our trading app makes it simple to help traders and investors make the right choices when trading various trading instruments!"""
    """ You can view historical market data, View investment indicators, and place trades using your preferred trading platform and much more!
    """)

import requests
import streamlit as st

import streamlit as st
import requests

if option == 'News':
    
    st.header("Business News")

# set the API endpoint and parameters
url = "https://newsapi.org/v2/top-headlines?country=us&category=business"
params = {"country": "us", "apiKey": "e05f54f819fb43b4b67385072ad1db10"}

# make the API request and retrieve the data
response = requests.get(url, params=params)
data = response.json()

# display the data in the Streamlit app with formatting

st.markdown(
    """
    <div style='text-align: center;'>
        <h1>Business News</h1>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("Here are the top headlines in business:")
for article in data["articles"]:
    st.write("## " + article["title"])
    st.write(article["description"])
    st.write(f"Source: {article['source']['name']}  Published: {article['publishedAt']}")
    st.write("---")


# Set the font family and size using HTML tags
html = f"<div style='font-family: Arial; font-size: 12pt </div>"
# Write the HTML to the Streamlit app
st.write(html, unsafe_allow_html=True)


if option == 'TC Social':
    
    st.header("Coming Soon")

if option == 'Performance Analysis':

    st.subheader("Performance Analysis")
    
     # Web scraping of S&P 500 data
    #
    @st.cache
    def load_data() :
        url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
        html = pd.read_html(url , header = 0)
        df = html[0]
        return df


    df = load_data()
    sector = df.groupby('GICS Sector')

    # Sidebar - Sector selection
    sorted_sector_unique = sorted(df['GICS Sector'].unique())
    selected_sector = st.sidebar.multiselect('Sector' , sorted_sector_unique , sorted_sector_unique)

    # Filtering data
    df_selected_sector = df[(df['GICS Sector'].isin(selected_sector))]

    st.header('Display Companies in Selected Sector')
    st.write('Data Dimension: ' + str(df_selected_sector.shape[0]) + ' rows and ' + str(
        df_selected_sector.shape[1]) + ' columns.')
    st.dataframe(df_selected_sector)

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

import streamlit as st
import yfinance as yf
import ta
import datetime

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

if option == 'Trade':

    st.subheader("Trade")

    st.markdown("<h2 style='text-align: center; color: white;'>Trade Traditional investment instruments, FOREX and Crypto</h2>" , unsafe_allow_html = True)

    from ibapi.client import EClient
    from ibapi.wrapper import EWrapper


    class IBapi(EWrapper , EClient) :
        def __init__(self) :
            EClient.__init__(self , self)


    app = IBapi()
    app.connect('127.0.0.1' , 7497 , 123)
    app.run()

    #Uncomment this section if unable to connect
    #and to prevent errors on a reconnect
    import time
    time.sleep(2)
    app.disconnect()
    ''

    st.components.v1.iframe("https://trade.ironbeam.com/login" , width = 1111 , height = 700 , scrolling = True)

    symbol = st.sidebar.text_input("Symbol" , value = 'MSFT' , max_chars = None , key = None , type = 'default')


if option == 'Twitter DB':
    st.subheader("Twitter Trader Info Dashboard")
    for username in config.TWITTER_USERNAMES :
        api = tweepy.API(auth)
        user = api.get_user(screen_name = 'dak')

        print(user.id)

        st.subheader(username)
        st.image(user.profile_image_url)

        for tweet in tweets :
            if '$' in tweet.text :
                words = tweet.text.split(' ')
                for word in words :
                    if word.startswith('$') and word[1 :].isalpha() :
                        symbol = word[1 :]
                        st.write(symbol)
                        st.write(tweet.text)
                        st.image(f"https://finviz.com/chart.ashx?t={symbol}")

    if option == 'chart' :
        symbol = st.sidebar.text_input("Symbol" , value = 'MSFT' , max_chars = None , key = None , type = 'default')

        data = pd.read_sql("""
            select date(day) as day, open, high, low, close
            from daily_bars
            where stock_id = (select id from stock where UPPER(symbol) = %s) 
            order by day asc""" , connection , params = (symbol.upper() ,))

        st.subheader(symbol.upper())

        fig = go.Figure(data = [go.Candlestick(x = data['day'] ,
                                               open = data['open'] ,
                                               high = data['high'] ,
                                               low = data['low'] ,
                                               close = data['close'] ,
                                               name = symbol)])

        fig.update_xaxes(type = 'category')
        fig.update_layout(height = 700)

        st.plotly_chart(fig , use_container_width = True)

        st.write(data)
        
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

##############
# Stock data #
##############

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from ta.volatility import BollingerBands
from ta.trend import MACD
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Stock Market Charts", page_icon=":chart_with_upwards_trend:")

# Define function to download stock data
def download_stock_data(symbol, start_date, end_date):
    df = yf.download(symbol, start=start_date, end=end_date, progress=False)
    return df

# Define function to plot Bollinger Bands
def plot_bollinger_bands(df):
    indicator_bb = BollingerBands(df['Close'])
    bb = df.copy()
    bb['bb_h'] = indicator_bb.bollinger_hband()
    bb['bb_l'] = indicator_bb.bollinger_lband()
    bb = bb[['Close','bb_h','bb_l']]
    return bb

# Define function to plot MACD
def plot_macd(df):
    macd = MACD(df['Close']).macd()
    return macd

# Define function to plot stock price
def plot_stock_price(df, symbol):
    fig, ax = plt.subplots()
    ax.fill_between(df.index, df['Close'], color='skyblue', alpha=0.3)
    ax.plot(df.index, df['Close'], color='skyblue', alpha=0.8)
    ax.set_xticklabels(df.index, rotation=90)
    ax.set_title(symbol, fontweight='bold')
    ax.set_xlabel('Date', fontweight='bold')
    ax.set_ylabel('Closing Price', fontweight='bold')
    return fig

# Define function to create streaming plot
def create_streaming_plot(tickerData):
    fig, ax = plt.subplots()
    plt.ion()
    while True:
        df = tickerData.history(period="3mo")
        ax.clear()
        ax.plot(df['Close'])
        plt.draw()
        plt.pause(1)

# Define page layout
header = st.beta_container()
main = st.beta_container()
sidebar = st.sidebar.beta_container()

# Define header
with header:
    st.title('Stock Market Charts')
    st.markdown('---')

# Define sidebar
with sidebar:
    symbol = st.text_input("Ticker Symbol", value='LTZBLD', max_chars=6)
    st.sidebar.markdown('---')
    st.sidebar.header('Number of Companies')
    num_company = st.sidebar.slider('Drag the slider to view the number of companies in a plot', 1, 10)

# Define main content
with main:
    # Download stock data
    df = download_stock_data(symbol, start_date='2021-01-01', end_date='2023-05-12')
    
    # Plot Bollinger Bands
    bb_df = plot_bollinger_bands(df)
    st.line_chart(bb_df)

    # Plot MACD
    macd_df = plot_macd(df)
    st.line_chart(macd_df)

    # Plot stock price
    fig = plot_stock_price(df, symbol)
    st.pyplot(fig)

    # Create streaming plot
    tickerData = yf.Ticker(symbol)
    if st.checkbox('Show streaming plot'):
        create_streaming_plot(tickerData)

    # Plot closing price of query symbol
    st.header('Stock Closing Price')
    for i in list(df_selected_sector.Symbol)[:num_company]:
        fig = plot_stock_price(data[i], i)
        st.pyplot(fig)

# Set global matplotlib option
