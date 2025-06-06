from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import os, uuid

from app_server.core.database import get_db
from app_server.models.file import UploadedFile
from app_server.services.file_service import extract_text

UPLOAD_DIR = "app_server/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

router = APIRouter()

@router.post("/upload/")
async def upload_file(
    lecture_name: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    unique_filename = f"{uuid.uuid4().hex}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    extracted = extract_text(file_path)
    if not extracted:
        raise HTTPException(status_code=400, detail="텍스트 추출 실패")

    db_file = UploadedFile(
        filename=unique_filename,
        lecture_name=lecture_name,
        extracted_text=extracted
    )
    db.add(db_file)
    db.commit()
    db.refresh(db_file)

    return {
        "file_id": db_file.id,
        "filename": unique_filename,
        "text": extracted,
        "message": "업로드 및 저장 완료"
    }

@router.get("/file/{filename}")
async def get_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="파일이 존재하지 않습니다")
    return FileResponse(file_path)