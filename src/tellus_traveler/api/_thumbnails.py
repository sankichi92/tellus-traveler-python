from .. import http_client
from ..models import File


def scene_thumbnails(dataset_id: str, scene_id: str) -> list[File]:
    """Get a list of thumbnail info belonging to a scene.

    <https://www.tellusxdp.com/docs/travelers/#/サムネイル/get_datasets__dataset_id__data__data_id__thumbnails_>

    Args:
        dataset_id: Dataset ID.
        scene_id: Scene ID.

    Returns:
        A list of `File` instances.
    """
    response = http_client.get(f"/datasets/{dataset_id}/data/{scene_id}/thumbnails/")
    thumbs = [
        File(dataset_id, scene_id, thumb, is_thumbnail=True)
        for thumb in response["results"]
    ]
    return thumbs
