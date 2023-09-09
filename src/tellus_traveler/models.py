"""Model classes."""

from typing import Any, Iterator

from . import http_client


class SceneSearch:
    """Search query for scenes."""

    def __init__(self, **params: Any):  # noqa: D107
        self.params = params

    def __repr__(self):  # noqa: D105
        return f"<tellus_traveler.SceneSearch params={self.params}>"

    def total(self) -> int:
        """Gets the total number of scenes that match the query."""
        response = self._request(self.params)
        return response["meta"]["total"]

    def scenes(self) -> Iterator["Scene"]:
        """Yields scenes that match the query."""
        for page in self.pages():
            for scene_dict in page["features"]:
                yield Scene(scene_dict)

    def pages(self) -> Iterator[dict[str, Any]]:
        """Yields pages that match the query."""
        count = 0
        params = self.params

        while True:
            page = self._request(params)

            meta = page.pop("meta")
            yield page

            count += len(page["features"])
            if count >= meta["total"]:
                break

            params = meta["search-condition"]

    @staticmethod
    def _request(params: dict[str, Any]) -> dict[str, Any]:
        return http_client.post("/data-search/", **params)


class Scene:
    """Scene, which is a GeoJSON Feature.

    Attributes:
        __geo_interface__: GeoJSON Feature dictionary.
            See https://gist.github.com/sgillies/2217756.
    """

    def __init__(self, geojson: dict[str, Any]):  # noqa: D107
        self.__geo_interface__ = geojson

    def __repr__(self):  # noqa: D105
        return f"<tellus_traveler.Scene id={self.id}>"

    def __getitem__(self, key: str) -> Any:
        """Gets a property value by key. Raises KeyError if the key is not found."""
        if key in self.properties:
            return self.properties[key]
        else:
            raise KeyError(key)

    def get(self, key: str, default: Any = None) -> Any:
        """Gets a property value by key. Returns `default` if the key is not found."""
        try:
            return self[key]
        except KeyError:
            return default

    @property
    def id(self) -> str:
        """Scene ID."""
        return self.__geo_interface__["id"]

    @property
    def dataset_id(self) -> str:
        """Dataset ID that the scene belongs to."""
        return self.__geo_interface__["dataset_id"]

    @property
    def geometry(self) -> dict[str, Any]:
        """GeoJSON Geometry dictionary."""
        return self.__geo_interface__["geometry"]

    @property
    def properties(self) -> dict[str, Any]:
        """Dataset properties."""
        return self.__geo_interface__["properties"]
