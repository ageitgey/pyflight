import os
import requests
import json


# Downloads the file at the specified URL if it is not found under the specified filename.
def download_file_if_not_exists(url: str, filename: str) -> dict:
    path = os.path.join("tests", filename)
    if not os.path.exists(path):
        resp = requests.get(url).json()
        with open(path, 'w+') as f:
            json.dump(resp, f)
        return resp

    with open(path, 'r') as f:
        return json.load(f)
