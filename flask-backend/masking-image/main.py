from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import os
import shutil
from utils import get_dominant_color, replace_color_with_hex_list, replace_color_with_texture

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Mengonfigurasi CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://masking-image.vercel.app"],  # Izinkan permintaan dari localhost:3000
    allow_credentials=True,
    allow_methods=["*"],  # Izinkan semua metode (GET, POST, dll.)
    allow_headers=["*"],  # Izinkan semua header
)


# Folder penyimpanan
UPLOAD_DIR = "uploads"
RESULT_DIR = "static/results"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)

# Mount file statis
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.post("/replace-color/")
async def replace_color_endpoint(
    image: UploadFile = File(...),
    target_color: str = Form(...),
    hex_list_file: UploadFile = File(...),
    tolerance: int = Form(30)
):
    
     
    # Simpan file sementara
    image_path = os.path.join(UPLOAD_DIR, image.filename)
    hex_path = os.path.join(UPLOAD_DIR, hex_list_file.filename)

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    with open(hex_path, "wb") as buffer:
        shutil.copyfileobj(hex_list_file.file, buffer)

    result_paths = replace_color_with_hex_list(
        image_path, target_color, hex_path, RESULT_DIR, tolerance=tolerance
    )

    # Kembalikan path hasil (bisa digunakan di frontend)
    return JSONResponse({"result_images": result_paths})


@app.post("/replace-with-texture/")
async def replace_with_texture_endpoint(
    image: UploadFile = File(...),
    texture: UploadFile = File(...),
    target_color: str = Form(...),
    tolerance: int = Form(30)
):
    image_path = os.path.join(UPLOAD_DIR, image.filename)
    texture_path = os.path.join(UPLOAD_DIR, texture.filename)

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    with open(texture_path, "wb") as buffer:
        shutil.copyfileobj(texture.file, buffer)

    result_path = replace_color_with_texture(
        image_path, texture_path, target_color, RESULT_DIR, tolerance=tolerance
    )

    return FileResponse(result_path, media_type="image/png")

@app.post("/detect-dominant-color/")
async def detect_dominant_color(image: UploadFile = File(...)):
    # Simpan file sementara
    image_path = os.path.join(UPLOAD_DIR, image.filename)
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    # Dapatkan warna dominan dari gambar
    dominant_color = get_dominant_color(image_path, n_clusters=3)  # 3 cluster default

    # Kembalikan warna dominan dalam format hexadecimal
    return JSONResponse({"dominant_color": dominant_color})
