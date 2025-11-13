# PowerShell script for Windows
# Setup script for Vibe Travel Project Virtual Environment

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "🌍 Vibe Travel - Virtual Environment Setup" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version
    Write-Host "✅ Found Python: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Error: Python is not installed!" -ForegroundColor Red
    Write-Host "   Please install Python 3.10 or higher" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Navigate to project directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# Create virtual environment
Write-Host "📦 Creating virtual environment..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "⚠️  Virtual environment 'venv' already exists" -ForegroundColor Yellow
    $recreate = Read-Host "   Do you want to recreate it? (y/n)"
    if ($recreate -eq "y" -or $recreate -eq "Y") {
        Write-Host "   Removing existing venv..." -ForegroundColor Yellow
        Remove-Item -Recurse -Force venv
        python -m venv venv
        Write-Host "✅ Virtual environment created" -ForegroundColor Green
    } else {
        Write-Host "   Using existing virtual environment" -ForegroundColor Yellow
    }
} else {
    python -m venv venv
    Write-Host "✅ Virtual environment created" -ForegroundColor Green
}

Write-Host ""

# Activate virtual environment
Write-Host "🔧 Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

# Upgrade pip
Write-Host "📦 Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip

# Install requirements
Write-Host ""
Write-Host "📦 Installing requirements..." -ForegroundColor Yellow
if (Test-Path "requirements.txt") {
    pip install -r requirements.txt
    Write-Host "✅ Requirements installed" -ForegroundColor Green
} else {
    Write-Host "⚠️  requirements.txt not found, installing basic packages..." -ForegroundColor Yellow
    pip install google-adk google-generativeai python-dotenv google-api-python-client google-auth
}

Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "✅ Setup Complete!" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "💡 To activate the virtual environment, run:" -ForegroundColor Yellow
Write-Host "   .\venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host ""
Write-Host "💡 To deactivate, run:" -ForegroundColor Yellow
Write-Host "   deactivate" -ForegroundColor White
Write-Host ""

