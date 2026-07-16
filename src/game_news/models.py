from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class SourceConfig:
    id: str
    name: str
    domain: str
    home_url: str
    category: str
    enabled: bool = True
    priority: int = 50
    language: str = "en"
    tags: list[str]