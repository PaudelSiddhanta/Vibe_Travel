from google.adk.agents.llm_agent import Agent
from tavily import TavilyClient
from dotenv import load_dotenv
import google.generativeai as genai
import os

# --- Load environment variables
load_dotenv(override=True)

tavily_key = os.getenv("TAVILY_API_KEY")
gemini_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=gemini_key)
tavily_client = TavilyClient(api_key=tavily_key)

# --- Tool: Internet Search
def internet_search(query: str) -> str:
    """Search the internet for travel information."""
    results = tavily_client.search(query, max_results=5)
    summaries = [
        f"- [{r['title']}]({r['url']}): {r['content'][:200]}..."
        for r in results.get("results", [])
    ]
    return "\n".join(summaries)

# --- Tool: Generate trip plan dynamically
def plan_smart_trip(home_city: str, interests: list[str], budget: int, days: int) -> dict:
    """Find an ideal destination and itinerary based on the user's situation."""
    search_query = (
        f"best destinations near {home_city} for {', '.join(interests)}, "
        f"budget {budget} USD, {days}-day trip, "
        "including travel costs, weather, and season."
    )
    context = internet_search(search_query)

    prompt = f"""
    You are an expert travel planner.
    A user currently in {home_city} wants to plan a {days}-day vacation.
    Interests: {', '.join(interests)}.
    Total budget: ${budget}.

    Use the latest travel data below to:
    1. Recommend the best possible destination(s) within the budget and timeframe. ( different from the current destination, you may find this by searching)
    2. Explain why you chose that destination.
    3. Create a detailed, day-by-day itinerary for that destination.
    4. Include approximate total cost, daily breakdown, and travel tips.

    Use this information from Tavily to support your recommendations:
    {context}

    Format your answer clearly with headings:
    - 🗺️ Destination
    - 💡 Why this destination
    - 📅 Day-by-day itinerary
    - 💰 Estimated total cost
    - 🧳 Tips & Notes
    """

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return {"home": home_city, "trip_plan": response.text.strip()}

# --- Define the main agent
agent = Agent(
    model="gemini-2.5-flash",
    name="vibe_travel_agent",
    description="An AI travel planner that chooses destinations automatically based on interests, budget, and time.",
    tools=[internet_search, plan_smart_trip],
)

# --- Interactive CLI
if __name__ == "__main__":
    print("\n🌍 Welcome to Vibe Travel Agent ✈️\n")

    home_city = input("🏠 Enter your current location: ").strip()
    interests_raw = input("🎨 Enter your interests (comma-separated): ").strip()
    interests = [i.strip() for i in interests_raw.split(",") if i.strip()]
    budget = int(input("💰 Enter your total budget (USD): ").strip())
    days = int(input("🗓️  How many days can you travel? ").strip())

    print("\n✨ Finding the perfect destination and itinerary... please wait ✨\n")

    result = plan_smart_trip(home_city=home_city, interests=interests, budget=budget, days=days)

    print(f"\n🌟 Vibe Travel Plan 🌟\n")
    print(result["trip_plan"])
    print("\n✅ Done! Your trip plan is ready 🌍")
t