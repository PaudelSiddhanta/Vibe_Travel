# 🚀 Vertex AI Deployment Checklist

Use this checklist to deploy your agent with **real-time Google Search** capabilities.

---

## ✅ Phase 1: Google Cloud Setup (15 min)

### Account & Project
- [ ] Create Google account (if you don't have one)
- [ ] Go to [Google Cloud Console](https://console.cloud.google.com/)
- [ ] Create new project named `vibe-travel`
- [ ] **Copy your Project ID** (e.g., `vibe-travel-123456`)
- [ ] Enable billing → Get $300 FREE credits for new users

### Enable APIs
- [ ] Open Cloud Shell or local terminal
- [ ] Run: `gcloud config set project YOUR_PROJECT_ID`
- [ ] Enable APIs:
```bash
gcloud services enable aiplatform.googleapis.com \
    generativelanguage.googleapis.com \
    cloudbuild.googleapis.com \
    artifactregistry.googleapis.com
```

---

## ✅ Phase 2: Local Setup (10 min)

### Install gcloud CLI (if not installed)
- [ ] **macOS**: `brew install google-cloud-sdk`
- [ ] **Linux**: Follow [installation guide](https://cloud.google.com/sdk/docs/install)
- [ ] **Windows**: Download from [here](https://cloud.google.com/sdk/docs/install)

### Authenticate
```bash
# Login to Google Cloud
gcloud auth login

# Set application default credentials
gcloud auth application-default login

# Set your project
gcloud config set project YOUR_PROJECT_ID

# Verify
gcloud config list
```

- [ ] Run authentication commands above
- [ ] Verify project is set correctly

### Update .env File
- [ ] Open `.env` file in Vibe_Travel directory
- [ ] Add/update these lines:
```env
GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID
GOOGLE_CLOUD_LOCATION=us-central1
AGENT_NAME=vibe-travel-agent
```
- [ ] Save the file

### Install Dependencies
```bash
cd /Users/catalinbotezat/Documents/NYUAD/NY/Advanced_Topics_Data_Science_LLM/Project/Vibe_Travel
source .venv/bin/activate
pip install google-cloud-aiplatform google-cloud-storage
pip install --upgrade google-adk
```

- [ ] Activate virtual environment
- [ ] Install required packages

---

## ✅ Phase 3: Verify Setup (5 min)

### Run Pre-deployment Check
```bash
cd my_agent
python deploy_agent.py
```

- [ ] All prerequisites pass ✅
- [ ] No errors shown
- [ ] Agent configuration displays correctly

### Verify agent2.py Configuration
Your agent already has:
- [x] ✅ `google_search` tool configured in sub-agents
- [x] ✅ All 6 sub-agents (location, flight, hotel, itinerary, food, financial)
- [x] ✅ Google Sheets/Docs export tools
- [x] ✅ Proper environment variable loading

---

## ✅ Phase 4: Deploy to Vertex AI (10 min)

### Option A: Using Vertex AI Console (Recommended)

1. **Go to Vertex AI Console**
   - [ ] Visit: https://console.cloud.google.com/vertex-ai
   - [ ] Select your project

2. **Navigate to Agent Builder**
   - [ ] Click "Agent Builder" or "Generative AI"
   - [ ] Click "Create Agent" or "Deploy Agent"

3. **Upload Your Agent**
   - [ ] Upload `agent2.py` file
   - [ ] Or copy/paste the code
   - [ ] Set agent name: `vibe-travel-agent`

4. **Configure Settings**
   - [ ] Model: `gemini-2.5-flash` or `gemini-2.5-pro`
   - [ ] Location: `us-central1`
   - [ ] Enable Google Search ✅

5. **Deploy**
   - [ ] Click "Deploy"
   - [ ] Wait 2-5 minutes
   - [ ] Copy the agent endpoint URL

### Option B: Using gcloud CLI

```bash
cd my_agent

# Deploy the agent
gcloud ai agents deploy \
    --agent-file=agent2.py \
    --display-name=vibe-travel-agent \
    --project=YOUR_PROJECT_ID \
    --location=us-central1
```

- [ ] Run deployment command
- [ ] Wait for deployment to complete
- [ ] Note the agent endpoint

### Option C: Programmatic Deployment

Check the latest Google ADK docs for programmatic deployment:
- [ ] Visit: https://cloud.google.com/vertex-ai/docs/generative-ai/adk/deploy
- [ ] Follow the deployment API instructions
- [ ] Use the code examples provided

---

## ✅ Phase 5: Test Deployed Agent (10 min)

### Test from Vertex AI Console
1. **Go to your deployed agent**
   - [ ] Visit: https://console.cloud.google.com/vertex-ai/agents
   - [ ] Click on `vibe-travel-agent`

2. **Test in Console**
   - [ ] Use the built-in chat interface
   - [ ] Try a test query:
     ```
     Find me a 5-day beach vacation from New York with $3000 budget
     ```
   - [ ] Verify Google Search is being used (should see real-time data)

### Test with Python

Create `test_deployed.py`:

```python
from google.cloud import aiplatform
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize
aiplatform.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION")
)

# Test query
print("Testing deployed agent...")
print("Check Vertex AI Console for your agent:")
print("https://console.cloud.google.com/vertex-ai/agents")
```

- [ ] Create test script
- [ ] Run test
- [ ] Verify agent responds

---

## ✅ Phase 6: Verify Features (5 min)

Test each feature:

- [ ] **Google Search**: Agent uses real-time web search
- [ ] **Location Finder**: Finds destinations based on interests
- [ ] **Flight Recommender**: Gets current flight options
- [ ] **Hotel Recommender**: Finds available hotels
- [ ] **Itinerary Planner**: Creates day-by-day plans
- [ ] **Food Recommender**: Suggests restaurants
- [ ] **Financial Planner**: Calculates budget breakdown
- [ ] **Google Docs Export**: Creates shareable trip document
- [ ] **Google Sheets Export**: Creates budget spreadsheet

---

## ✅ Phase 7: Monitor & Optimize

### Set Up Monitoring
- [ ] Go to: https://console.cloud.google.com/vertex-ai/monitoring
- [ ] Enable logging
- [ ] Set up alerts for errors
- [ ] Monitor usage and costs

### Cost Management
- [ ] Check billing dashboard daily
- [ ] Set budget alerts
- [ ] Monitor free tier usage
- [ ] Optimize based on usage patterns

### Performance
- [ ] Test response times
- [ ] Check accuracy of results
- [ ] Gather user feedback
- [ ] Iterate on agent instructions if needed

---

## 📊 Success Criteria

You're done when:
- ✅ Agent is deployed to Vertex AI
- ✅ Google Search returns real-time results
- ✅ All sub-agents work correctly
- ✅ Export to Google Docs/Sheets works
- ✅ Test queries complete successfully
- ✅ Monitoring is set up
- ✅ Costs are within budget

---

## 🎯 Quick Command Reference

```bash
# Check project
gcloud config get-value project

# Check APIs
gcloud services list --enabled

# View deployed agents
gcloud ai agents list --location=us-central1

# View logs
gcloud logging read "resource.type=vertex_ai_agent" --limit=50

# Check billing
gcloud billing accounts list
```

---

## 💰 Cost Tracking

| Service | Free Tier | After Free Tier |
|---------|-----------|-----------------|
| Vertex AI Agent | 1,000 requests/month | $0.10/1K requests |
| Google Search | Included | Included |
| Storage | 5 GB | $0.026/GB/month |
| Total Estimate | FREE | $5-20/month |

**Your $300 credit**: Lasts 3-6 months with moderate use!

---

## 📚 Documentation Links

- [Vertex AI Console](https://console.cloud.google.com/vertex-ai)
- [ADK Documentation](https://cloud.google.com/vertex-ai/docs/generative-ai/adk)
- [Deployment Guide](./VERTEX_AI_DEPLOYMENT_GUIDE.md)
- [Quick Start](./QUICK_START_VERTEX_AI.md)
- [Pricing](https://cloud.google.com/vertex-ai/pricing)

---

## 🆘 Troubleshooting

### Common Issues

**"Permission Denied"**
```bash
gcloud auth login
gcloud auth application-default login
```

**"API not enabled"**
```bash
gcloud services enable aiplatform.googleapis.com
```

**"Project not found"**
```bash
gcloud config set project YOUR_PROJECT_ID
```

**"Billing not enabled"**
- Go to: https://console.cloud.google.com/billing
- Link billing account

---

## 🎉 Next Steps After Deployment

1. **Test thoroughly** with various travel queries
2. **Build a web UI** (optional) using Flask/FastAPI
3. **Share with friends** and get feedback
4. **Monitor costs** and optimize
5. **Add more features** as needed

---

## ✨ You're Ready!

Follow this checklist step by step, and you'll have a fully functional travel agent with **real-time Google Search** in about 1 hour!

Good luck! 🚀🌍✈️

