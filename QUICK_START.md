# Quick Start Guide - Vibe Travel

## 🚀 Quick Setup (3 Steps)

### Step 1: Activate Virtual Environment

If you already have a virtual environment (`.venv` or `venv`):

```bash
cd Vibe_Travel
source .venv/bin/activate  # macOS/Linux
# OR
source venv/bin/activate   # if using 'venv' instead of '.venv'
```

If you don't have a virtual environment yet:

```bash
cd Vibe_Travel
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies

**Option A: Using the installation script (Recommended)**
```bash
chmod +x install_dependencies.sh
./install_dependencies.sh
```

**Option B: Manual installation**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables

Create a `.env` file in the `Vibe_Travel` directory:

```bash
cd Vibe_Travel
touch .env
```

Add the following to your `.env` file:

```env
# Required
GEMINI_API_KEY=your_gemini_api_key_here
MODEL_ID=gemini-1.5-pro

# Optional (for full agent deployment)
GOOGLE_CLOUD_PROJECT=your_project_id
GOOGLE_CLOUD_LOCATION=us-central1

# Optional (for Google Sheets/Docs tools)
SHEETS_SERVICE_ACCOUNT_KEY_PATH=path/to/service-account.json
USER_EMAIL_TO_SHARE_WITH=your-email@example.com
```

## ✅ Verify Installation

```bash
# Make sure virtual environment is activated
source .venv/bin/activate  # or source venv/bin/activate

# Test imports
python -c "import google.generativeai; import google.adk; print('✅ All packages installed!')"
```

## 🎯 Run the Interactive Travel Planner

```bash
# Make sure virtual environment is activated
source .venv/bin/activate

# Navigate to my_agent directory
cd my_agent

# Run the interactive travel planner
python interactive_travel_planner.py
```

## 📋 What You'll Be Asked

1. **Starting Location**: Your current city/country
2. **Interests**: Comma-separated interests (e.g., beaches, museums, hiking)
3. **Budget**: Total budget in USD
4. **Trip Duration**: Number of days

## 🔧 Troubleshooting

### "No module named 'google.generativeai'"
```bash
source .venv/bin/activate
pip install google-generativeai
```

### "No module named 'google.adk'"
```bash
source .venv/bin/activate
pip install google-adk
```

### "GEMINI_API_KEY is not set"
1. Make sure you have a `.env` file in `Vibe_Travel` directory
2. Add `GEMINI_API_KEY=your_api_key_here` to the `.env` file
3. Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### Virtual Environment Not Activating
```bash
# Check if venv exists
ls -la | grep venv

# If it doesn't exist, create it
python3 -m venv venv
source venv/bin/activate
```

## 📚 Next Steps

- Read the full [SETUP.md](SETUP.md) for detailed instructions
- Check [README.md](README.md) for project overview
- Deploy the agent to Google Cloud AI Platform for full functionality

## 💡 Pro Tips

1. **Always activate virtual environment before running scripts**
   ```bash
   source .venv/bin/activate
   ```

2. **Check if virtual environment is active**
   - You should see `(venv)` or `(.venv)` in your terminal prompt

3. **Install new packages in virtual environment**
   ```bash
   source .venv/bin/activate
   pip install package_name
   pip freeze > requirements.txt  # Update requirements.txt
   ```

4. **Deactivate virtual environment when done**
   ```bash
   deactivate
   ```

