import requests
import streamlit as st

# Function to fetch Business News data
@st.cache
def get_business_news_data():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=business"
    params = {"country": "us", "apiKey": "e05f54f819fb43b4b67385072ad1db10"}
    response = requests.get(url, params=params)
    return response.json()["articles"]

# Function to fetch Wall Street Journal Articles data
@st.cache
def get_wall_street_journal_data():
    url = "https://newsapi.org/v2/everything?domains=wsj.com"
    params = {"apiKey": "e05f54f819fb43b4b67385072ad1db10"}
    response = requests.get(url, params=params)
    return response.json()["articles"]

# Create the tabs
tab1, tab2 = st.tabs(["Current Business News", "Wall Street Journal Articles"])

if tab1:  # Only fetch and display data if tab1 is selected
    st.header("Current Business News")

    # Fetch Business News data
    business_news_data = get_business_news_data()

    # Display the data in the Streamlit app with formatting
    st.markdown(
        """
        <div style='text-align: center;'>
            <h1>Business News</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("Here are the top headlines in business:")
    for article in business_news_data:
        st.write("## " + article["title"])
        st.write(article["description"])
        st.write(f"Source: {article['source']['name']}  Published: {article['publishedAt']}")
        st.write("---")

if tab2:  # Only fetch and display data if tab2 is selected
    st.header("Wall Street Journal Articles")

    # Fetch Wall Street Journal Articles data
    wall_street_journal_data = get_wall_street_journal_data()

    # Display the data in the Streamlit app with formatting
    st.markdown(
        """
        <div style='text-align: center;'>
            <h1>WSJ Articles</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("Here are the top articles from WSJ:")
    for article in wall_street_journal_data:
        st.write("## " + article["title"])
        st.write(article["description"])
        st.write(f"Source: {article['source']['name']}  Published: {article['publishedAt']}")
        st.write("---")
        st.write('url')

        # Set the font family and size using HTML tags
        html = f"<div style='font-family: Arial; font-size: 12pt'></div>"
        # Write the HTML to the Streamlit app
        st.write(html, unsafe_allow_html=True)


