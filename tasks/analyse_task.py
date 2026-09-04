from crewai import Task
from agents.analyst_agent import analyst_agent

get_stock_analysis = Task(
    description=(
        "Analyze the stock performance of {stock} a given company, focusing on key financial metrics,"
        "market trends, and news. Provide insights into its current valuation and future outlook."
    ),
    expected_output=(
        "A comprehensive report detailing the stock's performance, including its current price,"
        "daily change, key financial ratios, relevant news, and a recommendation (buy/sell/hold)."
    ),
    agent=analyst_agent
)
