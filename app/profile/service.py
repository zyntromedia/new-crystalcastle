from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def get_profile(db: Session, user_id: str):
    """ดึงข้อมูลโปรไฟล์ตามรหัสผู้ใช้"""
    return db.query(models.Profile).filter(models.Profile.user_id == user_id).first()

def create_profile(db: Session, data: schemas.ProfileCreate):
    """สร้างโปรไฟล์ใหม่"""
    db_obj = models.Profile(**data.model_dump(exclude_unset=True))
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_profile(db: Session, user_id: str, data: schemas.ProfileUpdate):
    """แก้ไขข้อมูลโปรไฟล์ — อัปเดตเฉพาะฟิลด์ที่ส่งมา"""
    obj = get_profile(db, user_id)
    if not obj:
        return None
    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(obj, field, value)
    obj.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(obj)
    return obj
