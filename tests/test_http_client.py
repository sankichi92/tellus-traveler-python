import pytest
import responses
import tellus_traveler
import tellus_traveler.http_client as http_client
from responses import matchers


@responses.activate
def test_get():
    # Given
    tellus_traveler.api_token = "dummy"
    responses.get(
        "https://www.tellusxdp.com/api/traveler/v1/test/",
        match=[matchers.header_matcher({"Authorization": "Bearer dummy"})],
        json={"result": "ok"},
    )

    # When
    res = http_client.get("/test/")

    # Then
    assert res == {"result": "ok"}


@responses.activate
def test_get_raises_http_error():
    # Given
    responses.get(
        "https://www.tellusxdp.com/api/traveler/v1/test/",
        status=403,
        json={"code": "authentication_failed", "detail": "Invalid token"},
    )

    # When/Then
    with pytest.raises(http_client.HTTPError) as excinfo:
        http_client.get("/test/")
    assert excinfo.value.response.status_code == 403
    assert str(excinfo.value) == "403 authentication_failed: Invalid token"


@responses.activate
def test_post():
    # Given
    responses.post(
        "https://www.tellusxdp.com/api/traveler/v1/test/",
        match=[matchers.json_params_matcher({"foo": "bar"})],
        json={"result": "ok"},
    )

    # When
    res = http_client.post("/test/", foo="bar")

    # Then
    assert res == {"result": "ok"}
