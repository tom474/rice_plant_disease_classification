import numpy as np
from PIL import Image
import tensorflow as tf
from preprocessing import preprocess_image

# Configurations
MODEL_PATH = "../models/variety_identification_model.keras"
IMAGE_PATH = "./data/200100.jpg"
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
    model_path: str, image_path: str, width: int = 128, height: int = 128
):
    """
    Identifies the rice variety from an input image using a trained classification model.

    This function loads a variety classification model, preprocesses the image by resizing
    and normalizing it, performs prediction, and returns the predicted variety label along
    with its confidence score.

    Args:
        model_path (str): Path to the trained Keras model (.keras or .h5).
        image_path (str): Path to the image of the rice plant.
        width (int, optional): Width to resize the input image to. Defaults to 128.
        height (int, optional): Height to resize the input image to. Defaults to 128.

    Returns:
        Tuple[str, float]: A tuple containing the predicted variety name and the model's confidence score (0.0–1.0).
    """
    # Load model
    model = tf.keras.models.load_model(model_path)

    # Load and preprocess image
    image = Image.open(image_path)
    input_tensor = preprocess_image(image, width=width, height=height, normalize=False)

    # Predict
    prediction = model.predict(input_tensor)[0]
    predicted_idx = np.argmax(prediction)
    predicted_variety = VARIETY_CLASSES[predicted_idx]
    confidence = float(prediction[predicted_idx])

    # Output
    print("-" * 50)
    print("Model: Variety Identification Model")
    print("Image:", image_path)
    print("Predicted Variety:", predicted_variety)
    print("Confidence:", round(confidence, 4))

    return predicted_variety, confidence


if __name__ == "__main__":
    identify_variety(MODEL_PATH, IMAGE_PATH)
