import tensorflow as tf
import numpy as np
from PIL import Image
from utils.image_preprocessor import preprocess_image

# Load the age classification model
AGE_PREDICTION_MODEL_PATH = "models/age_classification_model.keras"
age_prediction_model = tf.keras.models.load_model(AGE_PREDICTION_MODEL_PATH)

# Define the age classes (in days)
AGE_CLASSES = sorted(
    [45, 47, 50, 55, 57, 60, 62, 65, 66, 67, 68, 70, 72, 73, 75, 77, 80, 82]
)


def predict_age(image_input: Image.Image, width: int = 128, height: int = 128) -> int:
    """
    Predict the age class (in days) of a paddy plant image.

    Args:
        image_input (PIL.Image.Image): Loaded PIL image.
        width (int): Target image width.
        height (int): Target image height.

    Returns:
        int: Predicted age in days.
    """
    input_tensor = preprocess_image(image_input, width=width, height=height)
    prediction = age_prediction_model.predict(input_tensor)[0]
    predicted_idx = np.argmax(prediction)
    return AGE_CLASSES[predicted_idx]
