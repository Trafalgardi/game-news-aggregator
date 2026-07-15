param([int]$Port = 8000)

$ErrorActionPreference = "Stop"
Set-Location (Split-Path -Parent $PSScriptRoot)
$Python = ".\.venv\Scripts\python.exe"

if (-not (Test-Path $Python)) {
    throw "Virtual environment not found. Run scripts/bootstrap.ps1 first."
}

Write-Host "Open http://localhost:$Port" -ForegroundColor Cyan
& $Python -m http.server $Port --directory public
