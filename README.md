# LumiMedia SDK

![License](https://img.shields.io/github/license/rainbowgore/lumimedia-sdk)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Build Status](https://img.shields.io/github/actions/workflow/status/rainbowgore/lumimedia-sdk/python-app.yml?branch=main)
![Repo Size](https://img.shields.io/github/repo-size/rainbowgore/lumimedia-sdk)

> A lightweight AI-powered media SDK for developers — automatic background removal, compression, metadata extraction, and easy uploads.

---

## Features

- **Upload API** — Streamlined HTTP uploads.
- **Compression Engine** — Optimized media size for web/mobile.
- **Background Removal** — Remove backgrounds from photos and artistic images (powered by AI).
- **Metadata Extraction** — Access file details programmatically.
- **Smart Retry Logic** — Resilient uploads with retry on failure.
- **Face Cropping (Optional)** — AI-assisted face detection and smart cropping (experimental).
- **Modular, Scalable Design** — Built for clean expansion.

---

## Installation

```bash
pip install -r requirements.txt
```

Requires Python 3.8+.

---

## 🛠 Usage

### CLI

```bash
python cli/cli.py compress_folder /path/to/your/folder
```

- Compress images in a folder and save optimized outputs to `/demo/output/`.

---

### Python SDK

```python
from lumimedia.uploader import MediaUploader
from lumimedia.ai.background_remover import remove_background

uploader = MediaUploader("your_api_key", "https://your-upload-endpoint.com")

# Upload and compress
uploader.upload_file("path/to/image.jpg")

# Remove background
remove_background("path/to/image.jpg", "path/to/output.png")
```

---

## Demo

**Automatic Background Removal**

|              Before              |             After              |
| :------------------------------: | :----------------------------: |
| ![Before](demo/input/before.png) | ![After](demo/input/after.png) |

---

## Project Structure

```
lumimedia-sdk/
├── cli/
│   └── cli.py
├── demo/
│   ├── input/
│   ├── output/
│   └── demo_runner.py
├── lumimedia/
│   ├── __init__.py
│   ├── logger.py
│   ├── metadata.py
│   ├── transformer.py
│   ├── uploader.py
│   └── ai/
│       ├── background_remover.py
│       └── face_cropper.py
├── tests/
│   ├── conftest.py
│   ├── test_transformer.py
│   └── test_uploader.py
├── .env.example
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
└── .github/
    └── workflows/
        └── python-app.yml
```

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
