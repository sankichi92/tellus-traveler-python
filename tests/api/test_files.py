import responses
from tellus_traveler import api


@responses.activate
def test_scene_files():
    # Given
    responses.get(
        "https://www.tellusxdp.com/api/traveler/v1/datasets/dataset_id/data/scene_id/files/",
        json={"results": [{"id": 1}]},
    )

    # When
    files = api.scene_files("dataset_id", "scene_id")

    # Then
    assert files[0]["id"] == 1


@responses.activate
def test_scene_file_url():
    # Given
    responses.post(
        "https://www.tellusxdp.com/api/traveler/v1/datasets/dataset-1/data/scene-1/files/1/download-url/",
        json={"download_url": "https://example.com/scene.tif"},
    )

    # When
    url = api.scene_file_url("dataset-1", "scene-1", 1)

    # Then
    assert url == "https://example.com/scene.tif"
