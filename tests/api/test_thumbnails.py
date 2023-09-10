import responses
from tellus_traveler import api


@responses.activate
def test_scene_thumbnails():
    # Given
    responses.get(
        "https://www.tellusxdp.com/api/traveler/v1/datasets/dataset_id/data/scene_id/thumbnails/",
        json={"results": [{"id": 1}]},
    )

    # When
    thumbs = api.scene_thumbnails("dataset_id", "scene_id")

    # Then
    assert thumbs[0].is_thumbnail
    assert thumbs[0]["id"] == 1


@responses.activate
def test_scene_thumbnail_url():
    # Given
    responses.post(
        "https://www.tellusxdp.com/api/traveler/v1/datasets/dataset-1/data/scene-1/thumbnails/1/download-url/",
        json={"download_url": "https://example.com/thumb.png"},
    )

    # When
    url = api.scene_thumbnail_url("dataset-1", "scene-1", 1)

    # Then
    assert url == "https://example.com/thumb.png"
