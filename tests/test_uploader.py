import pytest
import requests
from lumimedia.uploader import MediaUploader


@pytest.fixture
def uploader():
    return MediaUploader(
        api_key="fake-api-key",
        upload_endpoint="https://example.com/upload"
    )


def test_upload_file_success(monkeypatch, uploader):
    class DummyResponse:
        def raise_for_status(self): pass
        def json(self): return {"uploaded": True}

    monkeypatch.setattr(
        "requests.post",
        lambda *args, **kwargs: DummyResponse()
    )

    result = uploader.upload_file("demo/input/before.png")
    assert result == {"uploaded": True}


def test_upload_file_invalid_path(uploader):
    with pytest.raises(FileNotFoundError):
        uploader.upload_file("invalid_file.jpg")


def test_upload_file_request_failure(monkeypatch, uploader):
    def fail_post(*args, **kwargs):
        raise requests.RequestException("Simulated request failure")

    monkeypatch.setattr("requests.post", fail_post)

    with pytest.raises(ConnectionError):
        uploader.upload_file("demo/input/before.png")


def test_upload_folder_success(monkeypatch, uploader, tmp_path):
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


def test_upload_folder_partial_failure(monkeypatch, uploader, tmp_path):
    folder = tmp_path / "upload_folder"
    folder.mkdir()
    file = folder / "fail.jpg"
    file.write_bytes(b"123")

    def fail_upload(file_path):
        raise Exception("Simulated generic failure")

    monkeypatch.setattr(uploader, "upload_file", fail_upload)

    results = uploader.upload_folder(str(folder))
    assert len(results) == 1
    assert results[0]["status"] == "error"
    assert "Simulated generic failure" in results[0]["error"]


def test_sample_image_fixture_usage(sample_image_path):
    assert sample_image_path.exists()
    assert sample_image_path.read_bytes() == b"dummydata"
