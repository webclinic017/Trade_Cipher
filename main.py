import config
import streamlit as st
import plotly as pl
import requests as r
import tweepy
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yfinance as yf
import django as dj
import pandas_datareader as web
import datetime as dt
import mplfinance as mpf
import plotly.graph_objects as go
from fastapi import FastAPI
from django.db import models

option = st.sidebar.selectbox("Which Dashboard?", ('twitter', 'wallstreetbets', 'TC Social', 'chart', 'pattern'), 3)

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


if option == 'Model Performance Analysis':

    st.subheader("Model Performance Analysis")

    import matplotlib.pyplot as plt
    import pandas as pd

    #Where the data is

    data='C:\\Users\\mrtye\\Desktop\\Blockchain Projects\\SandP500App\\Tradecipher\\db.sqlite3'

    #Set benchmark to compare with

    bm = 'SPXTR'

    bm_name = 'S&P 500 Total Return'

    # These are the saved performance csv files from our book models.

    strat_names = {
        "trend_model" : "Core Trend Strategy",
        "time_return" : "Time Return Strategy",
        "counter_trend" : "Counter Trend Strategy",
        "curve_trading" : "Curve Trading Strategy",
        "systematic_momentum" : "Equity Momentum Strategy",

    }
    #Pick one to analyze

    strat = 'curve_trading'

    # Look up the name

    strat_name = strat_names[strat]

    # Read the strategy
    df = pd.read_csv('C:\\Users\\mrtye\\Desktop\\' + strat + '.csv', index_col = 0,
                     parse_dates=True, names=[strat])

    #Read the benchmark
    df[bm_name]=pd.read_csv('C:\\Users\\mrtye\\Desktop\\curve_trading' + '.csv', index_col = 0,
                            parse_dates=[0] , delim_whitespace=True)

    # Limit history to end of 2018 for the book

    df = df.loc[:'2018-12-31']

    # Print confirmation that all's done

    num_days = st.sidebar.slider('Number of days' , 1 , 30 , 3)

    cursor.execute("""
           SELECT COUNT(*) AS num_mentions, symbol
           FROM mention JOIN stock ON stock.id = mention.stock_id
           WHERE date(dt) > current_date - interval '%s day'
           GROUP BY stock_id, symbol   
           HAVING COUNT(symbol) > 10
           ORDER BY num_mentions DESC
       """ , (num_days ,))

    counts = cursor.fetchall()
    for count in counts :
        st.write(count)

    cursor.execute("""
           SELECT symbol, message, url, dt, username
           FROM mention JOIN stock ON stock.id = mention.stock_id
           ORDER BY dt DESC
           LIMIT 100
       """)

    mentions = cursor.fetchall()
    for mention in mentions :
        st.text(mention['dt'])
        st.text(mention['symbol'])
        st.text(mention['message'])
        st.text(mention['url'])
        st.text(mention['username'])

    rows = cursor.fetchall()

    st.write(rows)

    symbol = st.sidebar.text_input("Ticker Symbol", value='LTZBLD', max_chars=6)
    symbol = st.sidebar.text_input("Symbol" , value = 'MSFT' , max_chars = None , key = None , type = 'default')

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

    st.components.v1.iframe("http://trade.ironbeam.com" , width = 1111 , height = 700 , scrolling = True)

    st.components.v1.iframe("http://trade.oanda.com/" , width = 1000 , height = 700 , scrolling = True)

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

if option == 'RSI Dashboard':
    st.subheader("Relative Strength Index Dashboard")

#!/usr/bin/env python3

import datetime
import random
import time
from urllib.request import urlopen

import matplotlib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas_datareader.data as web
import pylab
from mplfinance.original_flavor import candlestick_ohlc
from pandas.core.common import flatten
from tabulate import tabulate

matplotlib.rcParams.update({'font.size': 9})

stocks = []

# If stocks array is empty, pull stock list from stocks.txt file
stocks = stocks if len(stocks) > 0 else [
    line.rstrip() for line in open("C:\\Users\\tyrone.canion\\Desktop\\Projects\\Trade_Cipher-main\\stocks.txt", "r")]

# Time frame you want to pull data from
start = datetime.datetime.now()-datetime.timedelta(days=365)
end = datetime.datetime.now()

if __name__ == "__main__":

    # Array of moving averages you want to get
    MAarr = [20, 200]

    allData = []

    for ticker in stocks:

        try:
            data = []

            print("Pulling data for " + ticker)

            stock = Stock(ticker, start, end)

            # Append data to array
            data.append(ticker.upper())

            data.append(stock.closes[-1])

            for MA in MAarr:
                computedSMA = stock.SMA(period=MA)
                # print(computedSMA)
                data.append(computedSMA[-1])

            currentRsi = float("{:.2f}".format(stock.rsi[-1]))

            if currentRsi > 70:
                data.append(str(currentRsi) + " 🔥")
            elif currentRsi < 30:
                data.append(str(currentRsi) + " 🧊")
            else:
                data.append(currentRsi)

            chartLink = "https://finance.yahoo.com/quote/" + ticker + "/chart?p=" + ticker

            data.append(chartLink)

            allData.append(data)

            # Shows chart only if current RSI is greater than or less than 70 or 30 respectively
            if currentRsi < 30 or currentRsi > 70:

                stock.graph(MAarr)

        except Exception as e:
            print('Error: ', str(e))

    print(tabulate(allData, headers=flatten([
        'Stock', 'Price', [str(x) + " MA" for x in MAarr], "RSI", "chart"])))




