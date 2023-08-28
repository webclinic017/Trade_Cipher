import streamlit as st
import time
import requests
import pandas as pd
import json

import http.client

st.markdown("""
<a target="_blank" href="https://shareasale.com/r.cfm?b=1517949&amp;u=3574798&amp;m=57542&amp;urllink=&amp;afftrack="><img src="https://static.shareasale.com/image/57542/generic-728x90-green_00.jpg" border="0" alt="Buy Gold and Silver" /></a>
""", unsafe_allow_html=True)

# Add divider line
st.markdown("---")

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

st.sidebar.text("Watch Bloomberg Video 24/7")

st.sidebar.video('https://www.youtube.com/watch?v=DxmDPrfinXY')

# Add divider line
st.markdown("---")

st.sidebar.text("Watch CNBC Live 24/7")

st.sidebar.video('https://www.youtube.com/watch?v=9NyxcX3rhQs')

st.markdown("""
<a href="https://click.linksynergy.com/fs-bin/click?id=8WC05bHq4DI&offerid=817940.369&subid=0&type=4"><IMG border="0"   alt="Microsoft365 for Business" src="https://ad.linksynergy.com/fs-bin/show?id=8WC05bHq4DI&bids=817940.369&subid=0&type=4&gridnum=16"></a>
""", unsafe_allow_html=True)

conn = http.client.HTTPSConnection("seeking-alpha-finance.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "62b008b623mshaf55ca1e208d945p1256acjsn8ca0e82661f6",
    'X-RapidAPI-Host': "seeking-alpha-finance.p.rapidapi.com"
}

conn.request("GET", "/v1/screeners/tickers?screener_id=96793299", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

def get_api_data():
    url = "https://seeking-alpha-finance.p.rapidapi.com/v1/screeners/tickers"
    querystring = {"screener_id": "96793299"}
    headers = {
        "X-RapidAPI-Key": "62b008b623mshaf55ca1e208d945p1256acjsn8ca0e82661f6",
        "X-RapidAPI-Host": "seeking-alpha-finance.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

def main():
    st.title("Seeking Alpha API Data")
    st.write("Fetching data from the API...")

    # Get the data from the API
    data = get_api_data()

    if data:
        # Convert data to a JSON string and prettify it
        json_string = json.dumps(data, indent=4)

        # Display the JSON response using st.code() to maintain formatting
        st.write("API Response (Raw JSON):")
        st.code(json_string, language="json")

        # Convert data to a pandas DataFrame
        df = pd.DataFrame(data)

        # Display the DataFrame with st.dataframe()
        st.write("API Response (Parsed Data):")
        st.dataframe(df)

        # Display the DataFrame as an HTML table with custom styling
        st.write("API Response (Formatted Table):")
        st.table(df.style.set_table_attributes("style='display:inline-block'").set_caption("API Data"))

    else:
        st.write("Failed to fetch data from the API. Please check your API key and connection.")

if __name__ == "__main__":
    main()
