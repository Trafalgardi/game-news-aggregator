#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3.12 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -e '.[dev]'
.venv/bin/python -m game_news validate-config
.venv/bin/python -m ruff check src tests
.venv/bin/python -m pytest
.venv/bin/python -m game_news build-site
