from PIL import Image
import numpy as np


def preprocess_image(image: Image.Image, size=(128, 128)) -> np.ndarray:
    """
    Resize, normalize, and expand dims for model prediction.
    Returns a NumPy array of shape (1, 128, 128, 3)
    """
    image = image.resize(size)
    image = np.array(image) / 255.0  # Normalize to [0, 1]

    if image.ndim == 2:  # If grayscale, convert to 3 channels
        image = np.stack([image] * 3, axis=-1)

    return np.expand_dims(image, axis=0)  # (1, H, W, C)
