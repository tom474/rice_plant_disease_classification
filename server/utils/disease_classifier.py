import tensorflow as tf
import numpy as np
from PIL import Image
from utils.image_preprocessor import preprocess_image

# Load the disease classification model
DISEASE_CLASSIFICATION_MODEL_PATH = "./models/disease_classification_model.keras"
disease_classification_model = tf.keras.models.load_model(DISEASE_CLASSIFICATION_MODEL_PATH)

# Flat list of class labels
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
) -> str:
    """
    Predict the disease class of a paddy plant image.

    Args:
        image_input (PIL.Image.Image): Loaded PIL image.
        width (int): Target image width.
        height (int): Target image height.

    Returns:
        str: Predicted disease label.
    """
    input_tensor = preprocess_image(image_input, width=width, height=height)
    prediction = disease_classification_model.predict(input_tensor)[0]
    predicted_idx = np.argmax(prediction)
    return DISEASE_CLASSES[predicted_idx]
