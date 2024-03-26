from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/upload/image/")
async def upload_image(file: UploadFile = File(...)):
    # 保存上传的图片文件
    contents = await file.read()
    with open(file.filename, "wb") as f:
        f.write(contents)
    
    return JSONResponse(content={"message": "Image uploaded successfully"}, status_code=200)

@app.post("/upload/video/")
async def upload_video(file: UploadFile = File(...)):
    # 保存上传的视频文件
    contents = await file.read()
    with open(file.filename, "wb") as f:
        f.write(contents)
    
    return JSONResponse(content={"message": "Video uploaded successfully"}, status_code=200)

@app.post("/upload/text/")
async def upload_text(file: UploadFile = File(...)):
    # 保存上传的文本文件
    contents = await file.read()
    with open(file.filename, "wb") as f:
        f.write(contents)
    
    return JSONResponse(content={"message": "Text uploaded successfully"}, status_code=200)
