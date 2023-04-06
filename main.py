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

st.title('BYOB is here with Trade Cipher! Bring Your Own Broker is the future!')

st.markdown("""
<a href="https://click.linksynergy.com/fs-bin/click?id=8WC05bHq4DI&offerid=1207190.332&subid=0&type=4"><IMG border="0"   alt="Newegg" src="https://ad.linksynergy.com/fs-bin/show?id=8WC05bHq4DI&bids=1207190.332&subid=0&type=4&gridnum=1"></a>
""", unsafe_allow_html=True)

option = st.sidebar.selectbox("Which Dashboard?", ('Main Page', 'Trade', 'Model Performance Analysis', 'TC Social', 'Charts','Twitter DB','RSI Dashboard'), 3)

st.sidebar.header("Trade Cipher Tools")

st.sidebar.header("Stock and Crypto Watchlist")

# Create an empty list to store the watchlist
watchlist = []

def add_to_watchlist(symbol):
    watchlist.append(symbol)
    return f"{symbol} added to watchlist."


# Create a form to add new symbols to the watchlist
new_symbol = st.text_input("Enter a stock or crypto symbol to add to your watchlist:")
if new_symbol:
    result = add_to_watchlist(new_symbol)
    st.success(result)

# Display the current watchlist
if watchlist:
    st.header("My Watchlist")
    st.write(watchlist)
else:
    st.warning("Your watchlist is empty.")

st.sidebar.text("Watch Bloomberg Video 24/7")

st.sidebar.video('https://www.youtube.com/watch?v=DxmDPrfinXY')

st.sidebar.text("Watch CNBC Live 24/7")

st.sidebar.video('https://www.youtube.com/watch?v=9NyxcX3rhQs')

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("Violet and Light Green Modern Gradient Financial Consultant Finance Animated Logo.png")

with col3:
    st.write(' ')

st.markdown("<h2 style='text-align: center; color: white;'>Select a dashboard to get started: </h2>" , unsafe_allow_html = True)

st.markdown("""
<a href="https://click.linksynergy.com/fs-bin/click?id=8WC05bHq4DI&offerid=817940.369&subid=0&type=4"><IMG border="0"   alt="Microsoft365 for Business" src="https://ad.linksynergy.com/fs-bin/show?id=8WC05bHq4DI&bids=817940.369&subid=0&type=4&gridnum=16"></a>
""", unsafe_allow_html=True)

import streamlit as st

option = st.selectbox("Select a dashboard below...", ('Main Page','Trade', 'Model Performance Analysis', 'TC Social', 'Charts', 'Twitter DB', 'RSI Dashboard'))

if option == 'Main Page':
    st.title('Welcome to Trade Cipher!')

    from PIL import Image

    image = Image.open('S&P500.png')

    st.image(image , use_column_width = True)

    st.markdown("""
    Our trading app makes it simple to help traders and investors make the right choices when trading various trading instruments!"""
    """ You can view historical market data, View investment indicators, and place trades using your preferred trading platform and much more!
    """)

    # Set title
st.title('Business News')

import requests
import streamlit as st

def fetch_news():
    url = "https://api.newscatcherapi.com/v2/search"
    querystring = {"q":"\"Business\"","lang":"en","sort_by":"relevancy","page":"1"}
    headers = {
        "x-api-key": "1m114J3QeX2h8UabjijTrWKjTcWhtft-bnHXnUm70QU"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

# Set the font family and size using HTML tags
html = f"<div style='font-family: Arial; font-size: 12pt;'>{fetch_news()}</div>"
# Write the HTML to the Streamlit app
st.write(html, unsafe_allow_html=True)


if option == 'TC Social':
    
import streamlit as st
import pandas as pd
import numpy as np
import os

# Create a Streamlit app
def app():
    st.set_page_config(page_title='Simple Social Media Platform', page_icon=':smiley:')
    st.title('Simple Social Media Platform')
    
    st.sidebar.header('User Profile')
    username = st.sidebar.text_input('Enter your username')
    
    st.sidebar.header('Actions')
    action = st.sidebar.selectbox('Select an action', ('Create Post', 'View Posts'))
    
    # Implement the 'Create Post' action
    if action == 'Create Post':
        st.header('Create a New Post')
        post_title = st.text_input('Enter the post title')
        post_content = st.text_area('Enter the post content')
        if st.button('Create'):
            new_post = {'Username': username, 'Title': post_title, 'Content': post_content}


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

# Download data
df = yf.download(option,start= start_date,end= end_date, progress=False)

# Bollinger Bands
indicator_bb = BollingerBands(df['Close'])
bb = df
bb['bb_h'] = indicator_bb.bollinger_hband()
bb['bb_l'] = indicator_bb.bollinger_lband()
bb = bb[['Close','bb_h','bb_l']]

# Moving Average Convergence Divergence
macd = MACD(df['Close']).macd()

symbol = st.sidebar.text_input("Ticker Symbol" , value = 'LTZBLD' , max_chars = 6)
    
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


# Plot Closing Price of Query Symbol
    def price_plot(symbol) :
        df = pd.DataFrame(data[symbol].Close)
        df['Date'] = df.index
        plt.fill_between(df.Date , df.Close , color = 'skyblue' , alpha = 0.3)
        plt.plot(df.Date , df.Close , color = 'skyblue' , alpha = 0.8)
        plt.xticks(rotation = 90)
        plt.title(symbol , fontweight = 'bold')
        plt.xlabel('Date' , fontweight = 'bold')
        plt.ylabel('Closing Price' , fontweight = 'bold')
        return st.pyplot()


    num_company = st.sidebar.slider('Drag the slider to view the Number of Companies in a plot' , 1 , 10)

    if st.button('Show Plots') :
        st.header('Stock Closing Price')
        for i in list(df_selected_sector.Symbol)[:num_company] :
            price_plot(i)

    fig , ax = plt.subplots()
    ax.scatter([1 , 2 , 3] , [1 , 2 , 3])
    assert isinstance(fig , object)
    st.pyplot(fig)

    st.set_option('deprecation.showPyplotGlobalUse' , False)


