from __future__ import annotations

import hashlib
import html
import re
import unicodedata
from urllib.parse import parse_qsl, urlencode, urljoin, urlparse, urlunparse

TRACKING_QUERY_KEYS = {
    "fbclid",
    "gclid",
    "yclid",
    "mc_cid",
    "mc_eid",
    "mkt_tok",
    "ref",
    "ref_src",
    "source",
}


def normalize_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(value or "")).strip()


def normalize_url(url: str, base_url: str | None = None) -> str:
    raw = normalize_whitespace(url).rstrip(".,;:!?)]}\"'")
    if base_url:
        raw = urljoin(base_url, raw)
    parsed = urlparse(raw)
    scheme = "https" if parsed.scheme in {"http", "https"} else parsed.scheme
    host = (parsed.hostname or "").lower().strip(".")
    if host.startswith("www."):
        host = host[4:]

    port = parsed.port
    netloc = host
    if port and not ((scheme == "https" and port == 443) or (scheme == "http" and port == 80)):
        netloc = f"{host}:{port}"

    path = re.sub(r"/{2,}", "/", parsed.path or "/")
    if path != "/":
        path = path.rstrip("/")

    query_items: list[tuple[str, str]] = []
    for key, value in parse_qsl(parsed.query, keep_blank_values=True):
        lower = key.lower()
        if lower.startswith("utm_") or lower in TRACKING_QUERY_KEYS:
            continue
        query_items.append((key, value))
    query_items.sort()

    return urlunparse((scheme, netloc, path, "", urlencode(query_items, doseq=True), ""))


def domain_of(url: str) -> str:
    host = (urlparse(url).hostname or "").lower().strip(".")
    return host[4:] if host.startswith("www.") else host


def stable_id(value: str, length: int = 20) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:length]


def normalized_title(value: str) -> str:
    text = unicodedata.normalize("NFKC", normalize_whitespace(value)).casefold()
    text = re.sub(r"[^\w\s]", " ", text, flags=re.UNICODE)
    return re.sub(r"\s+", " ", text).strip()


def title_from_url(url: str) -> str:
    path = urlparse(url).path.strip("/")
    if not path:
        return domain_of(url)
    slug = path.split("/")[-1]
    slug = re.sub(r"\.(html?|php|aspx?)$", "", slug, flags=re.IGNORECASE)
    slug = re.sub(r"[-_]+", " ", slug)
    slug = re.sub(r"\s+", " ", slug).strip()
    return slug[:1].upper() + slug[1:] if slug else domain_of(url)
