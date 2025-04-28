import pytest

@pytest.fixture
def sample_image_path(tmp_path):
    img_path = tmp_path / "test_image.jpg"
    img_path.write_bytes(b"dummydata")
    return img_path