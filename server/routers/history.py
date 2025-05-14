from fastapi import APIRouter, Query
from db import prediction_collection
from datetime import datetime

router = APIRouter()


@router.get("/")
async def get_prediction_history(limit: int = Query(50, ge=1, le=100)):
    """
    Retrieve the most recent prediction records from MongoDB.

    Args:
        limit (int): Number of records to return (max 100).

    Returns:
        List of dicts: Each includes image metadata, predictions, and timestamp.
    """
    cursor = prediction_collection.find().sort("timestamp", -1).limit(limit)
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
                "timestamp": (
                    doc.get("timestamp").isoformat()
                    if isinstance(doc.get("timestamp"), datetime)
                    else None
                ),
            }
        )

    return results
