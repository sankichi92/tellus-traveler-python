import responses
from tellus_traveler import api


@responses.activate
def test_datasets():
    # Given
    responses.get(
        "https://www.tellusxdp.com/api/traveler/v1/datasets/", json={"results": [0]}
    )

    # When
    res = api.datasets()

    # Then
    assert res == [0]


@responses.activate
def test_dataset_with_next():
    # Given
    responses.get(
        "https://www.tellusxdp.com/api/traveler/v1/datasets/",
        json={
            "results": [0],
            "next": "https://www.tellusxdp.com/api/traveler/v1/datasets/?page=2",
        },
    )
    responses.get(
        "https://www.tellusxdp.com/api/traveler/v1/datasets/?page=2",
        json={"results": [1]},
    )

    # When
    res = api.datasets()

    # Then
    assert res == [0, 1]


@responses.activate
def test_dataset():
    # Given
    responses.get(
        "https://www.tellusxdp.com/api/traveler/v1/datasets/1/", json={"id": "1"}
    )

    # When
    res = api.dataset("1")

    # Then
    assert res == {"id": "1"}


@responses.activate
def test_dataset_terms_url():
    # Given
    responses.get(
        "https://www.tellusxdp.com/api/traveler/v1/datasets/1/terms-of-use/",
        status=302,
        headers={"Location": "https://example.com/terms"},
    )

    # When
    res = api.dataset_terms_url("1")

    # Then
    assert res == "https://example.com/terms"


@responses.activate
def test_dataset_manual_url():
    # Given
    responses.get(
        "https://www.tellusxdp.com/api/traveler/v1/datasets/1/manual/",
        status=302,
        headers={"Location": "https://example.com/manual"},
    )

    # When
    res = api.dataset_manual_url("1")

    # Then
    assert res == "https://example.com/manual"
