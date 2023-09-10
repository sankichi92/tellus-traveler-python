import pytest
from tellus_traveler import models


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
