import argparse
import os
from lumimedia_sdk.uploader import upload_and_compress

def compress_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"Error: The folder {folder_path} does not exist.")
        return

    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            file_path = os.path.join(folder_path, filename)
            print(f"Compressing {filename}...")
            upload_and_compress(file_path)

def main():
    parser = argparse.ArgumentParser(description="Compress all images in a folder.")
    parser.add_argument("compress_folder", type=str, help="Path to the folder containing images.")

    args = parser.parse_args()

    compress_folder(args.compress_folder)

if __name__ == "__main__":
    main()
