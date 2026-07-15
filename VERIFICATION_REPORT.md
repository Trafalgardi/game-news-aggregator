# Отчёт проверки перед передачей

## Проверено

- структура Python package;
- загрузка и валидация `sources.yaml` и `keywords.yaml`;
- 92 уникальных источника, 30 включены;
- импорт Telegram JSON, включая обычные URL и скрытые `href`;
- 1 183 уникальных URL в стартовой истории;
- нормализация URL и удаление tracking-параметров;
- RSS parsing;
- sitemap parsing;
- кластеризация похожих заголовков;
- сохранение JSONL;
- генерация `latest.json`, `status.json`, archive и HTML;
- статический сайт использует относительные URL и подходит для project Pages;
- Ruff;
- Pytest;
- YAML синтаксис workflow-файлов.

## Результат

```text
Configuration is valid: 92 sources, 30 enabled
All checks passed!
11 passed
```

## Ограничение среды проверки

Текущая среда сборки не имеет рабочего внешнего DNS для произвольных HTTP-запросов. Поэтому реальный сетевой сбор сайтов здесь не подтверждён. Сетевой уровень проверяется первым ручным запуском `Collect and publish news` на GitHub-hosted runner. Workflow запускается с `strict_min_success=0`, поэтому недоступность отдельных сайтов не блокирует публикацию диагностического `status.json`.
