# Импорт HYPER NEWS

`hyper_news_result.json` — исходный экспорт публичного Telegram-канала, использованный как стартовая история.

Команда повторного импорта:

```powershell
python -m game_news import-telegram --input data/imports/hyper_news_result.json
```

Импорт идемпотентен: повторный запуск не добавляет уже известные canonical URL.
`data/articles.jsonl` содержит нормализованные URL и минимальные метаданные для дедупликации.
