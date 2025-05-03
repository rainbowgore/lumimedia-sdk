import argparse
from lumimedia.uploader import upload_and_compress
from lumimedia.ai.face_cropper import smart_crop
import os


def compress_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            upload_and_compress(file_path)
            smart_crop(file_path)


def main():
    parser = argparse.ArgumentParser(description="LumiMedia SDK CLI")
    parser.add_argument("command", choices=["compress_folder"], help="Command to run")
    parser.add_argument("path", help="Path to folder")

    args = parser.parse_args()

    if args.command == "compress_folder":
        compress_folder(args.path)


if __name__ == "__main__":
    main()
