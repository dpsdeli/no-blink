from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, Response, StreamingResponse
import shutil
from pathlib import Path
import os
from io import BytesIO
import logging
import io

app = FastAPI(
    title="My FastAPI Service",
    description="A sample FastAPI service ready for Railway deployment",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI service!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/upload-image/")
async def upload_image(image: UploadFile = File(...)):
    logging.info(f"Received file: {image.filename} with type: {image.content_type}")
    
    # Validate file type
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    try:
        # Read the file content into memory
        content = await image.read()
        logging.info(f"Read content length: {len(content)} bytes")
        
        # Create a BytesIO object
        image_stream = io.BytesIO(content)
        image_stream.seek(0)
        
        # Return a streaming response
        return StreamingResponse(
            image_stream,
            media_type=image.content_type,
            headers={
                "Content-Disposition": f"inline; filename={image.filename}"
            }
        )
    except Exception as e:
        logging.error(f"Error processing image: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))