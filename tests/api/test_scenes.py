import responses
from tellus_traveler import api


def test_search():
    # When
    search = api.search(
        bbox=[1, 2, 3, 4],
        start_datetime="2023-09-09T00:00:00Z",
        end_datetime="2020-09-10T00:00:00Z",
        sort_by="start_datetime",
    )

    # Then
    assert search.params["intersects"] == {
        "type": "Polygon",
        "coordinates": [[[1, 2], [3, 2], [3, 4], [1, 4], [1, 2]]],
    }
    assert search.params["query"]["start_datetime"] == {"gte": "2023-09-09T00:00:00Z"}
    assert search.params["query"]["end_datetime"] == {"lte": "2020-09-10T00:00:00Z"}
    assert search.params["sort_by"] == [{"field": "start_datetime"}]


@responses.activate
def test_scene():
    # Given
    responses.get(
        "https://www.tellusxdp.com/api/traveler/v1/datasets/dataset_id/data/scene_id/",
        json={"id": "scene_id", "dataset_id": "dataset_id"},
    )

    # When
    scene = api.scene("dataset_id", "scene_id")

    # Then
    assert scene.id == "scene_id"
    assert scene.dataset_id == "dataset_id"
