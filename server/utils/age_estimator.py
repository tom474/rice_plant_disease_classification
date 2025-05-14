import tensorflow as tf
import numpy as np
from PIL import Image
from utils.image_preprocessor import preprocess_image

# Load the age classification model
AGE_PREDICTION_MODEL_PATH = "models/age_prediction_model.keras"
age_prediction_model = tf.keras.models.load_model(AGE_PREDICTION_MODEL_PATH)

# Define the age classes (in days)
AGE_CLASSES = sorted(
    [45, 47, 50, 55, 57, 60, 62, 65, 66, 67, 68, 70, 72, 73, 75, 77, 80, 82]
)


def estimate_age(image_input: Image.Image, width: int = 128, height: int = 128) -> dict:
    """
    Estimate the age (in days) of a paddy plant based on its image, returning the result and confidence.

    The model is trained on discrete age classes. This function returns the predicted age category
    and its corresponding confidence score after preprocessing the input image.

    Args:
        image_input (PIL.Image.Image): Input image of the paddy plant.
        width (int): Target width for resizing. Default is 128.
        height (int): Target height for resizing. Default is 128.

    Returns:
        dict: Dictionary containing:
            - 'result' (int): Predicted age in days.
            - 'confidence' (float): Softmax confidence score (0.0 to 1.0), rounded to 4 decimals.
    """
    input_tensor = preprocess_image(image_input, width=width, height=height)
    prediction = age_prediction_model.predict(input_tensor)[0]
    predicted_idx = np.argmax(prediction)
    confidence = float(prediction[predicted_idx])
    return {"result": AGE_CLASSES[predicted_idx], "confidence": round(confidence, 4)}
