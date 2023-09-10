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
