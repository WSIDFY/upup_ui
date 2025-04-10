from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from database import Base


class UploadedFile(Base):
    __tablename__ = "uploaded_files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255))          # 원래 파일 이름
    lecture_name = Column(String(255))      # 강의명(폴더명)
    extracted_text = Column(Text)           # 추출된 전체 텍스트
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())  # 업로드 시간
