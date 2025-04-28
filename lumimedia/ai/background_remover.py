from rembg import remove
import cv2
import numpy as np
import os

def remove_background(input_path: str, output_path: str = None):
    if not output_path:
        output_path = input_path.replace("input", "output")
        if not output_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            output_path += ".png"

    input_image = cv2.imread(input_path)
    input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

    result = remove(
        input_image,
        alpha_matting=True,
        alpha_matting_foreground_threshold=240,
        alpha_matting_background_threshold=10,
        alpha_matting_erode_size=5,
    )

    result = cv2.cvtColor(np.array(result), cv2.COLOR_RGB2BGRA)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, result)

if __name__ == "__main__":
    remove_background("demo/input/sample.png")