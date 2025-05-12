from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from bson import ObjectId
from db import fs

router = APIRouter()


@router.get("/{image_id}")
async def get_image(image_id: str):
    try:
        stream = await fs.open_download_stream(ObjectId(image_id))
        return StreamingResponse(stream, media_type="image/jpeg")
    except:
        return {"error": "Image not found"}
