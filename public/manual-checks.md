# Что желательно проверить вручную

Обновлено: `2026-07-16T07:40:34Z`

Источники с обычным статусом `no_recent_articles` сюда не включаются: они технически исправны, но не публиковались в текущем окне.

## dev.by (`dev-by`)

- Приоритет: **high**
- Причина: `redirected_to_other_domain`
- Проверить: https://dev.by/
- Действие: Открыть источник и подтвердить, что редирект на devby.io ожидаем. Если бренд поглощён или закрыт — удалить либо объединить источник.
- Отбраковка: `{}`

## Liftoff (`liftoff-io`)

- Приоритет: **high**
- Причина: `redirected_to_other_domain`
- Проверить: https://liftoff.io/
- Действие: Открыть источник и подтвердить, что редирект на liftoff.ai ожидаем. Если бренд поглощён или закрыт — удалить либо объединить источник.
- Отбраковка: `{"too_old": 8}`

## Sensor Tower Resources (`go-sensortower-com`)

- Приоритет: **high**
- Причина: `redirected_to_other_domain`
- Проверить: https://go.sensortower.com/
- Действие: Открыть источник и подтвердить, что редирект на sensortower.com ожидаем. Если бренд поглощён или закрыт — удалить либо объединить источник.
- Отбраковка: `{}`

## Voodoo Blog (`blog-voodoo-io`)

- Приоритет: **high**
- Причина: `redirected_to_other_domain`
- Проверить: https://blog.voodoo.io/
- Действие: Открыть источник и подтвердить, что редирект на voodoo.io ожидаем. Если бренд поглощён или закрыт — удалить либо объединить источник.
- Отбраковка: `{}`

## Xsolla RU (`xsolla-ru`)

- Приоритет: **high**
- Причина: `redirected_to_other_domain`
- Проверить: https://xsolla.ru/
- Действие: Открыть источник и подтвердить, что редирект на ru.xsolla.com ожидаем. Если бренд поглощён или закрыт — удалить либо объединить источник.
- Отбраковка: `{}`

## 80 Level (`80-lv`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://80.lv/feed
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{}`

## App Developer Magazine (`appdevelopermagazine-com`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://appdevelopermagazine.com/RSS/
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{"too_old": 45}`

## App2Top (`app2top-ru`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://app2top.ru/feed
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{"too_old": 9}`

## Appfigures (`appfigures-com`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://appfigures.com/sitemap.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{}`

## AppMagic Blog (`appmagic-rocks`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://appmagic.rocks/sitemap.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{}`

## Appodeal (`appodeal-com`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://appodeal.com/sitemap_index.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{}`

## AppQuantum Hybrid Casual (`hybridcasual-appquantum-com`)

- Приоритет: **medium**
- Причина: `blocked_on_github_runner`
- Проверить: https://hybridcasual.appquantum.com/
- Действие: Проверить URL в обычном браузере. Если открывается, найти официальный RSS или подтвердить необходимость внешнего RSS-прокси.
- Отбраковка: `{}`

## AppsFlyer (`appsflyer-com`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://www.appsflyer.com:443/feed
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{"too_old": 9}`

## Apptica (`apptica-com`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://apptica.com/sitemap.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{}`

## BlockchainGamer.biz (`blockchaingamer-biz`)

- Приоритет: **medium**
- Причина: `blocked_on_github_runner`
- Проверить: https://blockchaingamer.biz/
- Действие: Проверить URL в обычном браузере. Если открывается, найти официальный RSS или подтвердить необходимость внешнего RSS-прокси.
- Отбраковка: `{}`

## Business of Apps (`businessofapps-com`)

- Приоритет: **medium**
- Причина: `blocked_on_github_runner`
- Проверить: https://businessofapps.com/
- Действие: Проверить URL в обычном браузере. Если открывается, найти официальный RSS или подтвердить необходимость внешнего RSS-прокси.
- Отбраковка: `{}`

## citybiz (`citybiz-co`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://www.citybiz.co/feed/
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{}`

## data.ai (`data-ai`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://www.data.ai/cn/sitemap.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{}`

## Deconstructor of Fun (`deconstructoroffun-com`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://www.deconstructoroffun.com/sitemap.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{"too_old": 1}`

## dev.by / devby.io (`devby-io`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://devby.io/rss
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{}`

## DTF (`dtf-ru`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://dtf.ru/rss
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{}`

## Ducky (`playducky-com`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://playducky.com/sitemap.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{}`

## Elite Game Developers (`elitegamedevelopers-substack-com`)

- Приоритет: **medium**
- Причина: `blocked_on_github_runner`
- Проверить: https://elitegamedevelopers.substack.com/
- Действие: Проверить URL в обычном браузере. Если открывается, найти официальный RSS или подтвердить необходимость внешнего RSS-прокси.
- Отбраковка: `{}`

## Game Developer (`gamedeveloper-com`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://www.gamedeveloper.com/rss.xml
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{"too_old": 27}`

## GameAnalytics (`gameanalytics-com`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://www.gameanalytics.com/sitemap.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{}`

## GameDiscoverCo (`newsletter-gamediscover-co`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://newsletter.gamediscover.co/feed
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{"too_old": 19}`

## GameRefinery (`gamerefinery-com`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://www.gamerefinery.com/feed/
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{"too_old": 9}`

## GamesIndustry.biz (`gamesindustry-biz`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://www.gamesindustry.biz/feed
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{"too_old": 23}`

## GamesPress (`gamespress-com`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://www.gamespress.com/en-US/News/RSS
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{}`

## GamingonPhone (`gamingonphone-com`)

- Приоритет: **medium**
- Причина: `blocked_on_github_runner`
- Проверить: https://gamingonphone.com/
- Действие: Проверить URL в обычном браузере. Если открывается, найти официальный RSS или подтвердить необходимость внешнего RSS-прокси.
- Отбраковка: `{}`

## HackerNoon (`hackernoon-com`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://hackernoon.com/feed
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{}`

## How To Market A Game (`howtomarketagame-com`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://howtomarketagame.com/feed/
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{"too_old": 7}`

## Kwalee Blog (`kwalee-com`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://www.kwalee.com/sitemap.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{}`

## Matej Lancaric (`lancaric-me`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://lancaric.me/sitemap_index.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{}`

## Matej Lancaric Substack (`lancaric-substack-com`)

- Приоритет: **medium**
- Причина: `blocked_on_github_runner`
- Проверить: https://lancaric.substack.com/
- Действие: Проверить URL в обычном браузере. Если открывается, найти официальный RSS или подтвердить необходимость внешнего RSS-прокси.
- Отбраковка: `{}`

## Mattel Corporate (`corporate-mattel-com`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://corporate.mattel.com/sitemap.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{}`

## Max Power Gaming (`maxpowergaming-co`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://www.maxpowergaming.co/blog-feed.xml
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{"too_old": 19}`

## Metacore (`metacoregames-com`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://metacoregames.com/sitemap.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{}`

## Mintegral (`mintegral-com`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://www.mintegral.com/sitemap.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{"duplicate_in_source": 1}`

## Mobidictum (`mobidictum-com`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://mobidictum.com/feed/
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{}`

## MobileGamer.biz (`mobilegamer-biz`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://mobilegamer.biz/feed/
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{}`

## Naavik (`naavik-co`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://naavik.co/feed/
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{"too_old": 8}`

## Nintendo (`nintendo-com`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://www.nintendo.com/au/sitemap/0.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{"duplicate_in_source": 1}`

## Onlíner Tech (`tech-onliner-by`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://tech.onliner.by/feed
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{}`

## PC Gamer (`pcgamer-com`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://www.pcgamer.com/feeds.xml
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{}`

## Photon Blog (`blog-photonengine-com`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://blog.photonengine.com/feed/
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{"too_old": 9}`

## Playgama (`wiki-playgama-com`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://wiki.playgama.com/playgama/sitemap.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{}`

## Pocket Gamer (`pocketgamer-com`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://www.pocketgamer.com/index.rss
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{}`

## PocketGamer.biz (`pocketgamer-biz`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://www.pocketgamer.biz/index.rss
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{}`

## RevenueCat (`revenuecat-com`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://www.revenuecat.com/blog/rss.xml
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{"too_old": 47}`

## RO Trends (`rotrends-com`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://rotrends.com/sitemap.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{}`

## Rock Paper Shotgun (`rockpapershotgun-com`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://www.rockpapershotgun.com/feed
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{}`

## Sensor Tower (`sensortower-com`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://sensortower.com/sitemap.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{}`

## Singular (`singular-net`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://www.singular.net/feed/
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{"too_old": 7}`

## Smart Ranking (`smartranking-ru`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://smartranking.ru/sitemap.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{}`

## SocialPeta (`socialpeta-com`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://socialpeta.com/sitemap.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{"duplicate_in_source": 5}`

## TapNation Blog (`tap-nation-io`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://www.tap-nation.io/sitemap.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{}`

## Tech.eu (`tech-eu`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://tech.eu/feed
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{}`

## TechBriefly (`techbriefly-com`)

- Приоритет: **medium**
- Причина: `blocked_on_github_runner`
- Проверить: https://techbriefly.com/
- Действие: Проверить URL в обычном браузере. Если открывается, найти официальный RSS или подтвердить необходимость внешнего RSS-прокси.
- Отбраковка: `{}`

## Udonis Blog (`blog-udonis-co`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://www.blog.udonis.co/rss.xml
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{"too_old": 39}`

## VentureBeat (`venturebeat-com`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://venturebeat.com/feed
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{}`

## VK Play Медиа (`vkplay-ru`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://vkplay.ru/sitemap.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{}`

## Voodoo (`voodoo-io`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://voodoo.io/sitemap.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{}`

## Xsolla (`xsolla-com`)

- Приоритет: **medium**
- Причина: `sitemap_needs_path_filter`
- Проверить: https://xsolla.com/sitemap.xml
- Действие: Открыть sitemap и указать, какой дочерний sitemap или URL-префикс содержит именно новости: /blog/, /news/, /insights/ или другой.
- Отбраковка: `{}`

## Бизнес-секреты (`secrets-tbank-ru`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://secrets.tbank.ru/feeds/rss-feed.rss
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{}`

## Кинжал (`kinzhal-media`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://kinzhal.media/feed/
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{"too_old": 21}`

## Т—Ж (`t-j-ru`)

- Приоритет: **medium**
- Причина: `feed_reachable_but_no_accepted_items`
- Проверить: https://t-j.ru/feed/
- Действие: Проверить первые 3 item: link, pubDate/updated и фактическую дату последней публикации.
- Отбраковка: `{}`

## AppQuantum (`appquantum-com`)

- Приоритет: **low**
- Причина: `source_structure_unknown`
- Проверить: https://appquantum.com/
- Действие: Найти на сайте раздел новостей, официальный RSS или sitemap с публикациями и прислать URL.
- Отбраковка: `{}`

## CTech (`calcalistech-com`)

- Приоритет: **low**
- Причина: `source_structure_unknown`
- Проверить: https://calcalistech.com/
- Действие: Найти на сайте раздел новостей, официальный RSS или sitemap с публикациями и прислать URL.
- Отбраковка: `{}`

## Homa (`homagames-com`)

- Приоритет: **low**
- Причина: `source_structure_unknown`
- Проверить: https://homagames.com/
- Действие: Найти на сайте раздел новостей, официальный RSS или sitemap с публикациями и прислать URL.
- Отбраковка: `{}`

## ironSource (`is-com`)

- Приоритет: **low**
- Причина: `source_structure_unknown`
- Проверить: https://is.com/
- Действие: Найти на сайте раздел новостей, официальный RSS или sitemap с публикациями и прислать URL.
- Отбраковка: `{}`

## Liftoff Content (`content-liftoff-io`)

- Приоритет: **low**
- Причина: `source_structure_unknown`
- Проверить: https://content.liftoff.io/
- Действие: Найти на сайте раздел новостей, официальный RSS или sitemap с публикациями и прислать URL.
- Отбраковка: `{}`

## SayGames (`say-games`)

- Приоритет: **low**
- Причина: `source_structure_unknown`
- Проверить: https://say.games/
- Действие: Найти на сайте раздел новостей, официальный RSS или sitemap с публикациями и прислать URL.
- Отбраковка: `{}`

## Tenjin Resources (`resources-tenjin-com`)

- Приоритет: **low**
- Причина: `source_structure_unknown`
- Проверить: https://resources.tenjin.com/
- Действие: Найти на сайте раздел новостей, официальный RSS или sitemap с публикациями и прислать URL.
- Отбраковка: `{}`

## Unity (`unity-com`)

- Приоритет: **low**
- Причина: `source_structure_unknown`
- Проверить: https://unity.com/
- Действие: Найти на сайте раздел новостей, официальный RSS или sitemap с публикациями и прислать URL.
- Отбраковка: `{}`

## Unity Blog (`blog-unity-com`)

- Приоритет: **low**
- Причина: `source_structure_unknown`
- Проверить: https://blog.unity.com/
- Действие: Найти на сайте раздел новостей, официальный RSS или sitemap с публикациями и прислать URL.
- Отбраковка: `{}`
