import os

from crewai import Agent
from crewai.llm import LLM
from dotenv import load_dotenv

from src.tools import (
    get_company_info,
    get_current_stock_price,
    get_income_statements,
    search_tool,
)
from src.utils import Today

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = LLM(model="gpt-4.1-2025-04-14", temperature=0.7)

# Agent for gathering company news and information
news_info_explorer = Agent(
    role="News and Info Researcher",
    goal="Gather and provide the latest news and information about a company from the internet",
    llm=llm,
    verbose=True,
    backstory=(
        "You are an expert researcher, who can gather detailed information about a company. "
        "Consider you are on: " + Today
    ),
    tools=[search_tool],
    cache=True,
    max_iter=5,
)

# Agent for gathering financial data
data_explorer = Agent(
    role="Data Researcher",
    goal="Gather and provide financial data and company information about a stock",
    llm=llm,
    verbose=True,
    backstory=(
        "You are an expert researcher, who can gather detailed information about a company or stock. "
        'When using tools, use the stock symbol and add a suffix ".NS" to it. try with and without the suffix and see what works'
        "Consider you are on: " + Today
    ),
    tools=[get_company_info, get_income_statements],
    cache=True,
    max_iter=5,
)

# Agent for analyzing data
analyst = Agent(
    role="Data Analyst",
    goal="Consolidate financial data, stock information, and provide a summary",
    llm=llm,
    verbose=True,
    backstory=(
        "You are an expert in analyzing financial data, stock/company-related current information, and "
        "making a comprehensive analysis. Use Indian units for numbers (lakh, crore). "
        "Consider you are on: " + Today
    ),
)

# Agent for financial recommendations
fin_expert = Agent(
    role="Financial Expert",
    goal="Considering financial analysis of a stock, make investment recommendations",
    llm=llm,
    verbose=True,
    tools=[get_current_stock_price],
    max_iter=5,
    backstory=(
        "You are an expert financial advisor who can provide investment recommendations. "
        "Consider the financial analysis, current information about the company, current stock price, "
        "and make recommendations about whether to buy/hold/sell a stock along with reasons."
        'When using tools, try with and without the suffix ".NS" to the stock symbol and see what works. '
        "Consider you are on: " + Today
    ),
)
