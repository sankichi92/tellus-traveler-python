import pytest
import responses
from tellus_traveler import models


class TestSceneSearch:
    @responses.activate
    def test_total(self):
        # Given
        responses.post(
            "https://www.tellusxdp.com/api/traveler/v1/data-search/",
            json={"meta": {"total": 100}},
        )

        # When
        search = models.SceneSearch()
        total = search.total()

        # Then
        assert total == 100

    @responses.activate
    def test_scenes(self):
        # Given
        responses.post(
            "https://www.tellusxdp.com/api/traveler/v1/data-search/",
            json={
                "features": [{"id": "1"}, {"id": "2"}],
                "meta": {
                    "total": 4,
                    "search-condition": {"paginate": {"size": 2, "cursor": "dummy"}},
                },
            },
        )
        responses.post(
            "https://www.tellusxdp.com/api/traveler/v1/data-search/",
            match=[
                responses.matchers.json_params_matcher(
                    {"paginate": {"size": 2, "cursor": "dummy"}}
                )
            ],
            json={"features": [{"id": "3"}, {"id": "4"}], "meta": {"total": 4}},
        )

        # When
        search = models.SceneSearch()
        scenes = search.scenes()

        # Then
        assert len(list(scenes)) == 4

    @responses.activate
    def test_pages(self):
        # Given
        responses.post(
            "https://www.tellusxdp.com/api/traveler/v1/data-search/",
            json={
                "features": [{"id": "1"}, {"id": "2"}],
                "meta": {
                    "total": 4,
                    "search-condition": {"paginate": {"size": 2, "cursor": "dummy"}},
                },
            },
        )
        responses.post(
            "https://www.tellusxdp.com/api/traveler/v1/data-search/",
            match=[
                responses.matchers.json_params_matcher(
                    {"paginate": {"size": 2, "cursor": "dummy"}}
                )
            ],
            json={"features": [{"id": "3"}, {"id": "4"}], "meta": {"total": 4}},
        )

        # When
        search = models.SceneSearch()
        pages = search.pages()

        # Then
        assert next(pages) == {"features": [{"id": "1"}, {"id": "2"}]}
        assert next(pages) == {"features": [{"id": "3"}, {"id": "4"}]}
        assert next(pages, None) is None


class TestScene:
    @pytest.fixture()
    def scene(self):
        return models.Scene(
            {
                "id": "scene-1",
                "dataset_id": "dateset-1",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [[-180, 90], [180, 90], [180, -90], [-180, -90], [-180, 90]]
                    ],
                },
                "properties": {"key": "value"},
            }
        )

    def test_getitem(self, scene):
        assert scene["key"] == "value"

    def test_id(self, scene):
        assert scene.id == "scene-1"

    def test_dataset_id(self, scene):
        assert scene.dataset_id == "dateset-1"

    def test_geometry(self, scene):
        assert scene.geometry["type"] == "Polygon"
