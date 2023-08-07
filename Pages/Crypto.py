import streamlit as st
import time
import requests
import pandas as pd

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
        # Convert data to a pandas DataFrame
        df = pd.DataFrame(data)

        # Convert DataFrame to HTML table
        table_html = df.to_html(index=False, escape=False)

        # Display the HTML table using components.html()
        st.write("API Response:")
        st.components.v1.html(table_html, height=500)
    else:
        st.write("Failed to fetch data from the API. Please check your API key and connection.")

if __name__ == "__main__":
    main()