import numpy as np
from PIL import Image
import tensorflow as tf
from preprocessing import preprocess_image

# Configurations
MODEL_PATH = "../models/age_prediction_model.keras"
IMAGE_PATH = "./data/200100.jpg"
AGE_CLASSES = sorted(
    [45, 47, 50, 55, 57, 60, 62, 65, 66, 67, 68, 70, 72, 73, 75, 77, 80, 82]
)


def predict_age(model_path: str, image_path: str, width: int = 128, height: int = 128):
    """
    Predicts the age class (in days) of a paddy plant from an image using a trained classification model.

    This function loads a pre-trained Keras model, preprocesses the input image (including resizing
    and normalization), runs the model to predict the age class index, and maps it to the actual age
    in days using AGE_CLASSES. It returns both the predicted age and the model's confidence score.

    Args:
        model_path (str): Path to the trained age classification model (.keras or .h5).
        image_path (str): Path to the input image of the rice plant.
        width (int, optional): Width to resize the image to. Defaults to 128.
        height (int, optional): Height to resize the image to. Defaults to 128.

    Returns:
        Tuple[int, float]: A tuple containing the predicted age (in days) and the confidence score (0.0–1.0).
    """
    # Load model
    model = tf.keras.models.load_model(model_path)

    # Load and preprocess image
    image = Image.open(image_path)
    input_tensor = preprocess_image(image, width=width, height=height, normalize=False)

    # Predict
    print("-" * 50)
    prediction = model.predict(input_tensor)[0]
    predicted_idx = np.argmax(prediction)
    predicted_age = AGE_CLASSES[predicted_idx]
    confidence = float(prediction[predicted_idx])

    # Output
    print("Model: Age Prediction Model")
    print("Image:", image_path)
    print("Predicted Age:", predicted_age)
    print("Confidence:", round(confidence, 4))

    return predicted_age, confidence


if __name__ == "__main__":
    predict_age(MODEL_PATH, IMAGE_PATH)
