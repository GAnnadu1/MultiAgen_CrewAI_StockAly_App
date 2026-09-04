import streamlit as st
from google import genai

st.write(bool(st.secrets.get("GEMINI_API_KEY")))

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

response = client.models.generate_content(
    model="gemini-omni-1.1-flash",
    contents="Hello"
)

print(response.text)
