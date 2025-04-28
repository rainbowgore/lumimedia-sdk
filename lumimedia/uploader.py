import os
import requests

class MediaUploader:
    def __init__(self, api_key: str, upload_endpoint: str):
        self.api_key = api_key
        self.upload_endpoint = upload_endpoint

    def upload_file(self, file_path: str) -> dict:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        files = {'file': open(file_path, 'rb')}
        headers = {'Authorization': f'Bearer {self.api_key}'}

        try:
            response = requests.post(self.upload_endpoint, files=files, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise ConnectionError(f"Failed to upload {file_path}: {e}")

    def upload_folder(self, folder_path: str) -> list:
        if not os.path.isdir(folder_path):
            raise NotADirectoryError(f"Not a directory: {folder_path}")

        results = []
        for root, _, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                try:
                    upload_result = self.upload_file(file_path)
                    results.append({"file": file_path, "status": "success", "result": upload_result})
                except Exception as e:
                    results.append({"file": file_path, "status": "error", "error": str(e)})
        return results
