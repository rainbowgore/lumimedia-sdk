from lumimedia.ai.background_remover import remove_background
from lumimedia.uploader import MediaUploader
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


INPUT_FOLDER = "demo/input"
OUTPUT_FOLDER = "demo/output"

API_KEY = "your_api_key"
UPLOAD_ENDPOINT = "https://httpbin.org/post"  # Fake upload target for demo


def run_demo():
    uploader = MediaUploader(API_KEY, UPLOAD_ENDPOINT)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    for filename in os.listdir(INPUT_FOLDER):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(INPUT_FOLDER, filename)
            output_path = os.path.join(OUTPUT_FOLDER, filename)

            print(f"Removing background for {filename}...")
            remove_background(input_path, output_path)

            print(f"Uploading {filename} after background removal...")
            try:
                uploader.upload_file(output_path)
                print(f"Successfully uploaded {filename}")
            except Exception as e:
                print(f"Failed to upload {filename}: {e}")


if __name__ == "__main__":
    run_demo()
