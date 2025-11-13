#!/bin/bash
# Setup script for Vibe Travel Project Virtual Environment

echo "=========================================="
echo "🌍 Vibe Travel - Virtual Environment Setup"
echo "=========================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed!"
    echo "   Please install Python 3.10 or higher"
    exit 1
fi

# Get Python version
PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✅ Found Python: $PYTHON_VERSION"
echo ""

# Navigate to project directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Create virtual environment
echo "📦 Creating virtual environment..."
if [ -d "venv" ]; then
    echo "⚠️  Virtual environment 'venv' already exists"
    read -p "   Do you want to recreate it? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "   Removing existing venv..."
        rm -rf venv
        python3 -m venv venv
        echo "✅ Virtual environment created"
    else
        echo "   Using existing virtual environment"
    fi
else
    python3 -m venv venv
    echo "✅ Virtual environment created"
fi

echo ""

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo ""
echo "📦 Installing requirements..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "✅ Requirements installed"
else
    echo "⚠️  requirements.txt not found, installing basic packages..."
    pip install google-adk google-generativeai python-dotenv google-api-python-client google-auth
fi

echo ""
echo "=========================================="
echo "✅ Setup Complete!"
echo "=========================================="
echo ""
echo "💡 To activate the virtual environment, run:"
echo "   source venv/bin/activate"
echo ""
echo "💡 To deactivate, run:"
echo "   deactivate"
echo ""
echo "💡 Make sure to create a .env file with:"
echo "   MODEL_ID=gemini-1.5-pro"
echo "   GEMINI_API_KEY=your_api_key_here"
echo "   GOOGLE_CLOUD_PROJECT=your_project_id"
echo "   GOOGLE_CLOUD_LOCATION=us-central1"
echo ""

