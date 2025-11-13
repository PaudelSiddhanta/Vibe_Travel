# Quick Start: Deploy to Vertex AI (30 minutes)

Enable **real-time Google Search** in your travel agent!

## 🎯 What You Need

1. **Google Account** (gmail works)
2. **Credit Card** (for Google Cloud - but you get $300 FREE credits!)
3. **30 minutes** of your time

---

## ⚡ 5-Step Quick Setup

### Step 1: Create Google Cloud Project (5 min)

1. Go to: https://console.cloud.google.com/
2. Click **"New Project"**
3. Name it: `vibe-travel`
4. Click **"Create"**
5. **Copy your Project ID** (something like `vibe-travel-123456`)

### Step 2: Enable Billing & APIs (5 min)

1. Go to: https://console.cloud.google.com/billing
2. Link your credit card → Get $300 FREE credits! 🎉
3. Open Cloud Shell (button at top-right)
4. Run these commands:

```bash
# Set your project (replace with YOUR project ID)
gcloud config set project vibe-travel-123456

# Enable APIs (copy all at once)
gcloud services enable aiplatform.googleapis.com \
    generativelanguage.googleapis.com \
    cloudbuild.googleapis.com
```

### Step 3: Authenticate (5 min)

**If you have gcloud CLI installed locally:**

```bash
# Login
gcloud auth login

# Set default credentials
gcloud auth application-default login

# Set your project
gcloud config set project vibe-travel-123456
```

**If you don't have gcloud CLI:**

Use Cloud Shell in the browser (already authenticated!)

### Step 4: Update Your .env File (2 min)

Edit your `.env` file:

```bash
cd /Users/catalinbotezat/Documents/NYUAD/NY/Advanced_Topics_Data_Science_LLM/Project/Vibe_Travel
nano .env
```

Add these lines (replace with YOUR project ID):

```env
GOOGLE_CLOUD_PROJECT=vibe-travel-123456
GOOGLE_CLOUD_LOCATION=us-central1
AGENT_NAME=vibe-travel-agent
```

Save and exit (Ctrl+X, then Y, then Enter)

### Step 5: Deploy Your Agent (10 min)

```bash
cd /Users/catalinbotezat/Documents/NYUAD/NY/Advanced_Topics_Data_Science_LLM/Project/Vibe_Travel
source .venv/bin/activate

# Install Vertex AI SDK
pip install google-cloud-aiplatform

# Run deployment prep
cd my_agent
python deploy_agent.py
```

Follow the instructions shown by the script!

---

## 🎊 You're Done!

Your agent now has:
- ✅ Real-time Google Search
- ✅ Current flight prices
- ✅ Live hotel availability
- ✅ Latest travel information

---

## 🧪 Test It

Create a test file `test_vertex_agent.py`:

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

# Test your deployed agent
# (See deployment output for exact endpoint)
print("Agent deployed! Check Vertex AI Console:")
print("https://console.cloud.google.com/vertex-ai/agents")
```

---

## 💰 Cost Estimate

**For learning/testing:**
- **FREE** for first 1,000 requests/month
- After: ~$0.10 per 1,000 requests
- Your $300 credits last MONTHS

**Monthly estimate for moderate use:**
- ~$5-20/month
- Free tier covers most testing

---

## ❓ Common Issues

### "Permission Denied"
```bash
gcloud auth login
gcloud auth application-default login
```

### "Project not found"
Check your project ID:
```bash
gcloud config get-value project
```

### "API not enabled"
```bash
gcloud services enable aiplatform.googleapis.com
```

---

## 📚 Full Guide

For detailed instructions, see: `VERTEX_AI_DEPLOYMENT_GUIDE.md`

---

## 🆘 Need Help?

1. Check `VERTEX_AI_DEPLOYMENT_GUIDE.md`
2. Google Cloud Support: https://cloud.google.com/support
3. Vertex AI Docs: https://cloud.google.com/vertex-ai/docs

---

## 🎯 Next Steps

After deployment:
1. Test with real travel queries
2. Monitor usage in Cloud Console
3. Build a web UI (optional)
4. Share with friends! 🌍✈️

