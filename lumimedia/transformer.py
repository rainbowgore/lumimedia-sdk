from PIL import Image
import io
import os

def resize_image(image_path: str, width: int, height: int) -> bytes:
    """
    Resize an image to the specified width and height.
    Returns the resized image as bytes.
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    with Image.open(image_path) as img:
        resized_img = img.resize((width, height))
        img_byte_arr = io.BytesIO()
        resized_img.save(img_byte_arr, format=img.format)
        return img_byte_arr.getvalue()

def convert_image_format(image_path: str, target_format: str) -> bytes:
    """
    Convert an image to a different format (e.g., JPEG, PNG).
    Returns the converted image as bytes.
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    with Image.open(image_path) as img:
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format=target_format.upper())
        return img_byte_arr.getvalue()

def compress_image(image_path: str, quality: int = 75) -> bytes:
    """
    Compress an image by reducing its quality.
    Returns the compressed image as bytes.
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    with Image.open(image_path) as img:
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format=img.format, optimize=True, quality=quality)
        return img_byte_arr.getvalue()

def change_format(image_path: str, target_format: str = "PNG") -> bytes:
    """
    Change the format of an image and return as bytes.
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    with Image.open(image_path) as img:
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format=target_format.upper())
        return img_byte_arr.getvalue()