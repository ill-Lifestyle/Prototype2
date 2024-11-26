from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
import cv2
import numpy as np
from PIL import Image
import io

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Load the image
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

    # Simulate cleaning process
    cleaned_image = process_image(img)

    # Convert to bytes
    _, buffer = cv2.imencode('.png', cleaned_image)
    return StreamingResponse(io.BytesIO(buffer.tobytes()), media_type="image/png")


def process_image(img):
    # Example cleanup: Convert to grayscale and apply threshold
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, cleaned = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return cleaned

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
