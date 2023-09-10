from collections import UserDict
from typing import Any


class File(UserDict[str, Any]):
    """File model.

    Attributes:
        dataset_id: Dataset ID that the file belongs to.
        scene_id: Scene ID that the file belongs to.
        is_thumbnail: Whether the file is a thumbnail.
    """

    def __init__(
        self,
        dataset_id: str,
        scene_id: str,
        data: dict[str, Any],
        is_thumbnail: bool = False,
    ):
        self.dataset_id: str = dataset_id
        self.scene_id: str = scene_id
        self.is_thumbnail: bool = is_thumbnail
        super().__init__(data)
