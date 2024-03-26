from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os

app = FastAPI()


UPLOAD_DIR = "file/rename"
user_dir = os.path.expanduser("~")

@app.post("/upload/image/")
async def upload_image(file: UploadFile = File(...)):
    
    file_path = os.path.join(user_dir, UPLOAD_DIR, file.filename)

    contents = await file.read()
    with open(file_path, "wb") as f:
        f.write(contents)
    
    return JSONResponse(content={"message": "Image uploaded successfully"}, status_code=200)


@app.post("/upload/video/")
async def upload_video(file: UploadFile = File(...)):
    file_path = os.path.join(user_dir, UPLOAD_DIR, file.filename)
    contents = await file.read()
    with open(file_path, "wb") as f:
        f.write(contents)
    
    return JSONResponse(content={"message": "Video uploaded successfully"}, status_code=200)

@app.post("/upload/text/")
async def upload_text(file: UploadFile = File(...)):
    file_path = os.path.join(user_dir, UPLOAD_DIR, file.filename)
    
    contents = await file.read()
    with open(file_path, "wb") as f:
        f.write(contents)
    
    return JSONResponse(content={"message": "Text uploaded successfully"}, status_code=200)
