import os
from google.adk.agents.llm_agent import Agent
from tavily import TavilyClient
from dotenv import load_dotenv
import google.generativeai as genai


# --- Load environment variables
load_dotenv(override=True)

tavily_key = os.getenv("TAVILY_API_KEY")
gemini_key = os.getenv("GOOGLE_API_KEY")


# --- Initialize Gemini and Tavily
genai.configure(api_key=gemini_key)
tavily_client = TavilyClient(api_key=tavily_key)

# --- Tool definitions
def internet_search(query: str) -> str:
    """Search the internet for travel information."""
    results = tavily_client.search(query, max_results=5)
    summaries = [
        f"- [{r['title']}]({r['url']}): {r['content'][:150]}..."
        for r in results.get("results", [])
    ]
    return "\n".join(summaries)

def get_trip_itinerary(city: str, interests: list[str], budget: int, days: int) -> dict:
    """Use Gemini and Tavily to plan a personalized itinerary."""
    search_query = f"{city} {', '.join(interests)} itinerary ideas, budget {budget} USD, {days} days"
    context = internet_search(search_query)

    prompt = f"""
    You are an expert travel planner.
    The user wants a {days}-day trip to {city}.
    Interests: {', '.join(interests)}.
    Budget: ${budget}.

    Use the following up-to-date search results to create a detailed itinerary:

    {context}

    Output a clear, day-by-day plan including:
    - Key attractions or experiences
    - Dining or nightlife suggestions (if relevant)
    - Approximate daily costs
    - Any travel tips or advice
    """

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return {"city": city, "itinerary": response.text.strip()}

# --- Define the main agent
agent = Agent(
    model="gemini-2.5-flash",
    name="trip_planner_agent",
    description="An AI travel planner that uses Tavily for live info and Gemini for reasoning.",
    tools=[internet_search, get_trip_itinerary],
)

# --- Interactive CLI
if __name__ == "__main__":
    print("\n🌍 Welcome to Vibe Travel Agent ✈️\n")

    city = input("🗺️ Enter destination city: ").strip()
    interests_raw = input("🎨 Enter your interests (comma-separated): ").strip()
    interests = [i.strip() for i in interests_raw.split(",") if i.strip()]
    budget = int(input("💰 Enter your budget in USD: ").strip())
    days = int(input("🗓️  How many days is your trip? ").strip())

    print("\n✨ Generating your custom itinerary... please wait ✨\n")

    result = get_trip_itinerary(city=city, interests=interests, budget=budget, days=days)

    print(f"\n🌟 Trip Itinerary for {city} 🌟\n")
    print(result["itinerary"])
    print("\n✅ Done! Enjoy your trip 🌍")
