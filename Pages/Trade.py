import streamlit as st

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

st.sidebar.header("Trade Cipher Tools")

import streamlit as st
import plotly.graph_objects as go

# Define a header for the app
st.header("Stock/Crypto Watchlist")

# Create an empty list to store the watchlist
watchlist = []

# Define a function to add symbols to the watchlist
def add_to_watchlist(symbol):
    watchlist.append(symbol.upper())
    return "{symbol.upper()} added to watchlist."

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

# Add divider line
st.markdown("---")

st.sidebar.text("Watch CNBC Live 24/7")

st.sidebar.video('https://www.youtube.com/watch?v=9NyxcX3rhQs')

st.markdown("""
<a href="https://click.linksynergy.com/fs-bin/click?id=8WC05bHq4DI&offerid=817940.369&subid=0&type=4"><IMG border="0"   alt="Microsoft365 for Business" src="https://ad.linksynergy.com/fs-bin/show?id=8WC05bHq4DI&bids=817940.369&subid=0&type=4&gridnum=16"></a>
""", unsafe_allow_html=True)
