# LumiMedia SDK

A lightweight SDK for media compression and optimization workflows, ideal for web and mobile developers.

---

## Overview

LumiMedia SDK provides tools to:

- Compress images via API
- Log actions and debug sessions
- Retry failed API calls
- Modularize and scale compression workflows

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
# Command Line Interface
python cli.py compress_folder /path/to/your/folder

# Python SDK Usage
from lumimedia_sdk.uploader import upload_and_compress

upload_and_compress("path/to/image.jpg")
```

---

## Requirements

- Python 3.8+
- requests
- tqdm

---

## Project Structure

```
lumimedia_sdk/
    __init__.py
    uploader.py
    transformer.py
    metadata.py
    logger.py
tests/
    test_uploader.py
    test_transformer.py
cli.py
README.md
requirements.txt
setup.py
LICENSE
```

---

## Quick Demo

1. Add images to `demo/input/`
2. Run the demo:

```bash
python demo/run_demo.py

----

## License

MIT License.
```
