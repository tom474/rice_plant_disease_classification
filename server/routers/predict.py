from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
from io import BytesIO
from datetime import datetime
from bson import ObjectId
import tensorflow as tf

from utils.preprocessing import preprocess_image

router = APIRouter()

# Load models
disease_classification_model = tf.keras.models.load_model("../models/disease_classification_model.keras")

@router.post("/disease")
async def classify_disease(file: UploadFile = File(...)):
    try:
        image = Image.open(BytesIO(await file.read()))
        input_image = preprocess_image(image)
        
        # Predict using the disease classification model
        predictions = disease_classification_model.predict(input_image)
        predicted_class = tf.argmax(predictions, axis=1).numpy()[0]
        confidence = tf.reduce_max(predictions, axis=1).numpy()[0]
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
        