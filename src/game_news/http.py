from __future__ import annotations

import time
from dataclasses import dataclass

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


@dataclass(slots=True)
class HttpResponse:
    url: str
    status_code: int
    text: str
    content_type: str


class HttpClient:
    def __init__(self, user_agent: str, timeout_seconds: int = 20) -> None:
        # Full audits touch many third-party domains. Keep the per-request budget
        # bounded so a handful of dead or blocked sites cannot consume the job.
        self.timeout_seconds = min(timeout_seconds, 12)
        self.session = requests.Session()
        retry = Retry(
            total=1,
            connect=1,
            read=1,
            status=1,
            backoff_factor=0.5,
            status_forcelist=(429, 500, 502, 503, 504),
            allowed_methods=frozenset({"GET", "HEAD"}),
            respect_retry_after_header=True,
        )
        adapter = HTTPAdapter(max_retries=retry, pool_connections=24, pool_maxsize=24)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        self.session.headers.update(
            {
                "User-Agent": user_agent,
                "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, text/html;q=0.9, */*;q=0.5",
                "Accept-Language": "en-US,en;q=0.8,ru;q=0.6",
                "Cache-Control": "no-cache",
            }
        )

    def get(self, url: str, delay_seconds: float = 0.0) -> HttpResponse:
        if delay_seconds > 0:
            time.sleep(delay_seconds)
        response = self.session.get(url, timeout=self.timeout_seconds, allow_redirects=True)
        response.raise_for_status()
        response.encoding = response.encoding or response.apparent_encoding or "utf-8"
        return HttpResponse(
            url=response.url,
            status_code=response.status_code,
            text=response.text,
            content_type=response.headers.get("content-type", "").split(";", 1)[0].lower(),
        )
