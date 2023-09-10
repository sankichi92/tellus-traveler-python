"""Client for Tellus Traveler API."""

__all__ = [
    "dataset",
    "dataset_manual_url",
    "dataset_terms_url",
    "datasets",
    "scene",
    "search",
    "get",
    "post",
]

import os

from .api import dataset, dataset_manual_url, dataset_terms_url, datasets, scene, search
from .http_client import get, post

api_token = os.environ.get("TELLUS_API_TOKEN", None)

base_url = os.environ.get(
    "TELLUS_TRAVELER_BASE_URL", "https://www.tellusxdp.com/api/traveler/v1/"
)
