# Диагностика источников

Обновлено: `2026-07-16T07:42:42Z`

Исключено вручную: **5**

## Сводка

- `no_articles_found`: **22**
- `no_recent_articles`: **12**
- `blocked`: **7**
- `timeout`: **4**

## Проблемные источники

### Appodeal (`appodeal-com`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `8608 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `12`

  - `homepage` → `ok` — https://appodeal.com/
  - `feed-common` → `empty` — https://appodeal.com/feed
  - `feed-common` → `empty` — https://appodeal.com/rss
  - `feed-common` → `error` — https://appodeal.com/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://appodeal.com/rss.xml
  - `feed-common` → `error` — https://appodeal.com/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://appodeal.com/feed.xml
  - `feed-common` → `error` — https://appodeal.com/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://appodeal.com/atom.xml
  - `html-listing` → `empty` — https://appodeal.com/
  - `robots` → `ok` — https://appodeal.com/robots.txt
  - `sitemap` → `ok` — https://appodeal.com/sitemap_index.xml
  - `sitemap-child` → `ok` — https://appodeal.com/page-sitemap.xml
  - `sitemap-child` → `ok` — https://appodeal.com/post-sitemap.xml
  - `sitemap-child` → `ok` — https://appodeal.com/case_studies-sitemap.xml

### AppQuantum (`appquantum-com`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `1959 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `9`

  - `homepage` → `ok` — https://appquantum.com/
  - `feed-common` → `error` — https://appquantum.com/feed — HTTPError: 404 Client Error: Not Found for url: https://appquantum.com/feed
  - `feed-common` → `error` — https://appquantum.com/rss — HTTPError: 404 Client Error: Not Found for url: https://appquantum.com/rss
  - `feed-common` → `error` — https://appquantum.com/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://appquantum.com/rss.xml
  - `feed-common` → `error` — https://appquantum.com/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://appquantum.com/feed.xml
  - `feed-common` → `error` — https://appquantum.com/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://appquantum.com/atom.xml
  - `html-listing` → `empty` — https://appquantum.com/
  - `robots` → `error` — https://appquantum.com/robots.txt — HTTPError: 404 Client Error: Not Found for url: https://appquantum.com/robots.txt
  - `sitemap` → `error` — https://appquantum.com/sitemap.xml — HTTPError: 404 Client Error: Not Found for url: https://appquantum.com/sitemap.xml

### AppQuantum Hybrid Casual (`hybridcasual-appquantum-com`)

- Статус: `warning`
- Категория: `blocked`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `1603 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `8`

  - `homepage` → `error` — https://hybridcasual.appquantum.com/ — HTTPError: 403 Client Error: Forbidden for url: https://hybridcasual.appquantum.com/
  - `feed-common` → `error` — https://hybridcasual.appquantum.com/feed — HTTPError: 403 Client Error: Forbidden for url: https://hybridcasual.appquantum.com/feed
  - `feed-common` → `error` — https://hybridcasual.appquantum.com/rss — HTTPError: 403 Client Error: Forbidden for url: https://hybridcasual.appquantum.com/rss
  - `feed-common` → `error` — https://hybridcasual.appquantum.com/rss.xml — HTTPError: 403 Client Error: Forbidden for url: https://hybridcasual.appquantum.com/rss.xml
  - `feed-common` → `error` — https://hybridcasual.appquantum.com/feed.xml — HTTPError: 403 Client Error: Forbidden for url: https://hybridcasual.appquantum.com/feed.xml
  - `feed-common` → `error` — https://hybridcasual.appquantum.com/atom.xml — HTTPError: 403 Client Error: Forbidden for url: https://hybridcasual.appquantum.com/atom.xml
  - `robots` → `error` — https://hybridcasual.appquantum.com/robots.txt — HTTPError: 403 Client Error: Forbidden for url: https://hybridcasual.appquantum.com/robots.txt
  - `sitemap` → `error` — https://hybridcasual.appquantum.com/sitemap.xml — HTTPError: 403 Client Error: Forbidden for url: https://hybridcasual.appquantum.com/sitemap.xml

### Apptica (`apptica-com`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `5968 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `11`

  - `homepage` → `ok` — https://apptica.com/
  - `feed-common` → `empty` — https://apptica.com/en/feed
  - `feed-common` → `empty` — https://apptica.com/en/rss
  - `feed-common` → `empty` — https://apptica.com/en/rss.xml
  - `feed-common` → `empty` — https://apptica.com/en/feed.xml
  - `feed-common` → `empty` — https://apptica.com/en/atom.xml
  - `html-listing` → `empty` — https://apptica.com/en/
  - `robots` → `ok` — https://apptica.com/robots.txt
  - `sitemap` → `ok` — https://apptica.com/sitemap.xml
  - `sitemap-child` → `ok` — https://apptica.com/sitemap-0.xml
  - `sitemap-child` → `ok` — https://apptica.com/blog/sitemap.xml

### Azur Games Blog (`azurgames-com`)

- Статус: `warning`
- Категория: `no_recent_articles`
- Метод: `feed-common`
- Получено кандидатов: `9`
- Принято: `0`
- Причины отбраковки: `{"too_old": 9}`
- Время: `2446 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `2`

  - `homepage` → `ok` — https://azurgames.com/
  - `feed-common` → `ok` — https://azurgames.com/feed

### BlockchainGamer.biz (`blockchaingamer-biz`)

- Статус: `warning`
- Категория: `blocked`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `768 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `8`

  - `homepage` → `error` — https://blockchaingamer.biz/ — HTTPError: 403 Client Error: Forbidden for url: https://www.blockchaingamer.biz/
  - `feed-common` → `error` — https://blockchaingamer.biz/feed — HTTPError: 403 Client Error: Forbidden for url: https://www.blockchaingamer.biz/feed
  - `feed-common` → `error` — https://blockchaingamer.biz/rss — HTTPError: 403 Client Error: Forbidden for url: https://www.blockchaingamer.biz/rss
  - `feed-common` → `error` — https://blockchaingamer.biz/rss.xml — HTTPError: 403 Client Error: Forbidden for url: https://www.blockchaingamer.biz/rss.xml
  - `feed-common` → `error` — https://blockchaingamer.biz/feed.xml — HTTPError: 403 Client Error: Forbidden for url: https://www.blockchaingamer.biz/feed.xml
  - `feed-common` → `error` — https://blockchaingamer.biz/atom.xml — HTTPError: 403 Client Error: Forbidden for url: https://www.blockchaingamer.biz/atom.xml
  - `robots` → `ok` — https://blockchaingamer.biz/robots.txt
  - `sitemap` → `error` — https://blockchaingamer.biz/sitemap.xml — HTTPError: 403 Client Error: Forbidden for url: https://www.blockchaingamer.biz/sitemap.xml

### Business of Apps (`businessofapps-com`)

- Статус: `warning`
- Категория: `blocked`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `195 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `8`

  - `homepage` → `error` — https://businessofapps.com/ — HTTPError: 403 Client Error: Forbidden for url: https://businessofapps.com/
  - `feed-common` → `error` — https://businessofapps.com/feed — HTTPError: 403 Client Error: Forbidden for url: https://businessofapps.com/feed
  - `feed-common` → `error` — https://businessofapps.com/rss — HTTPError: 403 Client Error: Forbidden for url: https://businessofapps.com/rss
  - `feed-common` → `error` — https://businessofapps.com/rss.xml — HTTPError: 403 Client Error: Forbidden for url: https://businessofapps.com/rss.xml
  - `feed-common` → `error` — https://businessofapps.com/feed.xml — HTTPError: 403 Client Error: Forbidden for url: https://businessofapps.com/feed.xml
  - `feed-common` → `error` — https://businessofapps.com/atom.xml — HTTPError: 403 Client Error: Forbidden for url: https://businessofapps.com/atom.xml
  - `robots` → `error` — https://businessofapps.com/robots.txt — HTTPError: 403 Client Error: Forbidden for url: https://businessofapps.com/robots.txt
  - `sitemap` → `error` — https://businessofapps.com/sitemap.xml — HTTPError: 403 Client Error: Forbidden for url: https://businessofapps.com/sitemap.xml

### CrazyLabs (`crazylabs-com`)

- Статус: `warning`
- Категория: `no_recent_articles`
- Метод: `feed`
- Получено кандидатов: `10`
- Принято: `0`
- Причины отбраковки: `{"too_old": 10}`
- Время: `475 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `2`

  - `homepage` → `ok` — https://crazylabs.com/
  - `feed-discovered` → `ok` — https://www.crazylabs.com/feed/

### CTech (`calcalistech-com`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `5544 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `9`

  - `homepage` → `ok` — https://calcalistech.com/
  - `feed-common` → `error` — https://www.calcalistech.com/ctechnews/feed — HTTPError: 404 Client Error: Not Found for url: https://www.calcalistech.com/ctechnews/feed
  - `feed-common` → `error` — https://www.calcalistech.com/ctechnews/rss — HTTPError: 404 Client Error: Not Found for url: https://www.calcalistech.com/ctechnews/rss
  - `feed-common` → `error` — https://www.calcalistech.com/ctechnews/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://www.calcalistech.com/ctechnews/rss.xml
  - `feed-common` → `error` — https://www.calcalistech.com/ctechnews/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://www.calcalistech.com/ctechnews/feed.xml
  - `feed-common` → `error` — https://www.calcalistech.com/ctechnews/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://www.calcalistech.com/ctechnews/atom.xml
  - `html-listing` → `empty` — https://www.calcalistech.com/ctechnews
  - `robots` → `ok` — https://www.calcalistech.com/robots.txt
  - `sitemap` → `error` — https://www.calcalistech.com/sitemap.xml — HTTPError: 404 Client Error: Not Found for url: https://www.calcalistech.com/sitemap.xml

### data.ai (`data-ai`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `38092 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `20`

  - `homepage` → `ok` — https://data.ai/
  - `feed-common` → `empty` — https://www.data.ai/account/login/feed
  - `feed-common` → `empty` — https://www.data.ai/account/login/rss
  - `feed-common` → `empty` — https://www.data.ai/account/login/rss.xml
  - `feed-common` → `empty` — https://www.data.ai/account/login/feed.xml
  - `feed-common` → `empty` — https://www.data.ai/account/login/atom.xml
  - `html-listing` → `empty` — https://www.data.ai/account/login/
  - `robots` → `ok` — https://www.data.ai/robots.txt
  - `sitemap` → `error` — https://www.data.ai/mkt/sitemap/index.xml — ParseError: not well-formed (invalid token): line 9, column 381
  - `sitemap` → `ok` — https://www.data.ai/cn/sitemap.xml
  - `sitemap` → `ok` — https://www.data.ai/app_sitemap_index.xml
  - `sitemap-child` → `ok` — https://www.data.ai/cn/ios_app_sitemap.xml
  - `sitemap-child` → `ok` — https://www.data.ai/de/ios_app_sitemap.xml
  - `sitemap-child` → `ok` — https://www.data.ai/en/ios_app_sitemap.xml
  - `sitemap-child` → `ok` — https://www.data.ai/es/ios_app_sitemap.xml
  - `sitemap-child` → `ok` — https://www.data.ai/fr/ios_app_sitemap.xml
  - `sitemap-child` → `ok` — https://www.data.ai/jp/ios_app_sitemap.xml
  - `sitemap` → `ok` — https://www.data.ai/sitemap.xml
  - `sitemap-child` → `ok` — https://www.data.ai/app_sitemap_index.xml
  - `sitemap-child` → `error` — https://www.data.ai/mkt/sitemap/index.xml — ParseError: not well-formed (invalid token): line 9, column 381

### Deconstructor of Fun (`deconstructoroffun-com`)

- Статус: `warning`
- Категория: `no_recent_articles`
- Метод: `sitemap`
- Получено кандидатов: `1`
- Принято: `0`
- Причины отбраковки: `{"too_old": 1}`
- Время: `2777 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `10`

  - `homepage` → `ok` — https://deconstructoroffun.com/
  - `feed-common` → `error` — https://www.deconstructoroffun.com/feed — HTTPError: 404 Client Error: Not Found for url: https://www.deconstructoroffun.com/feed
  - `feed-common` → `error` — https://www.deconstructoroffun.com/rss — HTTPError: 404 Client Error: Not Found for url: https://www.deconstructoroffun.com/rss
  - `feed-common` → `error` — https://www.deconstructoroffun.com/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://www.deconstructoroffun.com/rss.xml
  - `feed-common` → `error` — https://www.deconstructoroffun.com/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://www.deconstructoroffun.com/feed.xml
  - `feed-common` → `error` — https://www.deconstructoroffun.com/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://www.deconstructoroffun.com/atom.xml
  - `html-listing` → `empty` — https://www.deconstructoroffun.com/
  - `robots` → `ok` — https://www.deconstructoroffun.com/robots.txt
  - `sitemap` → `ok` — https://www.deconstructoroffun.com/sitemap.xml
  - `article-enrich` → `ok` — https://www.deconstructoroffun.com/home

### Ducky (`playducky-com`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `1503 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `9`

  - `homepage` → `ok` — https://playducky.com/
  - `feed-common` → `error` — https://playducky.com/feed — HTTPError: 404 Client Error: Not Found for url: https://playducky.com/feed
  - `feed-common` → `error` — https://playducky.com/rss — HTTPError: 404 Client Error: Not Found for url: https://playducky.com/rss
  - `feed-common` → `error` — https://playducky.com/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://playducky.com/rss.xml
  - `feed-common` → `error` — https://playducky.com/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://playducky.com/feed.xml
  - `feed-common` → `error` — https://playducky.com/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://playducky.com/atom.xml
  - `html-listing` → `empty` — https://playducky.com/
  - `robots` → `ok` — https://playducky.com/robots.txt
  - `sitemap` → `ok` — https://playducky.com/sitemap.xml

### Elite Game Developers (`elitegamedevelopers-substack-com`)

- Статус: `warning`
- Категория: `blocked`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `290 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `8`

  - `homepage` → `error` — https://elitegamedevelopers.substack.com/ — HTTPError: 403 Client Error: Forbidden for url: https://elitegamedevelopers.substack.com/
  - `feed-common` → `error` — https://elitegamedevelopers.substack.com/feed — HTTPError: 403 Client Error: Forbidden for url: https://elitegamedevelopers.substack.com/feed
  - `feed-common` → `error` — https://elitegamedevelopers.substack.com/rss — HTTPError: 403 Client Error: Forbidden for url: https://elitegamedevelopers.substack.com/rss
  - `feed-common` → `error` — https://elitegamedevelopers.substack.com/rss.xml — HTTPError: 403 Client Error: Forbidden for url: https://elitegamedevelopers.substack.com/rss.xml
  - `feed-common` → `error` — https://elitegamedevelopers.substack.com/feed.xml — HTTPError: 403 Client Error: Forbidden for url: https://elitegamedevelopers.substack.com/feed.xml
  - `feed-common` → `error` — https://elitegamedevelopers.substack.com/atom.xml — HTTPError: 403 Client Error: Forbidden for url: https://elitegamedevelopers.substack.com/atom.xml
  - `robots` → `error` — https://elitegamedevelopers.substack.com/robots.txt — HTTPError: 403 Client Error: Forbidden for url: https://elitegamedevelopers.substack.com/robots.txt
  - `sitemap` → `error` — https://elitegamedevelopers.substack.com/sitemap.xml — HTTPError: 403 Client Error: Forbidden for url: https://elitegamedevelopers.substack.com/sitemap.xml

### GameAnalytics (`gameanalytics-com`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `1169 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `9`

  - `homepage` → `ok` — https://gameanalytics.com/
  - `feed-common` → `error` — https://www.gameanalytics.com/feed — HTTPError: 404 Client Error: Not Found for url: https://www.gameanalytics.com/feed
  - `feed-common` → `error` — https://www.gameanalytics.com/rss — HTTPError: 404 Client Error: Not Found for url: https://www.gameanalytics.com/rss
  - `feed-common` → `error` — https://www.gameanalytics.com/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://www.gameanalytics.com/rss.xml
  - `feed-common` → `error` — https://www.gameanalytics.com/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://www.gameanalytics.com/feed.xml
  - `feed-common` → `error` — https://www.gameanalytics.com/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://www.gameanalytics.com/atom.xml
  - `html-listing` → `empty` — https://www.gameanalytics.com/
  - `robots` → `ok` — https://www.gameanalytics.com/robots.txt
  - `sitemap` → `ok` — https://www.gameanalytics.com/sitemap.xml

### GamingonPhone (`gamingonphone-com`)

- Статус: `warning`
- Категория: `blocked`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `87 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `8`

  - `homepage` → `error` — https://gamingonphone.com/ — HTTPError: 403 Client Error: Forbidden for url: https://gamingonphone.com/
  - `feed-common` → `error` — https://gamingonphone.com/feed — HTTPError: 403 Client Error: Forbidden for url: https://gamingonphone.com/feed
  - `feed-common` → `error` — https://gamingonphone.com/rss — HTTPError: 403 Client Error: Forbidden for url: https://gamingonphone.com/rss
  - `feed-common` → `error` — https://gamingonphone.com/rss.xml — HTTPError: 403 Client Error: Forbidden for url: https://gamingonphone.com/rss.xml
  - `feed-common` → `error` — https://gamingonphone.com/feed.xml — HTTPError: 403 Client Error: Forbidden for url: https://gamingonphone.com/feed.xml
  - `feed-common` → `error` — https://gamingonphone.com/atom.xml — HTTPError: 403 Client Error: Forbidden for url: https://gamingonphone.com/atom.xml
  - `robots` → `error` — https://gamingonphone.com/robots.txt — HTTPError: 403 Client Error: Forbidden for url: https://gamingonphone.com/robots.txt
  - `sitemap` → `error` — https://gamingonphone.com/sitemap.xml — HTTPError: 403 Client Error: Forbidden for url: https://gamingonphone.com/sitemap.xml

### Homa (`homagames-com`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `441 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `9`

  - `homepage` → `ok` — https://homagames.com/
  - `feed-common` → `error` — https://www.homagames.com/feed — HTTPError: 404 Client Error: Not Found for url: https://www.homagames.com/feed
  - `feed-common` → `error` — https://www.homagames.com/rss — HTTPError: 404 Client Error: Not Found for url: https://www.homagames.com/rss
  - `feed-common` → `error` — https://www.homagames.com/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://www.homagames.com/rss.xml
  - `feed-common` → `error` — https://www.homagames.com/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://www.homagames.com/feed.xml
  - `feed-common` → `error` — https://www.homagames.com/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://www.homagames.com/atom.xml
  - `html-listing` → `empty` — https://www.homagames.com/
  - `robots` → `error` — https://www.homagames.com/robots.txt — HTTPError: 404 Client Error: Not Found for url: https://www.homagames.com/robots.txt
  - `sitemap` → `error` — https://www.homagames.com/sitemap.xml — HTTPError: 404 Client Error: Not Found for url: https://www.homagames.com/sitemap.xml

### ironSource (`is-com`)

- Статус: `warning`
- Категория: `timeout`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `76549 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `8`

  - `homepage` → `error` — https://is.com/ — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /grow/ (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `feed-common` → `error` — https://is.com/feed — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /grow/ (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `feed-common` → `error` — https://is.com/rss — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /grow/ (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `feed-common` → `error` — https://is.com/rss.xml — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /grow/ (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `feed-common` → `error` — https://is.com/feed.xml — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /grow/ (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `feed-common` → `error` — https://is.com/atom.xml — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /grow/ (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `robots` → `error` — https://is.com/robots.txt — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /grow (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `sitemap` → `error` — https://is.com/sitemap.xml — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /grow/ (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))

### Kwalee Blog (`kwalee-com`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `2571 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `9`

  - `homepage` → `ok` — https://kwalee.com/
  - `feed-common` → `error` — https://www.kwalee.com/feed — HTTPError: 404 Client Error: Not Found for url: https://www.kwalee.com/feed
  - `feed-common` → `error` — https://www.kwalee.com/rss — HTTPError: 404 Client Error: Not Found for url: https://www.kwalee.com/rss
  - `feed-common` → `error` — https://www.kwalee.com/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://www.kwalee.com/rss.xml
  - `feed-common` → `error` — https://www.kwalee.com/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://www.kwalee.com/feed.xml
  - `feed-common` → `error` — https://www.kwalee.com/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://www.kwalee.com/atom.xml
  - `html-listing` → `empty` — https://www.kwalee.com
  - `robots` → `ok` — https://www.kwalee.com/robots.txt
  - `sitemap` → `ok` — https://www.kwalee.com/sitemap.xml

### Liftoff Content (`content-liftoff-io`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `837 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `8`

  - `homepage` → `error` — https://content.liftoff.io/ — HTTPError: 404 Client Error: Not Found for url: https://content.liftoff.io/
  - `feed-common` → `error` — https://content.liftoff.io/feed — HTTPError: 404 Client Error: Not Found for url: https://content.liftoff.io/feed
  - `feed-common` → `error` — https://content.liftoff.io/rss — HTTPError: 404 Client Error: Not Found for url: https://content.liftoff.io/rss
  - `feed-common` → `error` — https://content.liftoff.io/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://content.liftoff.io/rss.xml
  - `feed-common` → `error` — https://content.liftoff.io/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://content.liftoff.io/feed.xml
  - `feed-common` → `error` — https://content.liftoff.io/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://content.liftoff.io/atom.xml
  - `robots` → `ok` — https://content.liftoff.io/robots.txt
  - `sitemap` → `empty` — https://content.liftoff.io/sitemap.xml

### Liquid & Grit (`blog-liquidandgrit-com`)

- Статус: `warning`
- Категория: `no_recent_articles`
- Метод: `feed`
- Получено кандидатов: `10`
- Принято: `0`
- Причины отбраковки: `{"too_old": 10}`
- Время: `2467 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `2`

  - `homepage` → `ok` — https://blog.liquidandgrit.com/
  - `feed-discovered` → `ok` — https://blog.liquidandgrit.com/feed

### Matej Lancaric Substack (`lancaric-substack-com`)

- Статус: `warning`
- Категория: `blocked`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `572 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `8`

  - `homepage` → `error` — https://lancaric.substack.com/ — HTTPError: 403 Client Error: Forbidden for url: https://lancaric.substack.com/
  - `feed-common` → `error` — https://lancaric.substack.com/feed — HTTPError: 403 Client Error: Forbidden for url: https://lancaric.substack.com/feed
  - `feed-common` → `error` — https://lancaric.substack.com/rss — HTTPError: 403 Client Error: Forbidden for url: https://lancaric.substack.com/rss
  - `feed-common` → `error` — https://lancaric.substack.com/rss.xml — HTTPError: 403 Client Error: Forbidden for url: https://lancaric.substack.com/rss.xml
  - `feed-common` → `error` — https://lancaric.substack.com/feed.xml — HTTPError: 403 Client Error: Forbidden for url: https://lancaric.substack.com/feed.xml
  - `feed-common` → `error` — https://lancaric.substack.com/atom.xml — HTTPError: 403 Client Error: Forbidden for url: https://lancaric.substack.com/atom.xml
  - `robots` → `error` — https://lancaric.substack.com/robots.txt — HTTPError: 403 Client Error: Forbidden for url: https://lancaric.substack.com/robots.txt
  - `sitemap` → `error` — https://lancaric.substack.com/sitemap.xml — HTTPError: 403 Client Error: Forbidden for url: https://lancaric.substack.com/sitemap.xml

### Mattel Corporate (`corporate-mattel-com`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `2280 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `9`

  - `homepage` → `ok` — https://corporate.mattel.com/
  - `feed-common` → `error` — https://corporate.mattel.com/feed — HTTPError: 404 Client Error: Not Found for url: https://corporate.mattel.com/feed
  - `feed-common` → `error` — https://corporate.mattel.com/rss — HTTPError: 404 Client Error: Not Found for url: https://corporate.mattel.com/rss
  - `feed-common` → `error` — https://corporate.mattel.com/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://corporate.mattel.com/rss.xml
  - `feed-common` → `error` — https://corporate.mattel.com/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://corporate.mattel.com/feed.xml
  - `feed-common` → `error` — https://corporate.mattel.com/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://corporate.mattel.com/atom.xml
  - `html-listing` → `empty` — https://corporate.mattel.com/
  - `robots` → `ok` — https://corporate.mattel.com/robots.txt
  - `sitemap` → `ok` — https://corporate.mattel.com/sitemap.xml

### Metacore (`metacoregames-com`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `8924 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `9`

  - `homepage` → `ok` — https://metacoregames.com/
  - `feed-common` → `error` — https://metacoregames.com/feed — HTTPError: 404 Client Error: Not Found for url: https://metacoregames.com/feed
  - `feed-common` → `error` — https://metacoregames.com/rss — HTTPError: 404 Client Error: Not Found for url: https://metacoregames.com/rss
  - `feed-common` → `error` — https://metacoregames.com/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://metacoregames.com/rss.xml
  - `feed-common` → `error` — https://metacoregames.com/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://metacoregames.com/feed.xml
  - `feed-common` → `error` — https://metacoregames.com/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://metacoregames.com/atom.xml
  - `html-listing` → `empty` — https://metacoregames.com/
  - `robots` → `ok` — https://metacoregames.com/robots.txt
  - `sitemap` → `ok` — https://metacoregames.com/sitemap.xml

### Mintegral (`mintegral-com`)

- Статус: `warning`
- Категория: `timeout`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `13953 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `9`

  - `homepage` → `ok` — https://mintegral.com/
  - `feed-common` → `error` — https://www.mintegral.com/en/feed — HTTPError: 404 Client Error: Not Found for url: https://www.mintegral.com/en/feed
  - `feed-common` → `error` — https://www.mintegral.com/en/rss — HTTPError: 404 Client Error: Not Found for url: https://www.mintegral.com/en/rss
  - `feed-common` → `error` — https://www.mintegral.com/en/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://www.mintegral.com/en/rss.xml
  - `feed-common` → `error` — https://www.mintegral.com/en/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://www.mintegral.com/en/feed.xml
  - `feed-common` → `error` — https://www.mintegral.com/en/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://www.mintegral.com/en/atom.xml
  - `html-listing` → `empty` — https://www.mintegral.com/en
  - `robots` → `ok` — https://www.mintegral.com/robots.txt
  - `sitemap` → `error` — https://www.mintegral.com/sitemap.xml — ConnectionError: HTTPSConnectionPool(host='www.mintegral.com', port=443): Max retries exceeded with url: /sitemap.xml (Caused by ReadTimeoutError("HTTPSConnectionPool(host='www.mintegral.com', port=443): Read timed out. (read timeout=8)"))

### MobileAction / MAF (`maf-ad`)

- Статус: `warning`
- Категория: `no_recent_articles`
- Метод: `feed`
- Получено кандидатов: `10`
- Принято: `0`
- Причины отбраковки: `{"too_old": 10}`
- Время: `2108 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `2`

  - `homepage` → `ok` — https://maf.ad/
  - `feed-discovered` → `ok` — https://maf.ad/en/feed/

### PreMortem Games (`premortem-games`)

- Статус: `warning`
- Категория: `no_recent_articles`
- Метод: `feed`
- Получено кандидатов: `10`
- Принято: `0`
- Причины отбраковки: `{"too_old": 10}`
- Время: `2241 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `2`

  - `homepage` → `ok` — https://premortem.games/
  - `feed-discovered` → `ok` — https://premortem.games/feed/

### ProGameDev (`progamedev-net`)

- Статус: `warning`
- Категория: `no_recent_articles`
- Метод: `feed`
- Получено кандидатов: `10`
- Принято: `0`
- Причины отбраковки: `{"too_old": 10}`
- Время: `2329 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `2`

  - `homepage` → `ok` — https://progamedev.net/
  - `feed-discovered` → `ok` — https://progamedev.net/feed/

### QubicGames (`qubicgames-com`)

- Статус: `warning`
- Категория: `no_recent_articles`
- Метод: `feed-common`
- Получено кандидатов: `9`
- Принято: `0`
- Причины отбраковки: `{"too_old": 9}`
- Время: `5341 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `2`

  - `homepage` → `ok` — https://qubicgames.com/
  - `feed-common` → `ok` — https://qubicgames.com/feed

### SayGames (`say-games`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `8180 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `9`

  - `homepage` → `ok` — https://say.games/
  - `feed-common` → `error` — https://say.games/feed — HTTPError: 404 Client Error: Not Found for url: https://say.games/feed
  - `feed-common` → `error` — https://say.games/rss — HTTPError: 404 Client Error: Not Found for url: https://say.games/rss
  - `feed-common` → `error` — https://say.games/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://say.games/rss.xml
  - `feed-common` → `error` — https://say.games/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://say.games/feed.xml
  - `feed-common` → `error` — https://say.games/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://say.games/atom.xml
  - `html-listing` → `empty` — https://say.games/
  - `robots` → `error` — https://say.games/robots.txt — HTTPError: 404 Client Error: Not Found for url: https://say.games/robots.txt
  - `sitemap` → `error` — https://say.games/sitemap.xml — HTTPError: 404 Client Error: Not Found for url: https://say.games/sitemap.xml

### Sensor Tower (`sensortower-com`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `2010 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `15`

  - `homepage` → `ok` — https://sensortower.com/
  - `feed-common` → `error` — https://sensortower.com/feed — HTTPError: 404 Client Error: Not Found for url: https://sensortower.com/feed
  - `feed-common` → `error` — https://sensortower.com/rss — HTTPError: 404 Client Error: Not Found for url: https://sensortower.com/rss
  - `feed-common` → `error` — https://sensortower.com/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://sensortower.com/rss.xml
  - `feed-common` → `error` — https://sensortower.com/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://sensortower.com/feed.xml
  - `feed-common` → `error` — https://sensortower.com/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://sensortower.com/atom.xml
  - `html-listing` → `empty` — https://sensortower.com/
  - `robots` → `ok` — https://sensortower.com/robots.txt
  - `sitemap` → `ok` — https://sensortower.com/sitemap.xml
  - `sitemap-child` → `ok` — https://sensortower.com/en-US-s3-blog-sitemap-1.xml
  - `sitemap-child` → `ok` — https://sensortower.com/en-US-s3-blog-sitemap-2.xml
  - `sitemap-child` → `ok` — https://sensortower.com/en-US-s3-blog-sitemap-3.xml
  - `sitemap-child` → `ok` — https://sensortower.com/en-US-s3-blog-sitemap-4.xml
  - `sitemap-child` → `ok` — https://sensortower.com/en-US-s3-blog-sitemap-5.xml
  - `sitemap-child` → `ok` — https://sensortower.com/en-US-s3-blog-sitemap-6.xml

### Sensor Tower Resources (`go-sensortower-com`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `3946 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `15`

  - `homepage` → `ok` — https://go.sensortower.com/
  - `feed-common` → `error` — https://sensortower.com/feed — HTTPError: 404 Client Error: Not Found for url: https://sensortower.com/feed
  - `feed-common` → `error` — https://sensortower.com/rss — HTTPError: 404 Client Error: Not Found for url: https://sensortower.com/rss
  - `feed-common` → `error` — https://sensortower.com/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://sensortower.com/rss.xml
  - `feed-common` → `error` — https://sensortower.com/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://sensortower.com/feed.xml
  - `feed-common` → `error` — https://sensortower.com/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://sensortower.com/atom.xml
  - `html-listing` → `empty` — https://sensortower.com
  - `robots` → `ok` — https://sensortower.com/robots.txt
  - `sitemap` → `ok` — https://sensortower.com/sitemap.xml
  - `sitemap-child` → `ok` — https://sensortower.com/en-US-s3-blog-sitemap-1.xml
  - `sitemap-child` → `ok` — https://sensortower.com/en-US-s3-blog-sitemap-2.xml
  - `sitemap-child` → `ok` — https://sensortower.com/en-US-s3-blog-sitemap-3.xml
  - `sitemap-child` → `ok` — https://sensortower.com/en-US-s3-blog-sitemap-4.xml
  - `sitemap-child` → `ok` — https://sensortower.com/en-US-s3-blog-sitemap-5.xml
  - `sitemap-child` → `ok` — https://sensortower.com/en-US-s3-blog-sitemap-6.xml

### Supersonic / Unity LevelPlay (`supersonic-com`)

- Статус: `warning`
- Категория: `no_recent_articles`
- Метод: `feed`
- Получено кандидатов: `10`
- Принято: `0`
- Причины отбраковки: `{"too_old": 10}`
- Время: `1999 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `2`

  - `homepage` → `ok` — https://supersonic.com/
  - `feed-discovered` → `ok` — https://supersonic.com/feed/

### TapNation Blog (`tap-nation-io`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `2288 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `9`

  - `homepage` → `ok` — https://tap-nation.io/
  - `feed-common` → `error` — https://tap-nation.io/feed — HTTPError: 404 Client Error: Not Found for url: https://tap-nation.io/feed
  - `feed-common` → `error` — https://tap-nation.io/rss — HTTPError: 404 Client Error: Not Found for url: https://tap-nation.io/rss
  - `feed-common` → `error` — https://tap-nation.io/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://tap-nation.io/rss.xml
  - `feed-common` → `error` — https://tap-nation.io/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://tap-nation.io/feed.xml
  - `feed-common` → `error` — https://tap-nation.io/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://tap-nation.io/atom.xml
  - `html-listing` → `empty` — https://tap-nation.io/
  - `robots` → `ok` — https://tap-nation.io/robots.txt
  - `sitemap` → `ok` — https://www.tap-nation.io/sitemap.xml

### TechBriefly (`techbriefly-com`)

- Статус: `warning`
- Категория: `blocked`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `447 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `8`

  - `homepage` → `error` — https://techbriefly.com/ — HTTPError: 403 Client Error: Forbidden for url: https://techbriefly.com/
  - `feed-common` → `error` — https://techbriefly.com/feed — HTTPError: 403 Client Error: Forbidden for url: https://techbriefly.com/feed
  - `feed-common` → `error` — https://techbriefly.com/rss — HTTPError: 403 Client Error: Forbidden for url: https://techbriefly.com/rss
  - `feed-common` → `error` — https://techbriefly.com/rss.xml — HTTPError: 403 Client Error: Forbidden for url: https://techbriefly.com/rss.xml
  - `feed-common` → `error` — https://techbriefly.com/feed.xml — HTTPError: 403 Client Error: Forbidden for url: https://techbriefly.com/feed.xml
  - `feed-common` → `error` — https://techbriefly.com/atom.xml — HTTPError: 403 Client Error: Forbidden for url: https://techbriefly.com/atom.xml
  - `robots` → `error` — https://techbriefly.com/robots.txt — HTTPError: 403 Client Error: Forbidden for url: https://techbriefly.com/robots.txt
  - `sitemap` → `error` — https://techbriefly.com/sitemap.xml — HTTPError: 403 Client Error: Forbidden for url: https://techbriefly.com/sitemap.xml

### Tenjin (`tenjin-com`)

- Статус: `warning`
- Категория: `no_recent_articles`
- Метод: `feed`
- Получено кандидатов: `10`
- Принято: `0`
- Причины отбраковки: `{"too_old": 10}`
- Время: `2416 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `2`

  - `homepage` → `ok` — https://tenjin.com/
  - `feed-discovered` → `ok` — https://tenjin.com/feed/

### Tenjin Blog (`blog-tenjin-com`)

- Статус: `warning`
- Категория: `no_recent_articles`
- Метод: `feed`
- Получено кандидатов: `10`
- Принято: `0`
- Причины отбраковки: `{"too_old": 10}`
- Время: `3745 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `2`

  - `homepage` → `ok` — https://blog.tenjin.com/
  - `feed-discovered` → `ok` — https://tenjin.com/feed/

### Tenjin Resources (`resources-tenjin-com`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `1854 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `8`

  - `homepage` → `error` — https://resources.tenjin.com/ — HTTPError: 404 Client Error: Not Found for url: https://resources.tenjin.com/
  - `feed-common` → `error` — https://resources.tenjin.com/feed — HTTPError: 404 Client Error: Not Found for url: https://resources.tenjin.com/feed
  - `feed-common` → `error` — https://resources.tenjin.com/rss — HTTPError: 404 Client Error: Not Found for url: https://resources.tenjin.com/rss
  - `feed-common` → `error` — https://resources.tenjin.com/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://resources.tenjin.com/rss.xml
  - `feed-common` → `error` — https://resources.tenjin.com/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://resources.tenjin.com/feed.xml
  - `feed-common` → `error` — https://resources.tenjin.com/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://resources.tenjin.com/atom.xml
  - `robots` → `ok` — https://resources.tenjin.com/robots.txt
  - `sitemap` → `empty` — https://resources.tenjin.com/sitemap.xml

### Torick (`torick-ru`)

- Статус: `warning`
- Категория: `no_recent_articles`
- Метод: `feed`
- Получено кандидатов: `20`
- Принято: `0`
- Причины отбраковки: `{"too_old": 20}`
- Время: `1351 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `2`

  - `homepage` → `ok` — https://torick.ru/
  - `feed-discovered` → `ok` — https://torick.ru/feed/

### Unity (`unity-com`)

- Статус: `warning`
- Категория: `timeout`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `65293 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `8`

  - `homepage` → `error` — https://unity.com/ — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: / (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `feed-common` → `error` — https://unity.com/feed — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /feed (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `feed-common` → `error` — https://unity.com/rss — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /rss (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `feed-common` → `error` — https://unity.com/rss.xml — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /rss.xml (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `feed-common` → `error` — https://unity.com/feed.xml — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /feed.xml (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `feed-common` → `error` — https://unity.com/atom.xml — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /atom.xml (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `robots` → `error` — https://unity.com/robots.txt — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /robots.txt (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `sitemap` → `error` — https://unity.com/sitemap.xml — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /sitemap.xml (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))

### Unity Blog (`blog-unity-com`)

- Статус: `warning`
- Категория: `timeout`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `65449 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `8`

  - `homepage` → `error` — https://blog.unity.com/ — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /blog/ (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `feed-common` → `error` — https://blog.unity.com/feed — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /blog/feed (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `feed-common` → `error` — https://blog.unity.com/rss — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /blog/rss (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `feed-common` → `error` — https://blog.unity.com/rss.xml — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /blog/rss.xml (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `feed-common` → `error` — https://blog.unity.com/feed.xml — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /blog/feed.xml (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `feed-common` → `error` — https://blog.unity.com/atom.xml — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /blog/atom.xml (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `robots` → `error` — https://blog.unity.com/robots.txt — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /blog/robots.txt (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))
  - `sitemap` → `error` — https://blog.unity.com/sitemap.xml — ConnectionError: HTTPSConnectionPool(host='unity.com', port=443): Max retries exceeded with url: /blog/sitemap.xml (Caused by ReadTimeoutError("HTTPSConnectionPool(host='unity.com', port=443): Read timed out. (read timeout=8)"))

### VK Play Медиа (`vkplay-ru`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `9081 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `21`

  - `homepage` → `ok` — https://vkplay.ru/
  - `feed-common` → `empty` — https://vkplay.ru/feed
  - `feed-common` → `empty` — https://vkplay.ru/rss
  - `feed-common` → `empty` — https://vkplay.ru/rss.xml
  - `feed-common` → `empty` — https://vkplay.ru/feed.xml
  - `feed-common` → `empty` — https://vkplay.ru/atom.xml
  - `html-listing` → `empty` — https://vkplay.ru/
  - `robots` → `ok` — https://vkplay.ru/robots.txt
  - `sitemap` → `ok` — https://vkplay.ru/sitemap.xml
  - `sitemap-child` → `ok` — https://vkplay.ru/sitemap/sitemap.0.xml
  - `sitemap-child` → `ok` — https://vkplay.ru/sitemap/sitemap.1.xml
  - `sitemap-child` → `ok` — https://vkplay.ru/sitemap/sitemap.extra.xml
  - `sitemap-child` → `ok` — https://vkplay.ru/sitemap/sitemap.tags.xml
  - `sitemap` → `ok` — https://vkplay.ru/sitemap/sitemap.static.xml
  - `sitemap` → `ok` — https://vkplay.ru/sitemap/sitemap.media.xml
  - `sitemap-child` → `ok` — https://vkplay.ru/sitemap/sitemap.news.0.xml
  - `sitemap-child` → `ok` — https://vkplay.ru/sitemap/sitemap.news.1.xml
  - `sitemap-child` → `ok` — https://vkplay.ru/sitemap/sitemap.news.2.xml
  - `sitemap-child` → `ok` — https://vkplay.ru/sitemap/sitemap.news.latest.0.xml
  - `sitemap-child` → `ok` — https://vkplay.ru/sitemap/sitemap.articles.0.xml
  - `sitemap-child` → `ok` — https://vkplay.ru/sitemap/sitemap.media.games.0.xml

### Voodoo (`voodoo-io`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `493 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `9`

  - `homepage` → `ok` — https://voodoo.io/
  - `feed-common` → `error` — https://voodoo.io/feed — HTTPError: 404 Client Error: Not Found for url: https://voodoo.io/feed
  - `feed-common` → `error` — https://voodoo.io/rss — HTTPError: 404 Client Error: Not Found for url: https://voodoo.io/rss
  - `feed-common` → `error` — https://voodoo.io/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://voodoo.io/rss.xml
  - `feed-common` → `error` — https://voodoo.io/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://voodoo.io/feed.xml
  - `feed-common` → `error` — https://voodoo.io/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://voodoo.io/atom.xml
  - `html-listing` → `empty` — https://voodoo.io/
  - `robots` → `ok` — https://voodoo.io/robots.txt
  - `sitemap` → `ok` — https://voodoo.io/sitemap.xml

### Voodoo Blog (`blog-voodoo-io`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `496 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `9`

  - `homepage` → `ok` — https://blog.voodoo.io/
  - `feed-common` → `error` — https://voodoo.io/news/feed — HTTPError: 404 Client Error: Not Found for url: https://voodoo.io/news/feed
  - `feed-common` → `error` — https://voodoo.io/news/rss — HTTPError: 404 Client Error: Not Found for url: https://voodoo.io/news/rss
  - `feed-common` → `error` — https://voodoo.io/news/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://voodoo.io/news/rss.xml
  - `feed-common` → `error` — https://voodoo.io/news/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://voodoo.io/news/feed.xml
  - `feed-common` → `error` — https://voodoo.io/news/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://voodoo.io/news/atom.xml
  - `html-listing` → `empty` — https://voodoo.io/news
  - `robots` → `ok` — https://voodoo.io/robots.txt
  - `sitemap` → `ok` — https://voodoo.io/sitemap.xml

### Xsolla (`xsolla-com`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `4959 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `15`

  - `homepage` → `ok` — https://xsolla.com/
  - `feed-common` → `error` — https://xsolla.com/feed — HTTPError: 404 Client Error: Not Found for url: https://xsolla.com/feed
  - `feed-common` → `error` — https://xsolla.com/rss — HTTPError: 404 Client Error: Not Found for url: https://xsolla.com/rss
  - `feed-common` → `error` — https://xsolla.com/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://xsolla.com/rss.xml
  - `feed-common` → `error` — https://xsolla.com/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://xsolla.com/feed.xml
  - `feed-common` → `error` — https://xsolla.com/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://xsolla.com/atom.xml
  - `html-listing` → `empty` — https://xsolla.com/
  - `robots` → `ok` — https://xsolla.com/robots.txt
  - `sitemap` → `ok` — https://xsolla.com/sitemap.xml
  - `sitemap-child` → `ok` — https://xsolla.com/sitemap/developers.xml
  - `sitemap-child` → `ok` — https://help.xsolla.com/sitemap.xml
  - `sitemap-child` → `ok` — https://xsolla.com/sitemap/others.xml
  - `sitemap-child` → `ok` — https://xsolla.com/sitemap/pages.xml
  - `sitemap-child` → `ok` — https://xsolla.com/sitemap/pages2.xml
  - `sitemap-child` → `ok` — https://xsolla.com/sitemap/pages.xml

### Xsolla RU (`xsolla-ru`)

- Статус: `warning`
- Категория: `no_articles_found`
- Метод: `none`
- Получено кандидатов: `0`
- Принято: `0`
- Причины отбраковки: `{}`
- Время: `1759 ms`
- Ошибка: `No accepted recent dated articles`
- Попыток: `9`

  - `homepage` → `ok` — https://xsolla.ru/
  - `feed-common` → `error` — https://ru.xsolla.com/feed — HTTPError: 404 Client Error: Not Found for url: https://ru.xsolla.com/feed
  - `feed-common` → `error` — https://ru.xsolla.com/rss — HTTPError: 404 Client Error: Not Found for url: https://ru.xsolla.com/rss
  - `feed-common` → `error` — https://ru.xsolla.com/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://ru.xsolla.com/rss.xml
  - `feed-common` → `error` — https://ru.xsolla.com/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://ru.xsolla.com/feed.xml
  - `feed-common` → `error` — https://ru.xsolla.com/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://ru.xsolla.com/atom.xml
  - `html-listing` → `empty` — https://ru.xsolla.com/
  - `robots` → `ok` — https://ru.xsolla.com/robots.txt
  - `sitemap` → `ok` — https://ru.xsolla.com/sitemap.xml
