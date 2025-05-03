import unittest
import os
from lumimedia_sdk import uploader


class TestUploader(unittest.TestCase):

    def test_upload_success(self):
        result = uploader.upload_file("sample.jpg")
        self.assertIn("file_id", result)


if __name__ == "__main__":
    unittest.main()
