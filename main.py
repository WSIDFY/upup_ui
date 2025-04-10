from fastapi import FastAPI, UploadFile, File, Form, Depends, HTTPException
import os
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, UploadedFile
from extract_text import extract_text
from gpt_generator import generate_quiz_from_text
from routers import quiz_submit


app = FastAPI()

app.include_router(quiz_submit.router)


# 테이블 자동 생성 (처음 1회만 실행됨)
Base.metadata.create_all(bind=engine)

# 파일 저장 경로
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# DB 세션 의존성 주입
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload/")
async def upload_file(
    lecture_name: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

  # 1. 파일 저장
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # 2. 텍스트 추출
    extracted = extract_text(file_path)

    # 3. DB 저장
    db_file = UploadedFile(
        filename=file.filename,
        lecture_name=lecture_name,
        extracted_text=extracted
    )
    db.add(db_file)
    db.commit()
    db.refresh(db_file)

    # 4. 응답
    return {
        "file_id": db_file.id,
        "message": "파일 업로드 및 텍스트 저장 완료!"
    }


@app.get("/generate-quiz/{file_id}")
def generate_quiz(file_id: int, db: Session = Depends(get_db)):
    file = db.query(UploadedFile).filter(UploadedFile.id == file_id).first()
    if not file:
        raise HTTPException(status_code=404, detail="파일을 찾을 수 없습니다.")

    if not file.extracted_text:
        raise HTTPException(status_code=400, detail="텍스트가 없습니다.")

    quiz = generate_quiz_from_text(file.extracted_text)

    return {"quiz": quiz}


