from typing import Any


class Scene:
    """Scene model that wraps a GeoJSON Feature.

    Attributes:
        __geo_interface__: GeoJSON Feature dictionary.
            See https://gist.github.com/sgillies/2217756.
    """

    def __init__(self, geojson: dict[str, Any]):  # noqa: D107
        self.__geo_interface__: dict[str, Any] = geojson

    def __repr__(self):  # noqa: D105
        return f"<tellus_traveler.Scene id={self.id}>"

    def __getitem__(self, key: str) -> Any:
        """Gets a property value by key."""
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
