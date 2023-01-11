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
import pandas.data as web
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