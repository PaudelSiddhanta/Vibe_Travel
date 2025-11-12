# In this file I will utilize a langchain deepagnet  to generate trip plans based on user input.
import os
from typing import Literal
from tavily import TavilyClient
from deepagents import create_deep_agent

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """Run a web search"""
    return tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )

research_instructions = " Generate a detailed trip in between {day_1} and {day_2} for a traveler interested in {interests}. Include activities, places to visit, and dining options. " \
"Find a suitable location that satisfied the user's interests. Provide a day-wise breakdown of the trip plan. Give an estimate of the budget give {budget} "
trip_prompt = PromptTemplate(instructions)



agent = create_deep_agent(
    tools=[internet_search],
    system_prompt=research_instructions
)

result = agent.invoke({"messages": [{"role": "user", "content": "What is langgraph?"}]})

# Print the agent's response
print(result["messages"][-1].content)