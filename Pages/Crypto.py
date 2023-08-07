import streamlit as st
import time

progress_text = st.empty()
my_bar = st.progress(0)

progress_text.markdown("**Just a moment while we prepare the environment!**")

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)

progress_text.markdown("**The environment is ready!**")

import requests
import streamlit

import streamlit as st
import requests

def fetch_api_data():
    url = "https://seeking-alpha-finance.p.rapidapi.com/v1/screeners/tickers"
    querystring = {"screener_id":"96793299"}
    headers = {
        "X-RapidAPI-Key": "62b008b623mshaf55ca1e208d945p1256acjsn8ca0e82661f6",
        "X-RapidAPI-Host": "seeking-alpha-finance.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

def main():
    st.title("Seeking Alpha Screeners")
    st.subheader("Stock/Crypto Screeners")

    # Get the data from the API
    data = get_api_data()

    if data:
        st.write("API Response:")
        st.json(data)
    else:
        st.write("Failed to fetch data from the API. Please check your API key and connection.")

if __name__ == "__main__":
    main()

url = "https://coinranking1.p.rapidapi.com/coins"

querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h","tiers[0]":"1","orderBy":"marketCap","orderDirection":"desc","limit":"50","offset":"0"}

headers = {
	"X-RapidAPI-Key": "d29531ae60msh09b292159b1d570p1db262jsnd2039bec5d98",
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

import http.client

conn = http.client.HTTPSConnection("alpha-vantage.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "62b008b623mshaf55ca1e208d945p1256acjsn8ca0e82661f6",
    'X-RapidAPI-Host': "alpha-vantage.p.rapidapi.com"
}

conn.request("GET", "/query?interval=5min&function=TIME_SERIES_INTRADAY&symbol=MSFT&datatype=json&output_size=compact", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
