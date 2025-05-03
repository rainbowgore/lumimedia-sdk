import os
import pytest
from lumimedia.transformer import (
    resize_image,
    convert_image_format,
    compress_image,
    change_format
)

TEST_IMAGE = "demo/input/before.png"

def test_resize_image_success():
    resized = resize_image(TEST_IMAGE, 100, 100)
    assert isinstance(resized, bytes)


def test_convert_image_format_success():
    converted = convert_image_format(TEST_IMAGE, "PNG")
    assert isinstance(converted, bytes)


def test_compress_image_success():
    compressed = compress_image(TEST_IMAGE, quality=50)
    assert isinstance(compressed, bytes)


def test_change_format_success():
    changed = change_format(TEST_IMAGE, "JPEG")
    assert isinstance(changed, bytes)

# --- Error handling (sad path) ---
def test_resize_image_invalid_path():
    with pytest.raises(FileNotFoundError):
        resize_image("invalid_path.jpg", 100, 100)


def test_convert_image_format_invalid_path():
    with pytest.raises(FileNotFoundError):
        convert_image_format("invalid_path.jpg", "JPEG")


def test_compress_image_invalid_path():
    with pytest.raises(FileNotFoundError):
        compress_image("invalid_path.jpg", quality=50)


def test_change_format_invalid_path():
    with pytest.raises(FileNotFoundError):
        change_format("invalid_path.jpg", "PNG")


# --- Legacy class-based tests (if needed for coverage) ---
class TestTransformer:

    def test_resize_image(self):
        result = resize_image(TEST_IMAGE, 120, 120)
        assert isinstance(result, bytes)

    def test_convert_image_format(self):
        result = convert_image_format(TEST_IMAGE, "JPEG")
        assert isinstance(result, bytes)

    def test_compress_image(self):
        result = compress_image(TEST_IMAGE, 60)
        assert isinstance(result, bytes)

    def test_change_format(self):
        result = change_format(TEST_IMAGE, "WEBP")
        assert isinstance(result, bytes)

    def test_resize_image_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            resize_image("nonexistent.png", 100, 100)

    def test_convert_image_format_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            convert_image_format("nonexistent.png", "jpeg")

    def test_compress_image_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            compress_image("nonexistent.png", quality=80)

    def test_change_format_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            change_format("nonexistent.png", "jpeg")
