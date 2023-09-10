from collections import UserDict
from pathlib import Path
from typing import Any

import requests

from .. import api


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

    def url(self) -> str:
        """Get a download URL of the file.

        Returns:
            A download URL of the file.
        """
        if self.is_thumbnail:
            return api.scene_thumbnail_url(
                self.dataset_id, self.scene_id, self.data["id"]
            )
        else:
            return api.scene_file_url(self.dataset_id, self.scene_id, self.data["id"])

    def download(self, dir: Path | str = ".", name: str | None = None) -> Path:
        """Download the file.

        Args:
            dir: Directory path to save the file.
            name: File name to save the file. If not given, the original file name is
                used.

        Returns:
            A `Path` instance of the downloaded file.
        """
        if name is None:
            name = str(self.data["name"])

        response = requests.get(self.url(), stream=True)
        response.raise_for_status()

        file_path = Path(dir, name)
        with file_path.open("wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)

        return file_path
