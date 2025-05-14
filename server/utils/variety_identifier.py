import tensorflow as tf
import numpy as np
from PIL import Image
from utils.image_preprocessor import preprocess_image

# Load the variety classification model
VARIETY_IDENTIFICATION_MODEL_PATH = "../models/variety_identification_model.keras"
variety_identification_model = tf.keras.models.load_model(
    VARIETY_IDENTIFICATION_MODEL_PATH
)

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
) -> dict:
    """
    Predict the variety class of a paddy plant image and return the result with confidence score.

    This function uses a trained Keras model to identify the paddy variety based on visual features.
    It preprocesses the input image and returns the predicted result and associated confidence.

    Args:
        image_input (PIL.Image.Image): Input image to classify.
        width (int): Target width for resizing. Default is 128.
        height (int): Target height for resizing. Default is 128.

    Returns:
        dict: Dictionary containing:
            - 'result' (str): Predicted paddy variety.
            - 'confidence' (float): Softmax confidence score (0.0 to 1.0), rounded to 4 decimals.
    """
    input_tensor = preprocess_image(image_input, width=width, height=height, normalize=False)
    prediction = variety_identification_model.predict(input_tensor)[0]
    predicted_idx = np.argmax(prediction)
    confidence = float(prediction[predicted_idx])
    return {"result": VARIETY_CLASSES[predicted_idx], "confidence": round(confidence, 4)}
