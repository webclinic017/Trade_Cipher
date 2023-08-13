import requests
import streamlit as st
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

        # Set a unique index for the DataFrame
        df.set_index("Company Name", inplace=True)  # Replace with an actual unique column name

        # Display the DataFrame as an HTML table with custom styling
        st.write("API Response (Formatted Table):")
        st.table(df.style.set_table_attributes("style='display:inline-block'").set_caption("API Data"))

    else:
        st.write("Failed to fetch data from the API. Please check your API key and connection.")

if __name__ == "__main__":
    main()
