# Gemini Models Reference

## ✅ Available Models (as of Nov 2024)

### Recommended for Travel Planning:

1. **`gemini-2.5-flash`** ⚡ (Current Default)
   - Fast responses
   - Good quality
   - Cost-effective
   - **Best for**: Quick travel planning, general queries

2. **`gemini-2.5-pro`** 🧠
   - Most powerful
   - Best reasoning
   - More expensive
   - **Best for**: Complex itineraries, detailed planning

3. **`gemini-flash-latest`** 🔄
   - Always uses latest flash version
   - Auto-updates
   - **Best for**: Production systems

4. **`gemini-pro-latest`** 🔄
   - Always uses latest pro version
   - Auto-updates
   - **Best for**: Production systems needing max power

### Experimental Models:

- `gemini-2.0-flash-exp` - Experimental flash model
- `gemini-2.0-pro-exp` - Experimental pro model
- `gemini-2.0-flash-thinking-exp` - With reasoning capabilities

### Specialized Models:

- `gemini-2.5-flash-lite` - Lighter, faster
- `gemini-2.0-flash-lite` - Lightweight version
- `learnlm-2.0-flash-experimental` - Learning-optimized

## 🔧 How to Change Model

### Method 1: Update .env file
```bash
# Edit .env file
MODEL_ID=gemini-2.5-pro  # or any other model
```

### Method 2: Set environment variable
```bash
export MODEL_ID=gemini-2.5-pro
python my_agent/interactive_travel_planner.py
```

### Method 3: Let the script use default
If `MODEL_ID` is not set, the script will use `gemini-2.5-flash` by default.

## 📊 Model Comparison

| Model | Speed | Quality | Cost | Use Case |
|-------|-------|---------|------|----------|
| `gemini-2.5-flash` | ⚡⚡⚡ | ⭐⭐⭐ | 💰 | General travel planning |
| `gemini-2.5-pro` | ⚡⚡ | ⭐⭐⭐⭐⭐ | 💰💰💰 | Complex itineraries |
| `gemini-flash-latest` | ⚡⚡⚡ | ⭐⭐⭐ | 💰 | Production (auto-updates) |
| `gemini-2.5-flash-lite` | ⚡⚡⚡⚡ | ⭐⭐ | 💰 | Simple queries |

## ❌ Invalid Model Names (DON'T USE)

- ~~`gemini-1.5-pro`~~ - Not available
- ~~`gemini-1.5-flash`~~ - Not available
- ~~`gemini-1.5-pro-latest`~~ - Not available
- ~~`gemini-1.5-flash-latest`~~ - Not available

**Note**: Gemini 1.5 models have been superseded by 2.0 and 2.5 versions.

## 🧪 Test a Model

```bash
cd Vibe_Travel
source .venv/bin/activate

# Test specific model
export MODEL_ID=gemini-2.5-pro
python -c "
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel(os.getenv('MODEL_ID'))
response = model.generate_content('Say hello')
print(f'✅ {os.getenv(\"MODEL_ID\")} works! Response: {response.text}')
"
```

## 📝 Current Setup

Your `.env` file now uses:
```env
MODEL_ID=gemini-2.5-flash
```

This provides a good balance of speed, quality, and cost for travel planning!

