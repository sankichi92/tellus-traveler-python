"""Scene endpoints.

https://www.tellusxdp.com/docs/travelers/#/シーン
"""

from datetime import datetime
from typing import Any, Iterator

from ..models import SceneSearch


def search(
    datasets: list[str] | None = None,
    bbox: list[float] | tuple[float, ...] | Iterator[float] | None = None,
    intersects: dict[str, Any] | None = None,
    start_datetime: str | datetime | None = None,
    end_datetime: str | datetime | None = None,
    query: dict[str, Any] | None = None,
    is_order_required: bool | None = None,
    only_downloadable_file: bool | None = None,
    sort_by: list[dict[str, str]] | dict[str, str] | str | None = None,
) -> SceneSearch:
    """Search scenes.

    https://www.tellusxdp.com/docs/travelers/#/シーン/post_data_search_

    Args:
        datasets: Dataset IDs.
        bbox: Bounding box of coordinates.
        intersects: GeoJSON Polygon geometry.
        start_datetime: Observation start datetime.
        end_datetime: Observation end datetime.
        query: Other queries for dataset properties. See the API doc for more details.
        is_order_required: Whether orders are required to download files.
        only_downloadable_file: Whether to return only scenes which files are
            downloadable.
        sort_by: Dataset properties to sort by.

    Returns:
        A [SceneSearch][tellus_traveler.models.SceneSearch] instance that
        represents deferred query.
    """
    if bbox is not None:
        if intersects is not None:
            raise ValueError("intersects and bbox cannot be set at the same time.")

        x1, y1, x2, y2 = bbox
        intersects = {
            "type": "Polygon",
            "coordinates": [
                [
                    [x1, y1],
                    [x2, y1],
                    [x2, y2],
                    [x1, y2],
                    [x1, y1],
                ]
            ],
        }

    if query is None:
        query = {}

    if start_datetime is not None:
        if "start_datetime" in query:
            raise ValueError("start_datetime is already set in query.")

        if isinstance(start_datetime, datetime):
            start_datetime = start_datetime.isoformat()

        query["start_datetime"] = {"gte": start_datetime}

    if end_datetime is not None:
        if "end_datetime" in query:
            raise ValueError("end_datetime is already set in query.")

        if isinstance(end_datetime, datetime):
            end_datetime = end_datetime.isoformat()

        query["end_datetime"] = {"lte": end_datetime}

    if isinstance(sort_by, str):
        sort_by = [{"field": sort_by}]
    elif isinstance(sort_by, dict):
        sort_by = [sort_by]

    return SceneSearch(
        query=query,
        datasets=datasets,
        intersects=intersects,
        is_order_required=is_order_required,
        only_downloadable_file=only_downloadable_file,
        sort_by=sort_by,
    )
