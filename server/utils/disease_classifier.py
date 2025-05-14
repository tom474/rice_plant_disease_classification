import tensorflow as tf
import numpy as np
from PIL import Image
from utils.image_preprocessor import preprocess_image

# Load the disease classification model
DISEASE_CLASSIFICATION_MODEL_PATH = "./models/disease_classification_model.keras"
disease_classification_model = tf.keras.models.load_model(
    DISEASE_CLASSIFICATION_MODEL_PATH
)

# Define the disease classes
DISEASE_CLASSES = sorted(
    [
        "Bacterial Leaf Blight",
        "Bacterial Leaf Streak",
        "Bacterial Panicle Blight",
        "Blast",
        "Brown Spot",
        "Dead Heart",
        "Downy Mildew",
        "Hispa",
        "Normal",
        "Tungro",
    ]
)


def classify_disease(
    image_input: Image.Image, width: int = 256, height: int = 256
) -> dict:
    """
    Predict the disease class of a paddy plant image and return the result with confidence score.

    This function loads a pre-trained Keras model for disease classification, preprocesses
    the input image, and returns the predicted disease result along with its confidence score.

    Args:
        image_input (PIL.Image.Image): Input image to classify.
        width (int): Target width for resizing. Default is 256.
        height (int): Target height for resizing. Default is 256.

    Returns:
        dict: Dictionary containing:
            - 'result' (str): Predicted disease name.
            - 'confidence' (float): Softmax confidence score (0.0 to 1.0), rounded to 4 decimals.
    """
    input_tensor = preprocess_image(image_input, width=width, height=height)
    prediction = disease_classification_model.predict(input_tensor)[0]
    predicted_idx = np.argmax(prediction)
    confidence = float(prediction[predicted_idx])
    return {"result": DISEASE_CLASSES[predicted_idx], "confidence": round(confidence, 4)}
