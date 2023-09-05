import requests

import tellus_traveler


class HTTPError(IOError):
    def __init__(self, message: str, response: requests.Response):
        self.response = response
        super().__init__(message)


def get(path: str, **params):
    return _request("get", path, params=params)


def post(path: str, **json):
    return _request("post", path, json=json)


def _request(method: str | bytes, path: str, **kwargs):
    response = requests.request(
        method,
        tellus_traveler.base_url + path,
        headers={"Authorization": f"Bearer {tellus_traveler.api_token}"},
        **kwargs,
    )

    if response.ok:
        return response.json()

    try:
        body = response.json()
        raise HTTPError(
            f"{response.status_code} {body.get('code')}: {body.get('detail')}",
            response,
        )
    except requests.exceptions.JSONDecodeError:
        raise HTTPError(f"{response.status_code} {response.reason}", response)
