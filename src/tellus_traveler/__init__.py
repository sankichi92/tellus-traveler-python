__all__ = ["get", "post"]

from .http_client import get, post

import os

api_token = os.environ.get("TELLUS_API_TOKEN", None)

base_url = os.environ.get(
    "TELLUS_TRAVELER_BASE_URL", "https://www.tellusxdp.com/api/traveler/v1"
)
