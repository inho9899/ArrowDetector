# main.py
from fastapi import FastAPI, UploadFile, File
from model import get_answer
from PIL import Image
import io

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # 이미지 열기
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    # 예측 실행
    final_res, count_rotate, total = get_answer(image)

    return {
        "result": final_res,
        "rotate_count": count_rotate,
        "details": total
    }
