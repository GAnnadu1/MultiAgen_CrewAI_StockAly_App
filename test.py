from google import genai
import streamlit as st

st.write(bool(st.secrets.get("GEMINI_API_KEY")))

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Hello"
)

print(response.text)
