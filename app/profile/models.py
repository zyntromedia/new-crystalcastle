from sqlalchemy import Column, String, Text, DateTime
from datetime import datetime
from app.database import Base

class Profile(Base):
    __tablename__ = "profiles"

    user_id = Column(String(100), primary_key=True, index=True, comment="รหัสผู้ใช้")
    display_name = Column(String(100), nullable=False, comment="ชื่อที่แสดง")
    bio = Column(Text, nullable=True, comment="ประวัติย่อ")
    avatar_url = Column(String(500), nullable=True, comment="รูปประจำตัว")
    created_at = Column(DateTime, default=datetime.utcnow, comment="เวลาสร้าง")
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment="เวลาแก้ไขล่าสุด")
