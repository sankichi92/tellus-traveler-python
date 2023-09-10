"""Client for Tellus Traveler API."""

__all__ = [
    "datasets",
    "dataset",
    "scene",
    "search",
    "get",
    "post",
]

import os

from .api import dataset, datasets, scene, search
from .http_client import get, post

api_token = os.environ.get("TELLUS_API_TOKEN", None)

base_url = os.environ.get(
    "TELLUS_TRAVELER_BASE_URL", "https://www.tellusxdp.com/api/traveler/v1/"
)
