import os
import zipfile
from io import BytesIO


def zip_files(files_path: str, files: list[str]) -> BytesIO:
    """Given the path of the files and which files to zip\n
    Returns a BytesIO zip file."""
    zipped = BytesIO()
    with zipfile.ZipFile(zipped, 'w') as zipf:
        for file in files:
            zipf.write(os.path.join(files_path, file), file)
    return zipped
