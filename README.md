# Game News Aggregator

Автономный сборщик новостей игровой и мобильной индустрии для **GitHub Actions + GitHub Pages**.

Система два раза в сутки:

1. проверяет включённые источники;
2. ищет RSS/Atom, датированные элементы HTML и sitemap;
3. нормализует URL и удаляет tracking-параметры;
4. не добавляет уже известные ссылки;
5. объединяет похожие публикации об одном событии;
6. рассчитывает предварительную важность по темам;
7. обновляет JSON, HTML и дневной архив;
8. сохраняет историю обратно в Git-репозиторий;
9. публикует `public/` через GitHub Pages.

## Что уже подготовлено

- 92 источника из истории HYPER NEWS;
- 30 источников включены по умолчанию;
- 1 183 исторические ссылки импортированы в `data/articles.jsonl`;
- исходный экспорт канала сохранён в `data/imports/hyper_news_result.json`;
- расписание: 07:17 и 19:17 в `Europe/Amsterdam`;
- GitHub Pages: HTML, `latest.json`, `status.json`, дневной архив;
- CI: конфигурация, Ruff и Pytest;
- OpenAI API и другие платные сервисы не требуются.

## Быстрый запуск

Полная инструкция: **[SETUP_RU.md](SETUP_RU.md)**.

### Локально, Windows PowerShell

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\bootstrap.ps1
.\scripts\collect.ps1 -Hours 168 -Source app2top-ru,pocketgamer-biz
.\scripts\preview.ps1
```

После запуска preview откройте `http://localhost:8000`.

### Основные команды

```powershell
python -m game_news validate-config
python -m game_news collect --hours 36
python -m game_news collect --dry-run --source app2top-ru
python -m game_news import-telegram --input data/imports/hyper_news_result.json
python -m game_news build-site
python -m pytest
python -m ruff check src tests
```

## Публичные файлы

После включения Pages:

```text
https://GITHUB_USER.github.io/REPOSITORY/
https://GITHUB_USER.github.io/REPOSITORY/latest.json
https://GITHUB_USER.github.io/REPOSITORY/status.json
https://GITHUB_USER.github.io/REPOSITORY/archive/YYYY-MM-DD.json
```

## Конфигурация

- `config/sources.yaml` — источники, приоритеты, включение и ручные RSS/sitemap.
- `config/keywords.yaml` — темы и веса предварительного ранжирования.
- `data/articles.jsonl` — накопительная история canonical URL.
- `data/state.json` — техническое состояние каждого источника.

Чтобы включить источник:

```yaml
enabled: true
```

Если autodiscovery не нашёл RSS, укажите его вручную:

```yaml
feed_urls:
  - https://example.com/feed.xml
```

## Принцип дат

Материал попадает в `latest.json`, только если удалось получить дату из RSS/Atom, JSON-LD, `<time>` или метаданных статьи. `sitemap.lastmod` допускается как низкоуверенный fallback и явно маркируется полями `date_source` и `date_confidence`.

## Ограничения

- Сайты могут менять HTML или блокировать IP GitHub Actions.
- Sitemap `lastmod` иногда означает дату изменения, а не публикации.
- Предварительный `importance_score` — эвристика, а не LLM-анализ.
- Финальный вывод «что изучить» должен формировать ChatGPT по `latest.json`.
