param(
    [int]$Hours = 36,
    [string[]]$Source = @()
)

$ErrorActionPreference = "Stop"
Set-Location (Split-Path -Parent $PSScriptRoot)
$Python = ".\.venv\Scripts\python.exe"

if (-not (Test-Path $Python)) {
    throw "Virtual environment not found. Run scripts/bootstrap.ps1 first."
}

$Args = @("-m", "game_news", "collect", "--hours", $Hours)
foreach ($Item in $Source) {
    $Args += @("--source", $Item)
}

& $Python @Args
