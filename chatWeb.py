import streamlit as st
from chatFile import *

st.header('Welcome to Legendary GPT')
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    name = st.text_area(label="Your Name")

with col2:
    language = st.selectbox("Language",(
    "English",
    "Spanish",
    "French",
    "German",
    "Chinese",
    "Japanese",
    "Arabic",
    "Russian",
    "Portuguese",
    "Italian",
    "Dutch",
    "Hindi",
    "Swedish",
    "Korean",
    "Turkish",
    "Greek",
    "Hebrew",
    "Thai",
    "Vietnamese",
    "Polish",
))

key = st.text_area(label="Enter Your Key")

with col3:
    url = st.text_area(label="Enter URL.....")
    web(url)

with col4:
     file = st.file_uploader("Pick a File")

temperature = st.slider("Creativity", 0,10,5)

query = st.text_area(label="Your Query")

ans = chat_connection(query, temp = 1)

st.markdown("### Result From Legendary GPT")
st.write(ans)