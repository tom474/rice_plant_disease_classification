from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from bson import ObjectId
from db import fs
import gridfs
import io

router = APIRouter()


@router.get("/{image_id}")
async def get_image(image_id: str):
    """
    Retrieve an uploaded paddy image by its ID from GridFS.

    Args:
        image_id (str): The ObjectId of the image in GridFS.

    Returns:
        StreamingResponse: Image file stream if found.

    Raises:
        HTTPException: 404 if the image is not found or 400 if invalid ID.
    """
    try:
        file_id = ObjectId(image_id)
        grid_out = await fs.open_download_stream(file_id)
        content = await grid_out.read()
        return StreamingResponse(io.BytesIO(content), media_type="image/jpeg")

    except gridfs.errors.NoFile:
        raise HTTPException(status_code=404, detail="Image not found.")
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image ID.")
