import streamlit as st
from scrape import scrape_website

st.title("AI Web Scraper")

url = st.text_input("Enter URL:")

if st.button("Scrape"):
    if not url.strip():
        st.error("Please enter a valid URL.")
    else:
        st.write("Scraping...")
        result = scrape_website(url)
        if "Error occurred" in result:
            st.error(result)
        else:
            st.code(result, language="html")
