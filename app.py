import streamlit as st
from crew import stock_crew

st.set_page_config(page_title="AI Stock Analyst")

st.title("📊 CrewAI Stock Analyst")

symbol = st.text_input("Stock Symbol")

if st.button("Analyze"):
    if symbol:
        with st.spinner("Working..."):
            result = stock_crew.kickoff(
                inputs={"stock": symbol.upper()}
            )

        st.markdown(result)
