from fastapi import APIRouter
from bson import ObjectId
from db import prediction_collection

router = APIRouter()


@router.get("/")
async def get_prediction_history():
    """
    Retrieve all prediction records from MongoDB.
    Each record includes image reference, labels, and timestamp.
    """
    cursor = prediction_collection.find().sort("timestamp", -1)
    results = []

    async for doc in cursor:
        results.append(
            {
                "image_id": str(doc.get("image_id")),
                "image_url": f"/api/image/{doc.get('image_id')}",
                "filename": doc.get("filename"),
                "disease": doc.get("disease"),
                "variety": doc.get("variety"),
                "age": doc.get("age"),
                "timestamp": doc.get("timestamp"),
            }
        )

    return results
