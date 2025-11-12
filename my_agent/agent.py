import os
from google.adk.agents.llm_agent import Agent
from tavily import TavilyClient

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def internet_search(query: str) -> str:
    """Search the internet for travel information, attractions, hotels, and activities."""
    results = tavily_client.search(query, max_results=5)
    return str(results)

def get_trip_itinerary(city: str, interests: list[str], budget: int, start_date: str, end_date: str) -> dict:
    """Generate a detailed trip itinerary based on user preferences."""
    # This function will be enhanced by the agent using internet_search
    return {
        "city": city,
        "interests": interests,
        "budget": budget,
        "dates": f"{start_date} to {end_date}",
        "status": "Agent will generate itinerary"
    }

root_agent = Agent(
    model='gemini-2.5-flash',
    name='trip_planner_agent',
    description="An AI travel agent that creates personalized trip itineraries based on budget, destination, interests, and dates.",
    instruction="""You are an expert travel planner. When a user asks about trip planning:
    1. Use the internet_search tool to find current information about attractions, restaurants, hotels, and activities
    2. Create a detailed day-by-day itinerary
    3. Consider the user's budget and interests
    4. Include specific recommendations with estimated costs
    5. Provide practical travel tips
    
    Always search for up-to-date information about the destination before making recommendations.""",
    tools=[internet_search, get_trip_itinerary],
)