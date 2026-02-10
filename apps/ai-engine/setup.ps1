# AI Engine Setup Script
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  AI Meeting - Engine Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check Python
Write-Host "Checking Python installation..." -ForegroundColor Yellow
$pythonVersion = python --version 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "✗ Python not found. Please install Python 3.9+" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Installing dependencies..." -ForegroundColor Yellow
Write-Host "This will take 5-10 minutes on first run..." -ForegroundColor Gray
Write-Host ""

pip install -r requirements.txt

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "✓ Dependencies installed successfully!" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "✗ Installation failed. Check errors above." -ForegroundColor Red
    exit 1
}

# Setup .env file
Write-Host ""
if (Test-Path ".env") {
    Write-Host "✓ .env file already exists" -ForegroundColor Green
} else {
    Write-Host "Creating .env file..." -ForegroundColor Yellow
    Copy-Item ".env.example" ".env"
    Write-Host "✓ .env file created from .env.example" -ForegroundColor Green
    Write-Host ""
    Write-Host "⚠ IMPORTANT: Edit .env and add your HuggingFace token for diarization" -ForegroundColor Yellow
    Write-Host "   Get token from: https://huggingface.co/settings/tokens" -ForegroundColor Gray
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Setup Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Place audio file in: ..\..\data\raw_audio\test.wav" -ForegroundColor White
Write-Host "2. (Optional) Edit .env and add HF_TOKEN for speaker diarization" -ForegroundColor White
Write-Host "3. Run tests:" -ForegroundColor White
Write-Host "   python quick_start.py        # Quick STT test" -ForegroundColor Cyan
Write-Host "   python test_models.py        # Full test (STT + Diarization)" -ForegroundColor Cyan
Write-Host ""
