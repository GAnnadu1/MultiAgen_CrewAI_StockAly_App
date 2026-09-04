from crewai import Agent, LLM
from tools.stock_research_tools import get_stock_price

#initialize LLM
llm = LLM(
    model="gemini/gemini-3.1-flash-lite",
    temperature=0
    )

trader_agent = Agent(
    role="Strategic Stock Trader",
    goal=("Formulate investment strategies and execute trades based on comprehensive market analysis,"
          "aiming for optimal portfolio growth and risk management."),
    backstory=("You are a seasoned investment strategist with a track record of identifying profitable"
               "trading opportunities and managing risk effectively across diverse market conditions."),
    llm=llm,
    tools=[get_stock_price], # Including get_stock_price as a relevant tool for market data
    verbose=True
)
