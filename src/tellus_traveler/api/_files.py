from .. import http_client
from ..models import File


def scene_files(dataset_id: str, scene_id: str) -> list[File]:
    """Get a list of file info belonging to a scene.

    <https://www.tellusxdp.com/docs/travelers/#/ファイル/get_datasets__dataset_id__data__data_id__files_>

    Args:
        dataset_id: Dataset ID.
        scene_id: Scene ID.

    Returns:
        A list of `File` instances.
    """
    response = http_client.get(f"/datasets/{dataset_id}/data/{scene_id}/files/")
    files = [File(dataset_id, scene_id, file) for file in response["results"]]
    return files
