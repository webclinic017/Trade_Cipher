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
