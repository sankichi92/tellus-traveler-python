"""Thin HTTP client for Tellus Traveler API."""

from typing import Any
from urllib.parse import urljoin

import requests

import tellus_traveler


class HTTPError(IOError):
    """An HTTP error occurred."""

    def __init__(self, message: str, response: requests.Response):
        """Initialize HTTPError with `response` object."""
        self.response = response
        super().__init__(message)


def get(path: str, **params: Any):
    """Creates a GET request to Tellus Traveler API.

    Args:
        path: Path to the API endpoint.
        params: Query parameters.

    Returns:
        The JSON response body as a Python object.
    """
    return _request("get", path, params=params)


def post(path: str, **json: Any):
    """Creates a POST request to Tellus Traveler API.

    Args:
        path: Path to the API endpoint.
        json: JSON data to send in the request body.

    Returns:
        The JSON response body as a Python object.
    """
    return _request("post", path, json=json)


def _request(method: str | bytes, path: str, **kwargs: Any):
    if path.startswith("/"):
        path = path[1:]

    response = requests.request(
        method,
        urljoin(tellus_traveler.base_url, path),
        headers={"Authorization": f"Bearer {tellus_traveler.api_token}"},
        **kwargs,
    )

    if response.ok:
        return response.json()

    try:
        body = response.json()
        if body.keys() == {"code", "detail"}:
            raise HTTPError(
                f"{response.status_code} {body['code']}: {body['detail']}",
                response,
            )
        else:
            raise HTTPError(
                f"{response.status_code} {response.reason}: {body}",
                response,
            )
    except requests.exceptions.JSONDecodeError:
        raise HTTPError(f"{response.status_code} {response.reason}", response) from None
