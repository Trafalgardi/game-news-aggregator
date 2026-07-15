.PHONY: install test lint validate collect preview import-history

install:
	python -m pip install --upgrade pip
	python -m pip install -e ".[dev]"

test:
	python -m pytest

lint:
	python -m ruff check src tests

validate:
	python -m game_news validate-config

collect:
	python -m game_news collect --hours 36

preview:
	python -m http.server 8000 --directory public

import-history:
	python -m game_news import-telegram --input data/imports/result.json
