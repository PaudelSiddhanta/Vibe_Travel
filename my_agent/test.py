from google.adk.agents.llm_agent import Agent
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def internet_search(query: str) -> str:
    results = tavily_client.search(query, max_results=3)
    return str(results)

agent = Agent(
    model='gemini-2.5-flash',
    name='trip_planner_agent',
    description="An AI travel agent.",
    tools=[internet_search]
)

print(internet_search("i want to do a holidy where I go wine tasting. I live in New York and my budget is 1500$. I want a 1 week holiday."))
