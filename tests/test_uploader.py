import os
import pytest
from lumimedia.uploader import MediaUploader


@pytest.fixture
def uploader():
    return MediaUploader(api_key="fake-api-key", upload_endpoint="https://example.com/upload")


def test_upload_file_success(monkeypatch, uploader):
    class DummyResponse:
        def raise_for_status(self): pass
        def json(self): return {"uploaded": True}

    monkeypatch.setattr("requests.post", lambda *args, **kwargs: DummyResponse())

    result = uploader.upload_file("demo/input/before.png")
    assert result == {"uploaded": True}


def test_upload_file_invalid_path(uploader):
    with pytest.raises(FileNotFoundError):
        uploader.upload_file("invalid_file.jpg")


def test_upload_folder_success(monkeypatch, uploader, tmp_path):
    # Setup a fake folder with fake files
    folder = tmp_path / "test_folder"
    folder.mkdir()
    file = folder / "test.jpg"
    file.write_bytes(b"fake data")

    class DummyResponse:
        def raise_for_status(self): pass
        def json(self): return {"uploaded": True}

    monkeypatch.setattr("requests.post", lambda *args, **kwargs: DummyResponse())

    results = uploader.upload_folder(folder)
    assert len(results) == 1
    assert results[0]["status"] == "success"


def test_upload_folder_invalid_path(uploader):
    with pytest.raises(NotADirectoryError):
        uploader.upload_folder("invalid_folder/")
