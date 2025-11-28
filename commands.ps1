#!/usr/bin/env powershell
# Multi-Agent Content Creator - Quick Commands
# Windows PowerShell Script for easy access to common operations

Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host "Multi-Agent Content Creator - Command Reference" -ForegroundColor Green
Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host ""

# Define functions for common operations
function Start-ContentCreator {
    Write-Host "🚀 Starting Multi-Agent Content Creator..." -ForegroundColor Green
    Set-Location "c:\Users\Heisenberg Raja\OneDrive\Desktop\agentic"
    D:\miniforge\python.exe main.py
}

function Install-Dependencies {
    Write-Host "📦 Installing dependencies with UV..." -ForegroundColor Green
    Set-Location "c:\Users\Heisenberg Raja\OneDrive\Desktop\agentic"
    D:\miniforge\python.exe -m uv pip install -r requirements.txt
    Write-Host "✅ Dependencies installed!" -ForegroundColor Green
}

function Update-Dependencies {
    Write-Host "🔄 Updating all dependencies with UV..." -ForegroundColor Yellow
    Set-Location "c:\Users\Heisenberg Raja\OneDrive\Desktop\agentic"
    D:\miniforge\python.exe -m uv pip install --upgrade -r requirements.txt
    Write-Host "✅ Dependencies updated!" -ForegroundColor Green
}

function List-Dependencies {
    Write-Host "📋 Installed packages:" -ForegroundColor Blue
    Set-Location "c:\Users\Heisenberg Raja\OneDrive\Desktop\agentic"
    D:\miniforge\python.exe -m uv pip list
}

function Clear-Cache {
    Write-Host "🧹 Clearing UV cache..." -ForegroundColor Yellow
    D:\miniforge\python.exe -m uv cache clean
    Write-Host "✅ Cache cleared!" -ForegroundColor Green
}

function View-Output {
    Write-Host "📄 Opening latest article output..." -ForegroundColor Blue
    Set-Location "c:\Users\Heisenberg Raja\OneDrive\Desktop\agentic"
    if (Test-Path "article_output.txt") {
        Get-Content article_output.txt | Out-Host
    } else {
        Write-Host "❌ No output file found. Run the creator first." -ForegroundColor Red
    }
}

function View-Memory {
    Write-Host "📊 Opening memory log..." -ForegroundColor Blue
    Set-Location "c:\Users\Heisenberg Raja\OneDrive\Desktop\agentic"
    if (Test-Path "memory_log.json") {
        Get-Content memory_log.json | ConvertFrom-Json | ConvertTo-Json -Depth 10 | Out-Host
    } else {
        Write-Host "❌ No memory log found. Run the creator first." -ForegroundColor Red
    }
}

function Show-Help {
    Write-Host ""
    Write-Host "Available Commands:" -ForegroundColor Cyan
    Write-Host "==================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "  Start-ContentCreator        🚀 Run the multi-agent content creator" -ForegroundColor Green
    Write-Host "  Install-Dependencies        📦 Install all required dependencies" -ForegroundColor Green
    Write-Host "  Update-Dependencies         🔄 Update all dependencies to latest" -ForegroundColor Green
    Write-Host "  List-Dependencies           📋 Show all installed packages" -ForegroundColor Green
    Write-Host "  Clear-Cache                 🧹 Clear UV package cache" -ForegroundColor Yellow
    Write-Host "  View-Output                 📄 View the latest generated article" -ForegroundColor Blue
    Write-Host "  View-Memory                 📊 View the memory log (JSON)" -ForegroundColor Blue
    Write-Host "  Show-Help                   ❓ Show this help message" -ForegroundColor Cyan
    Write-Host ""
}

# Display menu
Write-Host "Quick Start Commands:" -ForegroundColor Yellow
Write-Host "====================`n" -ForegroundColor Yellow

Write-Host "1. First time setup:" -ForegroundColor Cyan
Write-Host "   Install-Dependencies`n" -ForegroundColor White

Write-Host "2. Run the application:" -ForegroundColor Cyan
Write-Host "   Start-ContentCreator`n" -ForegroundColor White

Write-Host "3. View results:" -ForegroundColor Cyan
Write-Host "   View-Output`n" -ForegroundColor White

Write-Host "4. See all available commands:" -ForegroundColor Cyan
Write-Host "   Show-Help`n" -ForegroundColor White

Write-Host "Or directly execute any command from above:" -ForegroundColor Yellow
Write-Host "============================================`n" -ForegroundColor Yellow

# Export functions for use in PowerShell session
Export-ModuleMember -Function Start-ContentCreator, Install-Dependencies, Update-Dependencies, List-Dependencies, Clear-Cache, View-Output, View-Memory, Show-Help
