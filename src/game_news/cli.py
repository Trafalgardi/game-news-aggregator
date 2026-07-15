from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from game_news.collector import collect
from game_news.config import load_config, validate_config
from game_news.site import build_site
from game_news.telegram_import import import_telegram_export


def _root(value: str | None) -> Path:
    return Path(value or ".").resolve()


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="game-news", description="Game news aggregator")
    parser.add_argument("--root", help="Repository root; defaults to current directory")
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate-config", help="Validate YAML configuration")
    validate.add_argument("--sources", default="config/sources.yaml")
    validate.add_argument("--keywords", default="config/keywords.yaml")

    collect_parser = sub.add_parser("collect", help="Collect and publish recent articles")
    collect_parser.add_argument("--sources-config", default="config/sources.yaml")
    collect_parser.add_argument("--keywords-config", default="config/keywords.yaml")
    collect_parser.add_argument("--hours", type=int, default=None)
    collect_parser.add_argument("--source", action="append", default=[])
    collect_parser.add_argument("--dry-run", action="store_true")
    collect_parser.add_argument("--strict-min-success", type=int, default=0)

    importer = sub.add_parser("import-telegram", help="Import Telegram JSON export into history")
    importer.add_argument("--input", required=True)
    importer.add_argument("--articles", default="data/articles.jsonl")

    site = sub.add_parser("build-site", help="Regenerate static HTML")
    site.add_argument("--public", default="public")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _parser()
    args = parser.parse_args(argv)
    root = _root(args.root)
    try:
        if args.command == "validate-config":
            config = load_config(root / args.sources, root / args.keywords)
            errors = validate_config(config)
            if errors:
                for error in errors:
                    print(f"ERROR: {error}", file=sys.stderr)
                return 2
            enabled = sum(1 for source in config.sources if source.enabled)
            print(f"Configuration is valid: {len(config.sources)} sources, {enabled} enabled")
            return 0

        if args.command == "collect":
            config = load_config(root / args.sources_config, root / args.keywords_config)
            result = collect(
                config=config,
                root=root,
                window_hours=args.hours,
                source_ids=args.source,
                dry_run=args.dry_run,
                strict_min_success=args.strict_min_success,
            )
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 0

        if args.command == "import-telegram":
            total, added = import_telegram_export(root / args.input, root / args.articles)
            print(f"Telegram URLs parsed: {total}; added to history: {added}")
            return 0

        if args.command == "build-site":
            output = build_site(root / args.public)
            print(f"Generated: {output}")
            return 0
    except Exception as exc:
        print(f"ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1
    return 0
