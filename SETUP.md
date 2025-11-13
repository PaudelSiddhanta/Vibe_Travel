# Vibe Travel - Setup Guide

This guide will help you set up a virtual environment and install all required dependencies for the Vibe Travel project.

## Prerequisites

- Python 3.10 or higher
- pip (Python package installer)
- Git (optional, for version control)

## Quick Setup

### Option 1: Automatic Setup (Recommended)

#### For macOS/Linux:
```bash
cd Vibe_Travel
chmod +x setup_venv.sh
./setup_venv.sh
```

#### For Windows (PowerShell):
```powershell
cd Vibe_Travel
.\setup_venv.ps1
```

### Option 2: Manual Setup

#### Step 1: Create Virtual Environment

```bash
cd Vibe_Travel
python3 -m venv venv
```

#### Step 2: Activate Virtual Environment

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

#### Step 3: Upgrade pip

```bash
pip install --upgrade pip
```

#### Step 4: Install Requirements

```bash
pip install -r requirements.txt
```

## Environment Variables Setup

Create a `.env` file in the `Vibe_Travel` directory with the following variables:

```env
# Google AI / Gemini API Key
GEMINI_API_KEY=your_gemini_api_key_here

# Model ID
MODEL_ID=gemini-1.5-pro

# Google Cloud Project (optional, for full agent deployment)
GOOGLE_CLOUD_PROJECT=your_project_id
GOOGLE_CLOUD_LOCATION=us-central1

# Google Sheets/Docs Service Account (optional, for tools.py)
SHEETS_SERVICE_ACCOUNT_KEY_PATH=path/to/service-account.json
USER_EMAIL_TO_SHARE_WITH=your-email@example.com
```

### Getting Your API Keys

1. **GEMINI_API_KEY**: 
   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy and paste it into your `.env` file

2. **Google Cloud Project** (for full agent deployment):
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the Vertex AI API

## Verify Installation

After setup, verify that everything is installed correctly:

```bash
# Activate virtual environment (if not already activated)
source venv/bin/activate  # macOS/Linux
# OR
.\venv\Scripts\Activate.ps1  # Windows PowerShell

# Test the installation
cd my_agent
python -c "import google.generativeai; import google.adk; print('✅ All packages installed successfully!')"
```

## Running the Interactive Travel Planner

```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux

# Navigate to my_agent directory
cd my_agent

# Run the interactive travel planner
python interactive_travel_planner.py
```

## Troubleshooting

### Issue: "No module named 'google.generativeai'"

**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux

# Install the package
pip install google-generativeai
```

### Issue: "No module named 'google.adk'"

**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux

# Install the package
pip install google-adk
```

### Issue: "GEMINI_API_KEY is not set"

**Solution:**
1. Create a `.env` file in the `Vibe_Travel` directory
2. Add `GEMINI_API_KEY=your_api_key_here`
3. Make sure `python-dotenv` is installed: `pip install python-dotenv`

### Issue: Permission denied on setup script

**Solution:**
```bash
# Make the script executable
chmod +x setup_venv.sh

# Then run it
./setup_venv.sh
```

## Project Structure

```
Vibe_Travel/
├── venv/                    # Virtual environment (created by setup)
├── my_agent/
│   ├── agent2.py           # Main agent definitions
│   ├── tools.py            # Google Sheets/Docs tools
│   ├── interactive_travel_planner.py  # Interactive planner script
│   └── test_agent2.py      # Test script
├── requirements.txt        # Python dependencies
├── setup_venv.sh          # Setup script (macOS/Linux)
├── setup_venv.ps1         # Setup script (Windows)
└── .env                   # Environment variables (create this)
```

## Next Steps

1. ✅ Set up virtual environment
2. ✅ Install dependencies
3. ✅ Configure environment variables
4. ✅ Run the interactive travel planner
5. 🚀 Deploy agent to Google Cloud AI Platform (optional, for full functionality)

## Additional Resources

- [Google ADK Documentation](https://cloud.google.com/vertex-ai/docs/agent-builder)
- [Google Generative AI Documentation](https://ai.google.dev/docs)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)

