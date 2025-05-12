from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorGridFSBucket
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get MONGO_URI from evironment
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Connect to MongoDB
client = AsyncIOMotorClient(MONGO_URI)

# Use paddy_scanner_ai database
db = client["paddy_scanner_ai"]

# GridFS bucket for storing uploaded images
fs = AsyncIOMotorGridFSBucket(db, bucket_name="images")

# Collection for prediction results (metadata)
prediction_collection = db["predictions"]
