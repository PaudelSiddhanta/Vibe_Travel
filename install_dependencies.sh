#!/bin/bash
# Quick installation script for Vibe Travel dependencies

echo "=========================================="
echo "📦 Installing Vibe Travel Dependencies"
echo "=========================================="
echo ""

# Navigate to project directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check if virtual environment exists
if [ -d ".venv" ]; then
    echo "✅ Found virtual environment: .venv"
    source .venv/bin/activate
elif [ -d "venv" ]; then
    echo "✅ Found virtual environment: venv"
    source venv/bin/activate
else
    echo "⚠️  No virtual environment found. Creating one..."
    python3 -m venv venv
    source venv/bin/activate
fi

echo ""
echo "🔧 Virtual environment activated"
echo "   Python: $(which python)"
echo "   Python version: $(python --version)"
echo ""

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip --quiet

# Install requirements
echo ""
echo "📦 Installing requirements from requirements.txt..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo ""
    echo "✅ Requirements installed successfully!"
else
    echo "❌ requirements.txt not found!"
    echo "   Installing basic packages..."
    pip install google-adk google-generativeai python-dotenv google-api-python-client google-auth
fi

echo ""
echo "=========================================="
echo "✅ Installation Complete!"
echo "=========================================="
echo ""
echo "💡 To activate the virtual environment in the future:"
if [ -d ".venv" ]; then
    echo "   source .venv/bin/activate"
elif [ -d "venv" ]; then
    echo "   source venv/bin/activate"
fi
echo ""
echo "💡 Verify installation:"
echo "   python -c \"import google.generativeai; import google.adk; print('✅ All packages installed!')\""
echo ""

