from tellus_traveler.api import scenes


def test_search():
    # When
    search = scenes.search(
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
