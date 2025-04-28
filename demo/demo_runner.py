import os
from lumimedia_sdk.uploader import upload_and_compress

# Define input and output directories
input_dir = os.path.join(os.path.dirname(__file__), "input")
output_dir = os.path.join(os.path.dirname(__file__), "output")

# Make sure output directory exists
os.makedirs(output_dir, exist_ok=True)

def compress_images():
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            print(f"Compressing {filename}...")
            upload_and_compress(input_path)

if __name__ == "__main__":
    compress_images()