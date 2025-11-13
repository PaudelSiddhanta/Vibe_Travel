#!/usr/bin/env python3
"""
Interactive Travel Planner
Collects user inputs (location, interests, budget, days) and generates a trip itinerary
This script works locally by calling the agent's sub-agents and tools directly
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def collect_user_inputs():
    """Collect travel planning inputs from the user."""
    print("\n" + "="*60)
    print("🌍 Vibe Travel Planner - Interactive Mode")
    print("="*60)
    print("\nPlease provide the following information to plan your trip:\n")
    
    # Collect starting location
    starting_location = input("🏠 Enter your starting location (city, country): ").strip()
    if not starting_location:
        print("❌ Starting location is required!")
        return None
    
    # Collect interests
    interests_raw = input("🎨 Enter your interests (comma-separated, e.g., beaches, museums, hiking): ").strip()
    if not interests_raw:
        print("⚠️  No interests provided. Using default: travel")
        interests = ["travel"]
    else:
        interests = [i.strip() for i in interests_raw.split(",") if i.strip()]
    
    # Collect budget
    while True:
        try:
            budget_str = input("💰 Enter your total budget (USD): ").strip()
            budget = int(budget_str)
            if budget <= 0:
                print("❌ Budget must be greater than 0!")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number for budget!")
    
    # Collect trip duration
    while True:
        try:
            days_str = input("🗓️  How many days is your trip? ").strip()
            days = int(days_str)
            if days <= 0:
                print("❌ Trip duration must be greater than 0!")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number for days!")
    
    return {
        "starting_location": starting_location,
        "interests": interests,
        "budget": budget,
        "days": days
    }

def generate_travel_plan_with_agent(user_inputs):
    """Generate travel plan using the agent's model with Google Search grounding."""
    try:
        from agent2 import root_agent
        import google.generativeai as genai
        
        print("\n" + "="*60)
        print("🚀 Generating Your Travel Plan...")
        print("="*60)
        print("\n⏳ Please wait while the agent plans your trip...\n")
        
        starting_location = user_inputs["starting_location"]
        interests = user_inputs["interests"]
        budget = user_inputs["budget"]
        days = user_inputs["days"]
        
        print(f"📤 Planning trip:")
        print(f"   Starting Location: {starting_location}")
        print(f"   Interests: {', '.join(interests)}")
        print(f"   Budget: ${budget} USD")
        print(f"   Duration: {days} days\n")
        
        # Use the agent's model (gemini-2.5-flash is fast and widely available)
        # Other good options: gemini-2.5-pro (more powerful), gemini-flash-latest, gemini-pro-latest
        MODEL_ID = os.getenv("MODEL_ID", "gemini-2.5-flash")
        
        # Configure the model (try both GEMINI_API_KEY and GOOGLE_API_KEY for compatibility)
        GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not GOOGLE_API_KEY:
            print("❌ ERROR: GEMINI_API_KEY or GOOGLE_API_KEY is not set!")
            print("   Please set GEMINI_API_KEY in your .env file")
            return False
        
        genai.configure(api_key=GOOGLE_API_KEY)
        
        # Create model (Google Search grounding only works in Vertex AI/Google Cloud)
        print("🔍 Configuring AI model...")
        model = genai.GenerativeModel(MODEL_ID)
        print("ℹ️  Using standard model (without real-time search)")
        print("   Note: For real-time search, the agent needs to be deployed to Google Cloud Vertex AI")
        
        # Create a comprehensive prompt
        prompt = f"""You are a friendly and helpful travel agent. A user wants to plan a trip with the following details:

- Starting Location: {starting_location}
- Interests: {', '.join(interests)}
- Budget: ${budget} USD
- Trip Duration: {days} days

Based on your knowledge of travel destinations, typical costs, and popular activities, create a comprehensive travel plan by:

1. **Recommended Destination**: Based on the starting location ({starting_location}) and interests ({', '.join(interests)}), recommend a specific destination that fits the budget of ${budget} and can be enjoyed over {days} days. Explain why you chose this destination.

2. **Flight Recommendations**: Search for and provide flight options from {starting_location} to the recommended destination. Include:
   - Estimated prices
   - Airlines
   - Travel times
   - Booking tips

3. **Hotel Recommendations**: Find suitable hotels in the destination that fit the budget. Include:
   - Hotel names and ratings
   - Amenities
   - Estimated prices per night
   - Location advantages

4. **Detailed Day-by-Day Itinerary**: Create a detailed itinerary for {days} days that incorporates the user's interests ({', '.join(interests)}). For each day, include:
   - Morning activities
   - Afternoon activities
   - Evening activities
   - Recommended times
   - Travel tips and notes
   - Estimated costs per day

5. **Food Recommendations**: Suggest restaurants, cafes, or food options that align with the itinerary and interests. Include:
   - Restaurant names
   - Cuisine types
   - Price ranges
   - Locations relative to itinerary activities

6. **Financial Planning**: Break down the budget:
   - Flights cost (estimated)
   - Hotels cost (estimated for {days} days)
   - Activities/itinerary cost (estimated)
   - Food cost (estimated)
   - Total estimated cost vs budget (${budget})
   - Remaining budget or over-budget amount

Format your response clearly with markdown:
- Use **bold** for section headings
- Use bullet points for lists
- Use clear structure with sections separated by blank lines
- Include specific details and actionable recommendations

Make the travel plan comprehensive, realistic, and aligned with the user's interests and budget."""

        print("🤖 Generating comprehensive travel plan...")
        print("   (This may take 30-60 seconds...)\n")
        
        # Generate the travel plan
        response = model.generate_content(prompt)
        
        if response and response.text:
            print("\n" + "="*60)
            print("🌟 Your Travel Plan")
            print("="*60)
            print()
            print(response.text)
            print()
            print("="*60)
            print("✅ Travel plan generated successfully!")
            print("\n💡 Important Notes:")
            print("   - This plan is based on the AI model's training data (not real-time search)")
            print("   - Prices and availability should be verified on booking websites")
            print("   - For real-time data: Deploy agent2.py to Google Cloud Vertex AI")
            print("   - The deployed agent can use Google Search and all sub-agents")
            return True
        else:
            print("⚠️  No response from the model")
            return False
            
    except ImportError as e:
        print(f"❌ Error importing modules: {e}")
        print("   Make sure all required packages are installed:")
        print("   - google-generativeai")
        print("   - google-adk")
        return False
    except Exception as e:
        print(f"❌ Error generating travel plan: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_agent_setup():
    """Test that the agent is set up correctly."""
    try:
        from agent2 import root_agent
        
        print("\n" + "="*60)
        print("🧪 Testing Agent Setup")
        print("="*60)
        
        print(f"\n✅ Agent Configuration:")
        print(f"   Agent Name: {root_agent.name}")
        print(f"   Model: {root_agent.model}")
        print(f"   Number of Tools: {len(root_agent.tools)}")
        print(f"   Tools: {[tool.name if hasattr(tool, 'name') else str(tool)[:50] for tool in root_agent.tools[:5]]}")
        
        print(f"\n✅ Agent is configured correctly!")
        print(f"\n💡 Note: For full agent functionality with tool calling,")
        print(f"   deploy the agent to Google Cloud AI Platform.")
        print(f"   This script uses direct model calls for local testing.")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing agent setup: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main function."""
    print("="*60)
    print("🌍 Vibe Travel Planner")
    print("="*60)
    
    # Check if MODEL_ID is set (with a sensible default)
    MODEL_ID = os.getenv("MODEL_ID", "gemini-2.5-flash")
    print(f"\nℹ️  Using model: {MODEL_ID}")
    print("   (Set MODEL_ID in .env to use a different model)")
    print("   Good options: gemini-2.5-flash, gemini-2.5-pro, gemini-flash-latest")
    
    # Check if GEMINI_API_KEY or GOOGLE_API_KEY is set
    GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not GOOGLE_API_KEY:
        print("\n❌ ERROR: GEMINI_API_KEY or GOOGLE_API_KEY environment variable is not set!")
        print("   Please set GEMINI_API_KEY in your .env file or environment variables.")
        print("   Example: GEMINI_API_KEY=your_api_key_here")
        sys.exit(1)
    
    # Ask user for mode
    print("\nChoose a mode:")
    print("1. Generate Travel Plan (collect inputs and generate itinerary)")
    print("2. Test Agent Setup (verify agent configuration)")
    print("3. Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1/2/3): ").strip()
            
            if choice == "1":
                # Generate travel plan
                user_inputs = collect_user_inputs()
                if user_inputs:
                    success = generate_travel_plan_with_agent(user_inputs)
                    if success:
                        print("\n💡 Next steps:")
                        print("   - Review the travel plan above")
                        print("   - For full agent functionality with tool calling,")
                        print("     deploy the agent to Google Cloud AI Platform")
                        print("   - The deployed agent can use all tools (flight search, hotel search, etc.)")
                    else:
                        print("\n❌ Failed to generate travel plan")
                break
            elif choice == "2":
                # Test agent setup
                test_agent_setup()
                break
            elif choice == "3":
                print("\n👋 Goodbye!")
                sys.exit(0)
            else:
                print("❌ Invalid choice. Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Error: {e}")
            import traceback
            traceback.print_exc()
            break

if __name__ == "__main__":
    main()
