import streamlit as st
from google import genai

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

response = client.models.generate_content(
    model="gemini/gemini-3.1-flash-lite",
    contents="Hello"
)

print(response.text)
