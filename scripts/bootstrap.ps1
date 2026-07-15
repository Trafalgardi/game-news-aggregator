$ErrorActionPreference = "Stop"

Set-Location (Split-Path -Parent $PSScriptRoot)

if (-not (Test-Path ".venv")) {
    py -3.12 -m venv .venv
}

& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -e ".[dev]"
& .\.venv\Scripts\python.exe -m game_news validate-config
& .\.venv\Scripts\python.exe -m ruff check src tests
& .\.venv\Scripts\python.exe -m pytest
& .\.venv\Scripts\python.exe -m game_news build-site

Write-Host "Bootstrap completed successfully." -ForegroundColor Green
