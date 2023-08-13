import streamlit as st
import time
import requests
import pandas as pd
import json

import http.client

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
