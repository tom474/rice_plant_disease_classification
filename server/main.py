from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers for different endpoints
from routers.predict import router as predict_router
from routers.history import router as history_router
from routers.image import router as image_router

app = FastAPI(
    title="PaddyScannerAI API",
    description="AI-powered backend for paddy disease classification, variety identification, and age prediction.",
    version="1.0.0",
)

# CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(predict_router, prefix="/api/predict", tags=["Predict"])
app.include_router(history_router, prefix="/api/history", tags=["History"])
app.include_router(image_router, prefix="/api/image", tags=["Image"])


@app.get("/")
async def root():
    return {"message": "PaddyScannerAI API is running."}
