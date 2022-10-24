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
import pandas_datareader as web
import datetime as dt
import mplfinance as mpf
import plotly.graph_objects as go
import js2py
from django.db import models


option = st.sidebar.selectbox("Which Dashboard?", ('Main Page', 'Trade', 'Model Performance Analysis', 'TC Social', 'Charts','Twitter DB','RSI Dashboard'), 3)

st.sidebar.header("Trade Cipher Tools")

st.sidebar.text("Watch Bloomberg Video 24/7")

st.sidebar.video('https://www.youtube.com/watch?v=DxmDPrfinXY')

st.sidebar.text("Live BTC/ETH Signals")

st.sidebar.video('https://www.youtube.com/watch?v=ADqqo73uaJA')

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("Violet and Light Green Modern Gradient Financial Consultant Finance Animated Logo.png")

with col3:
    st.write(' ')

st.markdown("<h2 style='text-align: center; color: white;'>Select a dashboard to get started: </h2>" , unsafe_allow_html = True)

option = st.selectbox("Select a dashboard below...", ('Main Page','Trade', 'Model Performance Analysis', 'TC Social', 'Charts', 'Twitter DB', 'RSI Dashboard'))

if option == 'Main Page':
    st.title('View and collect historical index data and more')

    from PIL import Image

    image = Image.open('S&P500.png')

    st.image(image , use_column_width = True)

    st.markdown("""
    This app retrieves the list of the **S&P 500** (from Wikipedia) and its corresponding **stock closing price** (year-to-date)!
    * **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
    * **Data source:** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
    """)

    st.sidebar.header('User Input Features')


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


    # Download S&P500 data
    # https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
    def filedownload(df) :
        csv = df.to_csv(index = False)
        b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
        href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
        return href


    st.markdown(filedownload(df_selected_sector) , unsafe_allow_html = True)

    # https://pypi.org/project/yfinance/

    data = yf.download(
        tickers = list(df_selected_sector[:10].Symbol) ,
        period = "ytd" ,
        interval = "1d" ,
        group_by = 'ticker' ,
        auto_adjust = True ,
        prepost = True ,
        threads = True ,
        proxy = None
    )


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

 #This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '1fdbee66-c1d9-45ee-9942-90f3270866f2',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

if option == 'TC Social':
    st.subheader("Trade Cipher Social Platform")

    symbol = st.sidebar.text_input("Symbol" , value = 'AAPL' , max_chars = 5)
    
import streamlit as st
from streamlit_chat import message
import requests

st.header("Trade Cipher Chat")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text 

if option == 'Model Performance Analysis':

    st.subheader("Model Performance Analysis")
   
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

    st.components.v1.iframe("https://platform.nadex.com/npwa/#/app" , width = 1000 , height = 700 , scrolling = True)

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

    symbol = st.sidebar.text_input("Ticker Symbol" , value = 'LTZBLD' , max_chars = 6)

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
import pandas_datareader.data as web
import pylab
from mplfinance.original_flavor import candlestick_ohlc
from pandas.core.common import flatten
from tabulate import tabulate
import yfinance as yf # https://pypi.org/project/yfinance/
import ta as ta
from ta import add_all_ta_features
from ta.utils import dropna
from ta.volatility import BollingerBands
from ta.trend import MACD
from ta.momentum import RSIIndicator

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

# Resistence Strength Indicator
rsi = RSIIndicator(df['Close']).rsi()

###################
# Set up main app #
###################

# Plot the prices and the bolinger bands
st.write('Stock Bollinger Bands')
st.line_chart(bb)

progress_bar = st.progress(0)

# Plot MACD
st.write('Stock Moving Average Convergence Divergence (MACD)')
st.area_chart(macd)

# Plot RSI
st.write('Stock RSI')
st.line_chart(rsi)

# Data of recent days
st.write('Recent data')
st.dataframe(df.tail(10))

def to_excel(df):
    output = df.to_excel
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    val = to_excel(df)
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="download.xlsx">Download excel file</a>' # decode b'abc' => abc

st.markdown(get_table_download_link(df), unsafe_allow_html=True)
