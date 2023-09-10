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
