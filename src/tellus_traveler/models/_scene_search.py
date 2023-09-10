from collections.abc import Iterator
from typing import Any

from .. import http_client
from . import Scene


class SceneSearch:
    """Search query for scenes.

    Attributes:
        params: Search query parameters.
    """

    def __init__(self, params: dict[str, Any]):  # noqa: D107
        self.params: dict[str, Any] = params

    def __repr__(self):  # noqa: D105
        return f"<tellus_traveler.SceneSearch params={self.params}>"

    def total(self) -> int:
        """Gets the total number of scenes that match the query.

        Returns:
            The total number of scenes.
        """
        response = self._request(self.params)
        return response["meta"]["total"]

    def scenes(self) -> Iterator[Scene]:
        """Returns [`Iterator`][collections.abc.Iterator] of scenes matched the query.

        Yields:
            Scene objects that match the query.
        """
        for page in self.pages():
            for scene_dict in page["features"]:
                yield Scene(scene_dict)

    def pages(self) -> Iterator[dict[str, Any]]:
        """Returns [`Iterator`][collections.abc.Iterator] of the search result pages.

        Yields:
            Search result dict that represents GeoJSON FeatureCollection.
        """
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
