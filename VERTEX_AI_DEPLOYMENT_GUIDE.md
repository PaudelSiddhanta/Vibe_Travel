# Vertex AI Deployment Guide - Enable Google Search

This guide will help you deploy your agent to Google Cloud Vertex AI to enable **real-time Google Search** capabilities.

## 📋 Prerequisites

- Google account
- Credit card (for Google Cloud - free tier available, ~$300 free credits for new users)
- Terminal/Command line access
- Python 3.10+

## 🎯 What You'll Get

✅ Real-time Google Search in your agent
✅ All sub-agents working (location finder, flight recommender, etc.)
✅ Google Sheets/Docs export functionality
✅ Production-ready deployment
✅ Scalable infrastructure

---

## Step 1: Google Cloud Setup (15 minutes)

### 1.1 Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click **"Select a Project"** → **"New Project"**
3. Enter project details:
   - **Project Name**: `vibe-travel` (or your choice)
   - **Project ID**: Will be auto-generated (note this down!)
   - Click **"Create"**

### 1.2 Enable Billing

1. Go to [Billing](https://console.cloud.google.com/billing)
2. Link a billing account (you'll get $300 free credits if new user)
3. Enable billing for your project

**Note**: Vertex AI has a free tier, but requires billing enabled.

### 1.3 Enable Required APIs

Open Cloud Shell (button at top right) or use terminal with gcloud CLI:

```bash
# Set your project
gcloud config set project YOUR_PROJECT_ID

# Enable required APIs
gcloud services enable \
    aiplatform.googleapis.com \
    generativelanguage.googleapis.com \
    cloudbuild.googleapis.com \
    artifactregistry.googleapis.com \
    run.googleapis.com
```

Or enable manually in Console:
1. Go to [APIs & Services](https://console.cloud.google.com/apis/library)
2. Search and enable:
   - **Vertex AI API**
   - **Cloud Build API**
   - **Artifact Registry API**
   - **Cloud Run API**

---

## Step 2: Authentication Setup (10 minutes)

### 2.1 Install Google Cloud SDK (if not installed)

**macOS:**
```bash
brew install google-cloud-sdk
```

**Linux:**
```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
```

**Windows:**
Download from [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)

### 2.2 Authenticate

```bash
# Login to Google Cloud
gcloud auth login

# Set application default credentials
gcloud auth application-default login

# Set your project
gcloud config set project YOUR_PROJECT_ID

# Set default region
gcloud config set compute/region us-central1
```

### 2.3 Create Service Account (for Sheets/Docs tools)

```bash
# Create service account
gcloud iam service-accounts create vibe-travel-agent \
    --display-name="Vibe Travel Agent"

# Get the service account email
gcloud iam service-accounts list

# Grant necessary roles
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
    --member="serviceAccount:vibe-travel-agent@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/aiplatform.user"

# Create and download key
gcloud iam service-accounts keys create ~/vibe-travel-key.json \
    --iam-account=vibe-travel-agent@YOUR_PROJECT_ID.iam.gserviceaccount.com

# Store the key path
export GOOGLE_APPLICATION_CREDENTIALS=~/vibe-travel-key.json
```

---

## Step 3: Update Your Environment (5 minutes)

### 3.1 Update .env file

```bash
cd /Users/catalinbotezat/Documents/NYUAD/NY/Advanced_Topics_Data_Science_LLM/Project/Vibe_Travel
```

Update your `.env` file with:

```env
# Existing
GEMINI_API_KEY=AIzaSyA_k6pOYRRM4p31pJ4JNPSIDVWM74_G3m8
MODEL_ID=gemini-2.5-flash

# Add these for Vertex AI
GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID  # Replace with your project ID
GOOGLE_CLOUD_LOCATION=us-central1     # Or your preferred region
AGENT_NAME=vibe-travel-agent

# Service account for Sheets/Docs
GOOGLE_APPLICATION_CREDENTIALS=/Users/catalinbotezat/vibe-travel-key.json
SHEETS_SERVICE_ACCOUNT_KEY_PATH=/Users/catalinbotezat/vibe-travel-key.json
USER_EMAIL_TO_SHARE_WITH=your-email@example.com  # Your email for sharing docs
```

### 3.2 Install Additional Dependencies

```bash
cd Vibe_Travel
source .venv/bin/activate

# Install Vertex AI SDK
pip install google-cloud-aiplatform google-cloud-storage
pip install --upgrade google-adk

# Save to requirements
pip freeze > requirements.txt
```

---

## Step 4: Deploy Agent to Vertex AI (15 minutes)

### 4.1 Create Deployment Script

I'll create this for you in the next step.

### 4.2 Prepare Agent for Deployment

Your `agent2.py` is already configured! It uses:
- ✅ `google_search` tool from ADK
- ✅ All sub-agents
- ✅ Google Sheets/Docs tools

### 4.3 Deploy to Vertex AI

```bash
cd /Users/catalinbotezat/Documents/NYUAD/NY/Advanced_Topics_Data_Science_LLM/Project/Vibe_Travel/my_agent

# Deploy the agent
python deploy_agent.py
```

(I'll create `deploy_agent.py` for you)

---

## Step 5: Test Your Deployed Agent (5 minutes)

### 5.1 Test with Python

```python
from google.cloud import aiplatform
from google.adk import Agent

# Initialize Vertex AI
aiplatform.init(
    project="YOUR_PROJECT_ID",
    location="us-central1"
)

# Load deployed agent
agent = Agent.load("vibe-travel-agent")

# Test with real-time search
response = agent.invoke({
    "messages": [{
        "role": "user",
        "content": "Find me the best 5-day beach vacation from New York with $3000 budget"
    }]
})

print(response)
```

### 5.2 Monitor Usage

1. Go to [Vertex AI Console](https://console.cloud.google.com/vertex-ai)
2. Navigate to **"Agent Builder"** or **"Generative AI"**
3. View your deployed agent
4. Monitor requests, costs, and performance

---

## 💰 Pricing Estimate

**For Development/Testing:**
- First 1,000 requests/month: Free tier
- After: ~$0.10 per 1,000 requests
- Storage: Minimal (~$0.01/month)

**For Production:**
- Based on usage
- Typical: $10-50/month for moderate use
- [See full pricing](https://cloud.google.com/vertex-ai/pricing)

---

## 🔧 Troubleshooting

### Error: "Permission Denied"
```bash
# Grant yourself admin role
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
    --member="user:YOUR_EMAIL@gmail.com" \
    --role="roles/owner"
```

### Error: "API not enabled"
```bash
# Enable all APIs again
gcloud services enable aiplatform.googleapis.com generativelanguage.googleapis.com
```

### Error: "Quota exceeded"
- Check [Quotas page](https://console.cloud.google.com/iam-admin/quotas)
- Request quota increase if needed
- Or wait for quota reset (usually next day)

---

## 🎯 Quick Setup Checklist

- [ ] Create Google Cloud project
- [ ] Enable billing (get $300 free credits)
- [ ] Enable Vertex AI API
- [ ] Install gcloud CLI
- [ ] Authenticate (`gcloud auth login`)
- [ ] Create service account
- [ ] Download service account key
- [ ] Update `.env` file with project details
- [ ] Install Vertex AI SDK (`pip install google-cloud-aiplatform`)
- [ ] Deploy agent using deployment script
- [ ] Test deployed agent
- [ ] Monitor usage in Cloud Console

---

## 📚 Next Steps After Deployment

1. **Test all features**: Location finder, flights, hotels, itinerary
2. **Monitor costs**: Check billing dashboard
3. **Scale up**: Increase quotas if needed
4. **Create UI**: Build a web interface (optional)
5. **Add features**: Customize agents for specific use cases

---

## 🔗 Important Links

- [Google Cloud Console](https://console.cloud.google.com/)
- [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)
- [Google ADK Docs](https://cloud.google.com/vertex-ai/docs/generative-ai/adk/overview)
- [Pricing Calculator](https://cloud.google.com/products/calculator)
- [Free Trial](https://cloud.google.com/free) - $300 free credits

---

## ⚠️ Important Notes

1. **Billing**: Even with free credits, keep monitoring your usage
2. **Security**: Never commit service account keys to git
3. **Quotas**: Start small, scale up as needed
4. **Region**: Use `us-central1` for best availability
5. **Testing**: Test thoroughly before production use

---

Need help with any step? Check the troubleshooting section or Google Cloud support!

