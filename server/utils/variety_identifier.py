import tensorflow as tf
import numpy as np
from PIL import Image
from utils.image_preprocessor import preprocess_image

# Load the variety classification model
VARIETY_IDENTIFICATION_MODEL_PATH = "./models/variety_identification_model.keras"
variety_identification_model = tf.keras.models.load_model(VARIETY_IDENTIFICATION_MODEL_PATH)

# Define the variety classes
VARIETY_CLASSES = sorted(
    [
        "ADT45",
        "AndraPonni",
        "AtchayaPonni",
        "IR20",
        "KarnatakaPonni",
        "Onthanel",
        "Ponni",
        "RR",
        "Surya",
        "Zonal",
    ]
)


def identify_variety(
    image_input: Image.Image, width: int = 128, height: int = 128
) -> str:
    """
    Predict the variety class of a paddy plant image.

    Args:
        image_input (PIL.Image.Image): Loaded PIL image.
        width (int): Target image width.
        height (int): Target image height.

    Returns:
        str: Predicted variety name.
    """
    input_tensor = preprocess_image(image_input, width=width, height=height)
    prediction = variety_identification_model.predict(input_tensor)[0]
    predicted_idx = np.argmax(prediction)
    return VARIETY_CLASSES[predicted_idx]
