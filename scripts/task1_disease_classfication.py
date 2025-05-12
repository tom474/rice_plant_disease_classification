import numpy as np
from PIL import Image
import tensorflow as tf
from preprocessing import preprocess_image

# Configurations
MODEL_PATH = "../models/disease_classification_model.keras"
IMAGE_PATH = "./data/200001.jpg"
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
    model_path: str, image_path: str, width: int = 256, height: int = 256
):
    """
    Classifies the disease present in a paddy plant image using a trained deep learning model.

    This function loads a disease classification model from the given path, preprocesses the input
    image (removes transparency, resizes, normalizes), performs prediction, and prints the result.
    It returns the predicted disease label and its confidence score.

    Args:
        model_path (str): Path to the trained Keras classification model (.keras or .h5).
        image_path (str): Path to the input image (e.g., JPG or PNG format).
        width (int, optional): Target width for preprocessing. Defaults to 256.
        height (int, optional): Target height for preprocessing. Defaults to 256.

    Returns:
        Tuple[str, float]: A tuple containing the predicted disease label and its confidence score (0.0 to 1.0).
    """
    # Load model
    model = tf.keras.models.load_model(model_path)

    # Load and preprocess image
    image = Image.open(image_path)
    input_tensor = preprocess_image(image, width=width, height=height)

    # Predict
    prediction = model.predict(input_tensor)[0]
    predicted_idx = np.argmax(prediction)
    predicted_disease = DISEASE_CLASSES[predicted_idx]
    confidence = float(prediction[predicted_idx])

    # Output
    print("-" * 50)
    print("Model: Disease Classification Model")
    print("Image:", image_path)
    print("Predicted Disease:", predicted_disease)
    print("Confidence:", round(confidence, 4))

    return predicted_disease, confidence


if __name__ == "__main__":
    classify_disease(MODEL_PATH, IMAGE_PATH)
