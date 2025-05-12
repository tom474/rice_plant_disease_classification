from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
from io import BytesIO
from datetime import datetime
from bson import ObjectId

from db import fs, prediction_collection
from utils.disease_classifier import classify_disease
from utils.variety_identifier import identify_variety
from utils.age_predictor import predict_age

router = APIRouter()


@router.post("/")
async def predict(file: UploadFile = File(...)):
    try:
        # Read and save image to GridFS
        contents = await file.read()
        image_stream = BytesIO(contents)
        image = Image.open(image_stream).convert("RGB")
        image_id = await fs.upload_from_stream(file.filename, BytesIO(contents))

        # Run all 3 predictions
        disease = classify_disease(image)
        variety = identify_variety(image)
        age = predict_age(image)

        # Save result to MongoDB
        prediction_record = {
            "image_id": str(image_id),
            "filename": file.filename,
            "disease": disease,
            "variety": variety,
            "age": age,
            "timestamp": datetime.utcnow(),
        }
        await prediction_collection.insert_one(prediction_record)

        return {
            "image_id": str(image_id),
            "disease": disease,
            "variety": variety,
            "age": age,
        }

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
