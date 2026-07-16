# Диагностика источников

Обновлено: `2026-07-16T07:01:01Z`

## Сводка

- `no_recent_articles`: **26**
- `unknown`: **14**
- `blocked`: **7**

## Проблемные источники

### AppMetrica (`appmetrica-yandex-ru`)

- Статус: `warning`
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `6032 ms`
- Ошибка: `No recent dated articles found`
- Попыток: `10`

  - `homepage` → `ok` — https://appmetrica.yandex.ru/
  - `feed-common` → `error` — https://appmetrica.yandex.ru/about/feed — HTTPError: 404 Client Error: Not Found for url: https://appmetrica.yandex.ru/about/feed
  - `feed-common` → `error` — https://appmetrica.yandex.ru/about/rss — HTTPError: 404 Client Error: Not Found for url: https://appmetrica.yandex.ru/about/rss
  - `feed-common` → `error` — https://appmetrica.yandex.ru/about/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://appmetrica.yandex.ru/about/rss.xml
  - `feed-common` → `error` — https://appmetrica.yandex.ru/about/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://appmetrica.yandex.ru/about/feed.xml
  - `feed-common` → `error` — https://appmetrica.yandex.ru/about/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://appmetrica.yandex.ru/about/atom.xml
  - `html-listing` → `empty` — https://appmetrica.yandex.ru/about
  - `robots` → `ok` — https://appmetrica.yandex.ru/robots.txt
  - `sitemap` → `error` — https://appmetrica.yandex.ru/docs/sitemap.xml — HTTPError: 404 Client Error: Not Found for url: https://appmetrica.yandex.ru/docs/ru/sitemap.xml
  - `sitemap` → `ok` — https://appmetrica.yandex.ru/sitemap.xml

### AppMetrica (`appmetrica-yandex-com`)

- Статус: `warning`
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `16473 ms`
- Ошибка: `No recent dated articles found`
- Попыток: `9`

  - `homepage` → `ok` — https://appmetrica.yandex.com/
  - `feed-common` → `empty` — https://passport.yandex.com/feed
  - `feed-common` → `empty` — https://passport.yandex.com/rss
  - `feed-common` → `empty` — https://passport.yandex.com/rss.xml
  - `feed-common` → `empty` — https://passport.yandex.com/feed.xml
  - `feed-common` → `empty` — https://passport.yandex.com/atom.xml
  - `html-listing` → `empty` — https://passport.yandex.com/pwl-yandex?retpath=https%3A%2F%2Fappmetrica.yandex.com%2Foverview&lang=en&cause=auth&process_uuid=ac0f1ffb-97d9-40dd-bcdc-1f4a1e43aa07
  - `robots` → `ok` — https://passport.yandex.com/robots.txt
  - `sitemap` → `error` — https://passport.yandex.com/sitemap.xml — ParseError: not well-formed (invalid token): line 13, column 14

### Appodeal (`appodeal-com`)

- Статус: `warning`
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `8192 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `2211 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `blocked`
- Метод: `none`
- Время: `1624 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `5691 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `unknown`
- Метод: `feed-common`
- Время: `2031 ms`
- Ошибка: `No recent dated articles found`
- Попыток: `2`

  - `homepage` → `ok` — https://azurgames.com/
  - `feed-common` → `ok` — https://azurgames.com/feed

### BlockchainGamer.biz (`blockchaingamer-biz`)

- Статус: `warning`
- Категория ошибки: `blocked`
- Метод: `none`
- Время: `589 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `blocked`
- Метод: `none`
- Время: `249 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `unknown`
- Метод: `feed`
- Время: `337 ms`
- Ошибка: `No recent dated articles found`
- Попыток: `2`

  - `homepage` → `ok` — https://crazylabs.com/
  - `feed-discovered` → `ok` — https://www.crazylabs.com/feed/

### CTech (`calcalistech-com`)

- Статус: `warning`
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `5530 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `37300 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `no_recent_articles`
- Метод: `sitemap`
- Время: `2130 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `2393 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `blocked`
- Метод: `none`
- Время: `328 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `1032 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `blocked`
- Метод: `none`
- Время: `106 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `573 ms`
- Ошибка: `No recent dated articles found`
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

### Kwalee Blog (`kwalee-com`)

- Статус: `warning`
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `2723 ms`
- Ошибка: `No recent dated articles found`
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

### Kwalee Press (`press-kwalee-com`)

- Статус: `warning`
- Категория ошибки: `unknown`
- Метод: `none`
- Время: `1818 ms`
- Ошибка: `No recent dated articles found`
- Попыток: `8`

  - `homepage` → `error` — https://press.kwalee.com/ — HTTPError: 404 Client Error: Not Found for url: https://press.kwalee.com/
  - `feed-common` → `error` — https://press.kwalee.com/feed — HTTPError: 404 Client Error: Not Found for url: https://press.kwalee.com/feed
  - `feed-common` → `error` — https://press.kwalee.com/rss — HTTPError: 404 Client Error: Not Found for url: https://press.kwalee.com/rss
  - `feed-common` → `error` — https://press.kwalee.com/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://press.kwalee.com/rss.xml
  - `feed-common` → `error` — https://press.kwalee.com/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://press.kwalee.com/feed.xml
  - `feed-common` → `error` — https://press.kwalee.com/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://press.kwalee.com/atom.xml
  - `robots` → `ok` — https://press.kwalee.com/robots.txt
  - `sitemap` → `error` — https://press.kwalee.com/sitemap.xml — HTTPError: 404 Client Error: Not Found for url: https://press.kwalee.com/sitemap.xml

### Liftoff Content (`content-liftoff-io`)

- Статус: `warning`
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `1342 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `unknown`
- Метод: `feed`
- Время: `3215 ms`
- Ошибка: `No recent dated articles found`
- Попыток: `2`

  - `homepage` → `ok` — https://blog.liquidandgrit.com/
  - `feed-discovered` → `ok` — https://blog.liquidandgrit.com/feed

### Matej Lancaric Substack (`lancaric-substack-com`)

- Статус: `warning`
- Категория ошибки: `blocked`
- Метод: `none`
- Время: `562 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `3358 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `10111 ms`
- Ошибка: `No recent dated articles found`
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

### MobileAction / MAF (`maf-ad`)

- Статус: `warning`
- Категория ошибки: `unknown`
- Метод: `feed`
- Время: `1996 ms`
- Ошибка: `No recent dated articles found`
- Попыток: `2`

  - `homepage` → `ok` — https://maf.ad/
  - `feed-discovered` → `ok` — https://maf.ad/en/feed/

### Playliner (`playliner-com`)

- Статус: `warning`
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `3663 ms`
- Ошибка: `No recent dated articles found`
- Попыток: `15`

  - `homepage` → `ok` — https://playliner.com/
  - `feed-common` → `error` — https://sensortower.com:443/product/live-ops/feed — HTTPError: 404 Client Error: Not Found for url: https://sensortower.com:443/product/live-ops/feed
  - `feed-common` → `error` — https://sensortower.com:443/product/live-ops/rss — HTTPError: 404 Client Error: Not Found for url: https://sensortower.com:443/product/live-ops/rss
  - `feed-common` → `error` — https://sensortower.com:443/product/live-ops/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://sensortower.com:443/product/live-ops/rss.xml
  - `feed-common` → `error` — https://sensortower.com:443/product/live-ops/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://sensortower.com:443/product/live-ops/feed.xml
  - `feed-common` → `error` — https://sensortower.com:443/product/live-ops/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://sensortower.com:443/product/live-ops/atom.xml
  - `html-listing` → `empty` — https://sensortower.com:443/product/live-ops
  - `robots` → `ok` — https://sensortower.com:443/robots.txt
  - `sitemap` → `ok` — https://sensortower.com:443/sitemap.xml
  - `sitemap-child` → `ok` — https://sensortower.com/en-US-s3-blog-sitemap-1.xml
  - `sitemap-child` → `ok` — https://sensortower.com/en-US-s3-blog-sitemap-2.xml
  - `sitemap-child` → `ok` — https://sensortower.com/en-US-s3-blog-sitemap-3.xml
  - `sitemap-child` → `ok` — https://sensortower.com/en-US-s3-blog-sitemap-4.xml
  - `sitemap-child` → `ok` — https://sensortower.com/en-US-s3-blog-sitemap-5.xml
  - `sitemap-child` → `ok` — https://sensortower.com/en-US-s3-blog-sitemap-6.xml

### PreMortem Games (`premortem-games`)

- Статус: `warning`
- Категория ошибки: `unknown`
- Метод: `feed`
- Время: `2219 ms`
- Ошибка: `No recent dated articles found`
- Попыток: `2`

  - `homepage` → `ok` — https://premortem.games/
  - `feed-discovered` → `ok` — https://premortem.games/feed/

### ProGameDev (`progamedev-net`)

- Статус: `warning`
- Категория ошибки: `unknown`
- Метод: `feed`
- Время: `2663 ms`
- Ошибка: `No recent dated articles found`
- Попыток: `2`

  - `homepage` → `ok` — https://progamedev.net/
  - `feed-discovered` → `ok` — https://progamedev.net/feed/

### QubicGames (`qubicgames-com`)

- Статус: `warning`
- Категория ошибки: `unknown`
- Метод: `feed-common`
- Время: `7264 ms`
- Ошибка: `No recent dated articles found`
- Попыток: `2`

  - `homepage` → `ok` — https://qubicgames.com/
  - `feed-common` → `ok` — https://qubicgames.com/feed

### SayGames (`say-games`)

- Статус: `warning`
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `7878 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `1307 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `2334 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `unknown`
- Метод: `feed`
- Время: `2004 ms`
- Ошибка: `No recent dated articles found`
- Попыток: `2`

  - `homepage` → `ok` — https://supersonic.com/
  - `feed-discovered` → `ok` — https://supersonic.com/feed/

### TapNation Blog (`tap-nation-io`)

- Статус: `warning`
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `2700 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `blocked`
- Метод: `none`
- Время: `373 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `unknown`
- Метод: `feed`
- Время: `1674 ms`
- Ошибка: `No recent dated articles found`
- Попыток: `2`

  - `homepage` → `ok` — https://tenjin.com/
  - `feed-discovered` → `ok` — https://tenjin.com/feed/

### Tenjin Blog (`blog-tenjin-com`)

- Статус: `warning`
- Категория ошибки: `unknown`
- Метод: `feed`
- Время: `1763 ms`
- Ошибка: `No recent dated articles found`
- Попыток: `2`

  - `homepage` → `ok` — https://blog.tenjin.com/
  - `feed-discovered` → `ok` — https://tenjin.com/feed/

### Tenjin Resources (`resources-tenjin-com`)

- Статус: `warning`
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `836 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `unknown`
- Метод: `feed`
- Время: `1439 ms`
- Ошибка: `No recent dated articles found`
- Попыток: `2`

  - `homepage` → `ok` — https://torick.ru/
  - `feed-discovered` → `ok` — https://torick.ru/feed/

### Unity Blog (`blog-unity-com`)

- Статус: `warning`
- Категория ошибки: `unknown`
- Метод: `feed-common`
- Время: `39037 ms`
- Ошибка: `No recent dated articles found`
- Попыток: `2`

  - `homepage` → `ok` — https://blog.unity.com/
  - `feed-common` → `ok` — https://unity.com/blog/feed

### VK Play Медиа (`vkplay-ru`)

- Статус: `warning`
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `9261 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `852 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `767 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `3776 ms`
- Ошибка: `No recent dated articles found`
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
- Категория ошибки: `no_recent_articles`
- Метод: `none`
- Время: `1913 ms`
- Ошибка: `No recent dated articles found`
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

### РБК (`rbc-ru`)

- Статус: `warning`
- Категория ошибки: `unknown`
- Метод: `none`
- Время: `10850 ms`
- Ошибка: `No recent dated articles found`
- Попыток: `26`

  - `homepage` → `error` — https://rbc.ru/ — HTTPError: 401 Client Error: Unauthorized for url: https://www.rbc.ru/8c1a1713-f82e-4b8a-97a4-6a2f1cfa20a2/
  - `feed-common` → `error` — https://rbc.ru/feed — HTTPError: 401 Client Error: Unauthorized for url: https://www.rbc.ru/feed
  - `feed-common` → `error` — https://rbc.ru/rss — HTTPError: 401 Client Error: Unauthorized for url: https://www.rbc.ru/rss
  - `feed-common` → `error` — https://rbc.ru/rss.xml — HTTPError: 404 Client Error: Not Found for url: https://www.rbc.ru/rss.xml
  - `feed-common` → `error` — https://rbc.ru/feed.xml — HTTPError: 404 Client Error: Not Found for url: https://www.rbc.ru/feed.xml
  - `feed-common` → `error` — https://rbc.ru/atom.xml — HTTPError: 404 Client Error: Not Found for url: https://www.rbc.ru/atom.xml
  - `robots` → `ok` — https://rbc.ru/robots.txt
  - `sitemap` → `ok` — https://www.rbc.ru/sitemap_index.xml
  - `sitemap-child` → `ok` — https://www.rbc.ru/sitemap_979.xml
  - `sitemap-child` → `ok` — https://www.rbc.ru/sitemap_889.xml
  - `sitemap-child` → `ok` — https://www.rbc.ru/sitemap_692.xml
  - `sitemap-child` → `ok` — https://www.rbc.ru/sitemap_854.xml
  - `sitemap-child` → `ok` — https://www.rbc.ru/sitemap_945.xml
  - `sitemap-child` → `ok` — https://www.rbc.ru/sitemap_590.xml
  - `article-enrich` → `error` — https://www.rbc.ru/sport/16/07/2026/6a57d14e9a79470d72a134f8 — HTTPError: 401 Client Error: Unauthorized for url: https://www.rbc.ru/sport/16/07/2026/6a57d14e9a79470d72a134f8
  - `article-enrich` → `error` — https://www.rbc.ru/rbcfreenews/6a58048f9a7947ee016e8631 — HTTPError: 401 Client Error: Unauthorized for url: https://www.rbc.ru/rbcfreenews/6a58048f9a7947ee016e8631
  - `article-enrich` → `error` — https://www.rbc.ru/story/worldcup2026 — HTTPError: 401 Client Error: Unauthorized for url: https://www.rbc.ru/story/worldcup2026
  - `article-enrich` → `error` — https://www.rbc.ru/sport/16/07/2026/6a57f8909a7947328f2edf4d — HTTPError: 401 Client Error: Unauthorized for url: https://www.rbc.ru/sport/16/07/2026/6a57f8909a7947328f2edf4d
  - `article-enrich` → `error` — https://www.rbc.ru/story/61ee7c0f9a7947051824f535 — HTTPError: 401 Client Error: Unauthorized for url: https://www.rbc.ru/story/61ee7c0f9a7947051824f535
  - `article-enrich` → `error` — https://www.rbc.ru/story/6734a0de9a7947d05d2e8128 — HTTPError: 401 Client Error: Unauthorized for url: https://www.rbc.ru/story/6734a0de9a7947d05d2e8128
  - `article-enrich` → `error` — https://www.rbc.ru/politics/16/07/2026/6a5860709a7947dc9f438f77 — HTTPError: 401 Client Error: Unauthorized for url: https://www.rbc.ru/politics/16/07/2026/6a5860709a7947dc9f438f77
  - `article-enrich` → `error` — https://www.rbc.ru/story/69a29bdb9a7947d25744d371 — HTTPError: 401 Client Error: Unauthorized for url: https://www.rbc.ru/story/69a29bdb9a7947d25744d371
  - `article-enrich` → `error` — https://www.rbc.ru/politics/16/07/2026/6a587db09a7947b5470223e0 — HTTPError: 401 Client Error: Unauthorized for url: https://www.rbc.ru/politics/16/07/2026/6a587db09a7947b5470223e0
  - `article-enrich` → `error` — https://www.rbc.ru/politics/16/07/2026/6a587cce9a794742b5b46605 — HTTPError: 401 Client Error: Unauthorized for url: https://www.rbc.ru/politics/16/07/2026/6a587cce9a794742b5b46605
  - `article-enrich` → `error` — https://www.rbc.ru/politics/16/07/2026/6a5874df9a794782edfd5494 — HTTPError: 401 Client Error: Unauthorized for url: https://www.rbc.ru/politics/16/07/2026/6a5874df9a794782edfd5494
  - `article-enrich` → `error` — https://www.rbc.ru/rbcfreenews/6a5872649a79476695a52f56 — HTTPError: 401 Client Error: Unauthorized for url: https://www.rbc.ru/rbcfreenews/6a5872649a79476695a52f56
