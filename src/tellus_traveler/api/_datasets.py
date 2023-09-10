from typing import Any

from .. import http_client


def datasets(
    is_order_required: bool | None = None, has_order: bool | None = None
) -> list[dict[str, Any]]:
    """Gets a list of datasets with automatic pagination.

    <https://www.tellusxdp.com/docs/travelers/#/データセット/get_datasets_>

    Args:
        is_order_required: Whether orders are required to download files.
        has_order: Whether active orders exists.

    Returns:
        A list of dataset dictionaries.
    """

    def get_all_pages(url: str) -> list[dict[str, Any]]:
        response = http_client.get(url)
        if response.get("next"):
            return response["results"] + get_all_pages(response["next"])
        else:
            return response["results"]

    response = http_client.get(
        "/datasets/", is_order_required=is_order_required, has_order=has_order
    )

    if response.get("next"):
        return response["results"] + get_all_pages(response["next"])
    else:
        return response["results"]


def dataset(id: str) -> dict[str, Any]:
    """Gets a dataset by ID.

    <https://www.tellusxdp.com/docs/travelers/#/データセット/get_datasets__dataset_id__>

    Args:
        id: Dataset ID.

    Returns:
        A dataset dictionary.
    """
    return http_client.get(f"/datasets/{id}/")


def dataset_terms_url(id: str) -> str:
    """Gets a dataset terms of use URL by ID.

    <https://www.tellusxdp.com/docs/travelers/#/データセットメディア/get_datasets__dataset_id__terms_of_use_>

    Args:
        id: Dataset ID.

    Returns:
        A dataset terms of use URL.
    """
    return http_client.get(f"/datasets/{id}/terms-of-use/")


def dataset_manual_url(id: str) -> str:
    """Gets a dataset manual URL by ID.

    <https://www.tellusxdp.com/docs/travelers/#/データセットメディア/get_datasets__dataset_id__manual_>

    Args:
        id: Dataset ID.

    Returns:
        A dataset manual URL.
    """
    return http_client.get(f"/datasets/{id}/manual/")
