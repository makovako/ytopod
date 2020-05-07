from pathlib import Path
import os

def extract_video_id(url):
    url_split = url.split('?')
    if len(url_split) < 2:
        return null
    for param in url_split[1].split('&'):
        key, value = param.split("=")
        if key == "v":
            return value
    return null

def create_download_directory():
    """Tries to create download directory at startup."""

    path = Path(os.getcwd()).joinpath('download')
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
    except (OSError,FileExistsError,FileNotFoundError) as error:
        print("Creation of downlaod directory failed")
        print(error)