from crewai import Agent, LLM

from tools.stock_research_tools import get_stock_price

#initialze LLM
llm = LLM(
    model="gemini/gemini-3.1-flash-lite",
    api_key=os.environ["GEMINI_API_KEY"],
    temperature=0
    )

analyst_agent = Agent(
    role="Financial Market Agent",
    goal = ("Perform in-depth evaluations of publicly traded stocks using real-time data,"
            "identifying trends, performance insights, and key financial ratios."),
    backstory = ("You are a veteran financial analyst with deep expertise in interpreting stock market data,"
                "technical trends, and fundamentals. You apecialize in producting well-structured reports that evaluate"
                "Stock performance using live marke indicators."),
    llm=llm,
    tools=[get_stock_price],
    verbose=True
)
