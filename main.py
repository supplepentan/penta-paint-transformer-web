# 必要なモジュールを読み込む
from fastapi import FastAPI, UploadFile, Form, Body
from fastapi.staticfiles import StaticFiles
import tempfile
from PIL import Image
import subprocess
import os
import zipfile
import shutil
from fastapi.params import File

import uvicorn
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.responses import FileResponse
from io import BytesIO

from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title='さぷりぺんたんの油絵AI',
    description='油絵みたいのが作成できるよ',
    version='1.0')

#: Configure CORS
origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="./front/dist/static"), name="static")
templates = Jinja2Templates(directory="./front/dist/")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse('index.html',
                                      {'request': request})

@app.post("/upload")
async def index(file: UploadFile = File(...)):
    print(file)
    contents = await file.read()
    #im = Image.open(BytesIO(contents))
    image = Image.open(BytesIO(contents)).convert('RGB')
    image.save('input/input.jpg')
    if not os.path.exists("./front/dist/img_res"):
        os.mkdir("./front/dist/img_res")
    subprocess.run(["python", "run.py"])

    return {"msg":"Finished"}
if __name__ == "__main__":
    uvicorn.main(app=app)
