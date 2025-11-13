# Google Search & Grounding - Explained

## ❌ The Error You Got

```
400 google_search_retrieval is not supported. Please use google_search tool instead.
```

## 🔍 Why This Happened

There are **TWO different ways** to use Google Search with Gemini, and they work in different environments:

### 1. `google_search_retrieval` (Grounding) ❌ NOT Available with API Key

- **What it is**: Google Search Grounding feature
- **Where it works**: Only in **Vertex AI** (Google Cloud Platform)
- **Requires**: Google Cloud project, Vertex AI setup
- **Access method**: Through Vertex AI API
- **Error**: "google_search_retrieval is not supported" when using consumer API key

```python
# ❌ This ONLY works in Vertex AI, NOT with consumer API key
model = genai.GenerativeModel(
    "gemini-2.5-flash",
    tools='google_search_retrieval'  # ❌ Fails with API key
)
```

### 2. `google_search` (ADK Tool) ✅ Works with Agents

- **What it is**: Google ADK tool for agents
- **Where it works**: In deployed agents on Google Cloud
- **Requires**: Agent deployment to Vertex AI
- **Access method**: Through Google ADK agents
- **Usage**: Automatically called by agents

```python
# ✅ This works when agent is deployed to Vertex AI
from google.adk.tools import google_search

root_agent = LlmAgent(
    name="travel_planner",
    model="gemini-2.5-flash",
    tools=[google_search]  # ✅ Works when deployed
)
```

## 📊 Comparison Table

| Feature | API Key (Consumer) | Vertex AI (Cloud) |
|---------|-------------------|-------------------|
| Basic model | ✅ Works | ✅ Works |
| `google_search_retrieval` | ❌ Not supported | ✅ Works |
| `google_search` tool | ❌ Needs deployment | ✅ Works |
| Real-time search | ❌ No | ✅ Yes |
| Cost | Free tier available | Pay-as-you-go |
| Setup complexity | Easy (just API key) | Complex (Cloud setup) |

## 🛠️ Current Setup

### What You're Using Now:

```python
# Your current setup (interactive_travel_planner.py)
genai.configure(api_key=GEMINI_API_KEY)  # Consumer API key
model = genai.GenerativeModel("gemini-2.5-flash")  # Standard model
```

✅ **Works**: Basic model with its training data
❌ **Doesn't have**: Real-time Google Search

### What This Means:

- ✅ Can generate travel plans based on training data
- ✅ Knows about popular destinations, typical costs, activities
- ❌ No real-time flight prices
- ❌ No real-time hotel availability
- ❌ No current weather or events

## 🚀 How to Get Real-Time Search

### Option 1: Deploy Agent to Vertex AI (Recommended for Production)

This is what `agent2.py` is designed for:

```bash
# 1. Set up Google Cloud project
# 2. Enable Vertex AI API
# 3. Deploy agent2.py to Vertex AI
# 4. Agent can then use google_search tool
```

**Benefits:**
- ✅ Real-time Google Search
- ✅ All sub-agents work (location finder, flight recommender, etc.)
- ✅ Google Sheets/Docs export tools
- ✅ Production-ready

**Requirements:**
- Google Cloud account
- Vertex AI enabled
- Deployment setup

### Option 2: Use Third-Party Search APIs (Alternative)

You could integrate other search APIs:

```python
# Example with Tavily (you already have the key in .env)
from tavily import TavilyClient

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
results = client.search("best beach destinations from New York")
```

**Benefits:**
- ✅ Works with API key (no Cloud setup)
- ✅ Real-time search
- ⚠️ Different API than Google Search

## 💡 Recommendations

### For Testing/Development (Current):
- ✅ Use `interactive_travel_planner.py` with standard model
- ✅ Good for basic travel planning
- ✅ No additional setup needed
- ⚠️ Verify prices/availability manually

### For Production:
- 🚀 Deploy `agent2.py` to Vertex AI
- ✅ Get real-time search capabilities
- ✅ Use all agent features
- ✅ Professional grade solution

## 📝 Quick Summary

**Your Error**: You tried to use `google_search_retrieval` (Vertex AI feature) with a consumer API key.

**The Fix**: Removed `google_search_retrieval` to use the standard model.

**Current Status**: ✅ Working - generates travel plans from training data

**For Real-Time Data**: Deploy `agent2.py` to Vertex AI (see `agent2.py` file for deployment instructions)

## 🔗 Useful Links

- [Google AI Studio](https://makersuite.google.com/) - Get API keys
- [Vertex AI Console](https://console.cloud.google.com/vertex-ai) - Deploy agents
- [Google ADK Docs](https://cloud.google.com/vertex-ai/docs/generative-ai/adk/overview) - Agent development
- [Gemini API Docs](https://ai.google.dev/docs) - Consumer API reference

