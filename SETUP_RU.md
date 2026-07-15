# Пошаговая установка и проверка

## 0. Что понадобится

- аккаунт GitHub;
- Git для Windows;
- PowerShell 7 или стандартный Windows PowerShell;
- Python 3.12 — только для локальной проверки; GitHub Actions установит Python самостоятельно.

Рекомендуемое имя репозитория: `game-news-aggregator`.

---

## 1. Распаковать архив

Распакуйте ZIP в каталог без кириллицы и длинных путей, например:

```text
C:\Projects\game-news-aggregator
```

Архив содержит `.git`, поэтому в проводнике должна быть включена видимость скрытых элементов только для диагностики; вручную менять `.git` не нужно.

---

## 2. Локальная проверка до загрузки

Откройте PowerShell в корне репозитория:

```powershell
cd C:\Projects\game-news-aggregator
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\bootstrap.ps1
```

Ожидаемый результат:

```text
Configuration is valid: 92 sources, 30 enabled
All checks passed!
11 passed
Bootstrap completed successfully.
```

Если команда `py -3.12` не найдена, установите Python 3.12 и включите `Add python.exe to PATH`.

### Проверить импорт истории

```powershell
(Get-Content .\data\articles.jsonl).Count
```

Ожидается:

```text
1183
```

### Проверить один источник локально

```powershell
.\scripts\collect.ps1 -Hours 168 -Source app2top-ru
```

Это реальный сетевой запрос. Если локальный провайдер, корпоративная сеть или сайт блокирует запрос, команда выведет ошибку источника. Это не означает, что GitHub Actions также будет заблокирован.

### Открыть локальную страницу

В одном PowerShell:

```powershell
.\scripts\preview.ps1
```

Открыть:

```text
http://localhost:8000
```

Остановить сервер: `Ctrl+C`.

---

## 3. Создать пустой репозиторий на GitHub

На GitHub:

1. Нажмите **New repository**.
2. Имя: `game-news-aggregator`.
3. Выберите **Public**.
4. Не включайте `Add a README file`.
5. Не добавляйте `.gitignore`.
6. Не добавляйте лицензию.
7. Нажмите **Create repository**.

Пустой репозиторий нужен, потому что в ZIP уже есть история Git и первый commit.

---

## 4. Подключить remote и отправить repository

В PowerShell замените `YOUR_GITHUB_LOGIN`:

```powershell
cd C:\Projects\game-news-aggregator
git status
git branch --show-current
git remote -v
git remote add origin https://github.com/YOUR_GITHUB_LOGIN/game-news-aggregator.git
git push -u origin main
```

Проверка перед push:

- ветка должна быть `main`;
- `git status` должен показывать чистое рабочее дерево;
- `git remote -v` до добавления origin не должен содержать старой ссылки.

Если `origin` уже существует:

```powershell
git remote set-url origin https://github.com/YOUR_GITHUB_LOGIN/game-news-aggregator.git
git push -u origin main
```

---

## 5. Исправить User-Agent

Откройте `config/sources.yaml` и замените:

```text
https://github.com/OWNER/game-news-aggregator
```

на реальный URL репозитория. Затем:

```powershell
git add config/sources.yaml
git commit -m "config: set repository user agent"
git push
```

Это не обязательно для первого запуска, но правильно идентифицирует сборщик перед сайтами.

---

## 6. Разрешить GitHub Actions записывать историю

В репозитории GitHub:

1. **Settings**.
2. **Actions** → **General**.
3. Найдите **Workflow permissions**.
4. Выберите **Read and write permissions**.
5. Нажмите **Save**.

Без этого шаг `git push` внутри Action не сможет обновлять `data/articles.jsonl`, `data/state.json` и `public/`.

Если на `main` включена branch protection с обязательным pull request, временно отключите её либо разрешите GitHub Actions push. Для первого запуска защита ветки не нужна.

---

## 7. Включить GitHub Pages

1. **Settings** → **Pages**.
2. В блоке **Build and deployment** выберите **Source: GitHub Actions**.
3. Сохраните настройку, если GitHub показывает кнопку сохранения.

Workflow сам загружает каталог `public` через Pages artifact и выполняет deployment.

---

## 8. Первый ручной запуск

1. Откройте вкладку **Actions**.
2. Выберите workflow **Collect and publish news**.
3. Нажмите **Run workflow**.
4. Ветка: `main`.
5. `window_hours`: `168` для первой проверки, чтобы увидеть материалы за 7 дней.
6. `strict_min_success`: `0`.
7. Нажмите **Run workflow**.

Параметр `0` означает: отдельные заблокированные сайты не останавливают весь pipeline.

### Что должно произойти

Job `collect`:

1. checkout;
2. установка Python;
3. проверка конфигурации;
4. 11 тестов;
5. сетевой сбор;
6. обновление JSON/HTML;
7. commit новых данных;
8. загрузка Pages artifact.

Job `deploy` публикует сайт.

---

## 9. Проверить результат

### 9.1. Проверить Action

В зелёном workflow откройте шаг **Collect news and build static site**. В конце должен быть JSON примерно такого вида:

```json
{
  "selected_sources": 30,
  "successful_sources": 18,
  "candidate_count": 120,
  "added_count": 35,
  "latest_count": 27
}
```

Цифры зависят от доступности сайтов и текущих публикаций.

### 9.2. Проверить новый commit

На вкладке **Code** должен появиться commit:

```text
data: update game news feed
```

Если новых URL нет, commit не создаётся — это нормальное поведение.

### 9.3. Проверить Pages

URL отображается в job `deploy` и в **Settings → Pages**. Обычно:

```text
https://YOUR_GITHUB_LOGIN.github.io/game-news-aggregator/
```

Проверьте четыре адреса:

```text
/
/latest.json
/status.json
/archive/YYYY-MM-DD.json
```

### 9.4. Проверить состояние источников

В `status.json`:

- `ok` — найдены свежие датированные материалы;
- `warning` — сайт доступен, но свежих датированных материалов не найдено;
- `error` — сетевой ответ, DNS, 403, timeout или ошибка парсинга.

Откройте конкретную запись в `sources` и посмотрите:

- `method`;
- `error`;
- `discovered_feeds`;
- `discovered_sitemaps`;
- `elapsed_ms`.

---

## 10. Стабилизация источников

После 2–3 ручных запусков:

1. Посмотрите источники со статусом `error`.
2. Для сайта с известным RSS добавьте URL в `feed_urls`.
3. Для сайта без RSS добавьте sitemap в `sitemap_urls`.
4. Если сайт стабильно блокирует GitHub, установите `enabled: false`.
5. Включайте дополнительные источники партиями по 5–10.

Пример:

```yaml
- id: example-com
  name: Example
  domain: example.com
  home_url: https://example.com/
  enabled: true
  feed_urls:
    - https://example.com/rss.xml
  sitemap_urls:
    - https://example.com/sitemap.xml
```

После изменения:

```powershell
git add config/sources.yaml
git commit -m "config: stabilize news sources"
git push
```

---

## 11. Вернуть окно с 168 на 36 часов

Ручной параметр не меняет файл workflow. Плановые запуски автоматически используют 36 часов.

Расписание в `.github/workflows/collect-news.yml`:

```yaml
- cron: "17 7 * * *"
  timezone: "Europe/Amsterdam"
- cron: "17 19 * * *"
  timezone: "Europe/Amsterdam"
```

Для другого времени измените cron и timezone, затем commit/push.

---

## 12. Подключить ежедневный анализ ChatGPT

Откройте `CHATGPT_TASK_PROMPT_RU.md` и замените:

```text
LATEST_JSON_URL
STATUS_JSON_URL
```

на реальные Pages URL.

Создайте ежедневную задачу после того, как `latest.json` стабильно открывается без авторизации.

---

## Критерии успешного запуска

Система считается установленной, если одновременно выполняются условия:

- CI зелёный;
- ручной workflow зелёный;
- `data: update game news feed` создаётся при наличии новых статей;
- Pages открывается;
- `latest.json` содержит корректный JSON;
- `status.json` показывает результаты 30 источников;
- следующий ручной запуск не добавляет повторно те же canonical URL;
- дневной файл создаётся в `public/archive/`.
