import unittest
from lumimedia_sdk.transformer import resize_image, change_format
from PIL import Image
import io

class TestTransformer(unittest.TestCase):

    def setUp(self):
        self.image = Image.new("RGB", (200, 200), color='red')

    def test_resize_image(self):
        resized = resize_image(self.image, (100, 100))
        self.assertEqual(resized.size, (100, 100))

    def test_change_format(self):
        buffer = io.BytesIO()
        changed = change_format(self.image, "PNG")
        changed.save(buffer, format="PNG")
        buffer.seek(0)
        self.assertTrue(buffer.read().startswith(b'\x89PNG'))

if __name__ == "__main__":
    unittest.main()
