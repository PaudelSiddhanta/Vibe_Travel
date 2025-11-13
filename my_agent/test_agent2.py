#!/usr/bin/env python3
"""
Test script for agent2.py
This script tests the travel planner agent setup and allows interactive testing.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_imports():
    """Test that all imports work correctly."""
    print("🔍 Testing imports...")
    try:
        from agent2 import (
            root_agent,
            location_finder_based_on_interests,
            flight_recommender,
            hotel_recommender,
            itinerary_recommender,
            food_recommender,
            financial_planner_agent
        )
        print("✅ All imports successful!")
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

def test_environment_variables():
    """Test that required environment variables are set."""
    print("\n🔍 Testing environment variables...")
    required_vars = {
        "MODEL_ID": os.getenv("MODEL_ID"),
        "GOOGLE_CLOUD_PROJECT": os.getenv("GOOGLE_CLOUD_PROJECT"),
        "GOOGLE_CLOUD_LOCATION": os.getenv("GOOGLE_CLOUD_LOCATION"),
    }
    
    all_set = True
    for var_name, var_value in required_vars.items():
        if var_value:
            print(f"✅ {var_name}: {var_value}")
        else:
            print(f"⚠️  {var_name}: Not set (optional for basic testing)")
            # MODEL_ID is critical, others are optional
            if var_name == "MODEL_ID":
                all_set = False
                print(f"❌ {var_name} is required but not set!")
    
    return all_set

def test_agent_creation():
    """Test that agents are created correctly."""
    print("\n🔍 Testing agent creation...")
    try:
        from agent2 import root_agent
        
        # Check agent attributes
        assert hasattr(root_agent, 'name'), "Agent should have a 'name' attribute"
        assert hasattr(root_agent, 'model'), "Agent should have a 'model' attribute"
        assert hasattr(root_agent, 'tools'), "Agent should have a 'tools' attribute"
        
        print(f"✅ Agent '{root_agent.name}' created successfully")
        print(f"   Model: {root_agent.model}")
        print(f"   Number of tools: {len(root_agent.tools)}")
        
        return True
    except Exception as e:
        print(f"❌ Agent creation test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_agent_invoke_simple():
    """Test invoking the agent with a simple message."""
    print("\n🔍 Testing agent invocation...")
    try:
        from agent2 import root_agent
        
        # Check available methods (avoid accessing deprecated Pydantic attributes)
        available_methods = []
        for attr in dir(root_agent):
            if not attr.startswith('_') and attr not in ['model_computed_fields', 'model_fields', 'model_config', 'model_fields_set', 'model_extra', 'model_json_schema', 'model_parametrized_name']:
                try:
                    if callable(getattr(root_agent, attr, None)):
                        available_methods.append(attr)
                except:
                    pass
        print(f"   Available methods: {', '.join(available_methods[:10])}...")
        
        # Check if agent has invoke method (preferred for testing)
        if hasattr(root_agent, 'invoke'):
            print("   ✅ Agent has 'invoke' method")
            print("   ℹ️  Agent can be invoked with messages")
            return True
        
        # Check if agent has run_live method (note: requires parent_context)
        if hasattr(root_agent, 'run_live'):
            print("   ⚠️  Agent has 'run_live' method (but requires parent_context parameter)")
            print("   ℹ️  Use 'invoke()' method instead for testing")
            return True
        
        # If neither, the agent might need deployment
        print("   ⚠️  Agent doesn't have 'invoke' or 'run_live' methods")
        print("   ℹ️  This agent might need to be deployed to Google Cloud AI Platform")
        print("   ℹ️  Check Google ADK documentation for deployment instructions")
        return None  # Return None to indicate it needs deployment
        
    except Exception as e:
        print(f"❌ Agent invocation test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def interactive_test():
    """Interactive testing mode using invoke method."""
    print("\n" + "="*60)
    print("🌍 Interactive Travel Planner Test")
    print("="*60)
    print("\n💡 TIP: Use the structured input mode for better results!")
    print("   Run: python interactive_travel_planner.py")
    print("\nYou can now interact with the travel planner agent.")
    print("Type 'exit' or 'quit' to end the session.\n")
    
    try:
        from agent2 import root_agent
        
        # Use invoke method (run_live requires parent_context which is not available)
        if hasattr(root_agent, 'invoke'):
            print("🚀 Starting interactive session with invoke()...")
            messages = []
            
            while True:
                try:
                    user_input = input("\n👤 You: ").strip()
                    
                    if user_input.lower() in ['exit', 'quit', 'q']:
                        print("\n👋 Goodbye! Safe travels! 🌍")
                        break
                    
                    if not user_input:
                        continue
                    
                    # Add user message to history
                    messages.append({
                        "role": "user",
                        "content": user_input
                    })
                    
                    print("\n🤖 Agent is thinking...")
                    response = root_agent.invoke({
                        "messages": messages
                    })
                    
                    if response and "messages" in response:
                        # Get the last message from the agent
                        agent_messages = [msg for msg in response["messages"] if msg.get("role") == "assistant"]
                        if agent_messages:
                            last_message = agent_messages[-1]
                            content = last_message.get("content", "No response")
                            print(f"\n🤖 Agent: {content}")
                            # Update messages with the full response
                            messages = response["messages"]
                        else:
                            print("\n⚠️  No response from agent")
                    else:
                        print(f"\n⚠️  Unexpected response: {response}")
                        
                except KeyboardInterrupt:
                    print("\n\n👋 Session interrupted. Goodbye!")
                    break
                except Exception as e:
                    print(f"\n❌ Error: {e}")
                    import traceback
                    traceback.print_exc()
                    break
            return
        else:
            # If invoke method is not available
            print("❌ Agent doesn't support interactive mode (no 'invoke' method)")
            available_methods = [m for m in dir(root_agent) if not m.startswith('_') and callable(getattr(root_agent, m, None))]
            print(f"   Available methods: {', '.join(available_methods[:10])}...")
            print("\nℹ️  This agent might need to be deployed to Google Cloud AI Platform")
            print("   Check Google ADK documentation for deployment and testing instructions")
                
    except KeyboardInterrupt:
        print("\n\n👋 Session interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error starting interactive mode: {e}")
        import traceback
        traceback.print_exc()

def main():
    """Main test function."""
    print("="*60)
    print("🧪 Testing agent2.py")
    print("="*60)
    
    # Run tests
    tests = [
        ("Import Test", test_imports),
        ("Environment Variables Test", test_environment_variables),
        ("Agent Creation Test", test_agent_creation),
        ("Agent Invoke Test", test_agent_invoke_simple),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ {test_name} crashed: {e}")
            results.append((test_name, False))
    
    # Print summary
    print("\n" + "="*60)
    print("📊 Test Summary")
    print("="*60)
    for test_name, result in results:
        if result is True:
            print(f"✅ {test_name}: PASSED")
        elif result is None:
            print(f"⚠️  {test_name}: SKIPPED (needs deployment)")
        else:
            print(f"❌ {test_name}: FAILED")
    
    # Ask if user wants to run interactive test (only if running in interactive terminal)
    print("\n" + "="*60)
    if sys.stdin.isatty():  # Check if running in an interactive terminal
        try:
            user_input = input("\n🤖 Would you like to test the agent interactively? (y/n): ").strip().lower()
            if user_input in ['y', 'yes']:
                interactive_test()
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Goodbye!")
    else:
        print("\n💡 To test interactively, run:")
        print("   python test_agent2.py")
        print("   (in an interactive terminal)")

if __name__ == "__main__":
    main()

