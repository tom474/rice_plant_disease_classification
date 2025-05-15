from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
from io import BytesIO
import traceback
from datetime import datetime, timezone
from utils.disease_classifier import classify_disease
from utils.variety_identifier import identify_variety
from utils.age_estimator import estimate_age
from db import fs, prediction_collection

router = APIRouter()


@router.post("/")
async def predict(file: UploadFile = File(...)):
    """
    Predict the disease class, variety, and age of a paddy plant image.

    This route performs the full prediction workflow:
    1. Stores the uploaded image in MongoDB GridFS.
    2. Runs disease, variety, and age prediction models.
    3. Saves the prediction result to the database.
    4. Returns all predictions with confidence and image ID.

    Args:
        file (UploadFile): An uploaded image file.

    Returns:
        JSON: {
            image_id: str,
            disease: {result: str, confidence: float},
            variety: {result: str, confidence: float},
            age: {result: int, confidence: float}
        }
    """
    try:
        contents = await file.read()
        image = Image.open(BytesIO(contents)).convert("RGB")
        image_id = await fs.upload_from_stream(file.filename, BytesIO(contents))

        disease = classify_disease(image)
        variety = identify_variety(image)
        age = estimate_age(image)

        prediction_record = {
            "image_id": str(image_id),
            "filename": file.filename,
            "disease": disease,
            "variety": variety,
            "age": age,
            "timestamp": datetime.now(),
        }
        await prediction_collection.insert_one(prediction_record)

        return {
            "image_id": str(image_id),
            "disease": disease,
            "variety": variety,
            "age": age,
        }

    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": str(e)})


@router.post("/disease")
async def predict_disease(file: UploadFile = File(...)):
    """
    Classify the disease of a paddy plant image.

    Args:
        file (UploadFile): Image file of the paddy plant.

    Returns:
        JSON: {
            result: str,
            confidence: float
        }
    """
    try:
        image_bytes = await file.read()
        image = Image.open(BytesIO(image_bytes)).convert("RGB")
        disease_result = classify_disease(image)

        return {
            "result": disease_result["result"],
            "confidence": disease_result["confidence"],
        }

    except Exception:
        return JSONResponse(status_code=500, content={"error": "Internal server error"})


@router.post("/variety")
async def predict_variety(file: UploadFile = File(...)):
    """
    Identify the variety of the paddy plant from the uploaded image.

    Args:
        file (UploadFile): Image file of the paddy plant.

    Returns:
        JSON: {
            result: str,
            confidence: float
        }
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files are allowed.")

    try:
        image_bytes = await file.read()
        image = Image.open(BytesIO(image_bytes)).convert("RGB")
        variety_result = identify_variety(image)

        return {
            "result": variety_result["result"],
            "confidence": variety_result["confidence"],
        }

    except Exception:
        return JSONResponse(status_code=500, content={"error": "Internal server error"})


@router.post("/age")
async def predict_age(file: UploadFile = File(...)):
    """
    Predict the age (in days) of the paddy plant from the uploaded image.

    Args:
        file (UploadFile): Image file of the paddy plant.

    Returns:
        JSON: {
            result: int,
            confidence: float
        }
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files are allowed.")

    try:
        image_bytes = await file.read()
        image = Image.open(BytesIO(image_bytes)).convert("RGB")
        age_result = estimate_age(image)

        return {"result": age_result["result"], "confidence": age_result["confidence"]}

    except Exception:
        return JSONResponse(status_code=500, content={"error": "Internal server error"})
