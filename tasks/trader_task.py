from crewai import Task
from agents.trader_agent import trader_agent

trade_decision = Task(
    description=(
        "Analyze the current stock market data and the financial analysis report provided by the analyst agent."
        "Formulate a strategic trade decision (buy, sell, or hold) for a given stock based on its valuation,"
        "market sentiment, and potential future performance. Justify the decision with clear reasoning."
    ),
    expected_output=(
        "A concise trade recommendation (buy, sell, or hold) for the specified stock, including the target price,"
        "stop-loss, and a detailed explanation of the rationale behind the decision, considering both fundamental"
        "and technical indicators."
    ),
    agent=trader_agent
)
