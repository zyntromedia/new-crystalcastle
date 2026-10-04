from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session

from app.database import get_db
from . import schemas, service
from .utils import validate_image, generate_safe_filename, process_and_save_image, delete_old_avatar

router = APIRouter(
    prefix="/profile",
    tags=["👤 Profile"],
    responses={404: {"description": "ไม่พบทรัพยากร"}}
)


# === (เก็บ endpoints เดิมไว้ที่นี่: GET, POST, PATCH) ===


@router.post("/avatar", response_model=schemas.ProfileResponse)
async def upload_avatar(
    user_id: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """📸 อัปโหลดรูปโปรไฟล์
    - รองรับ: JPG, PNG, WebP
    - ขนาดสูงสุด: 2 MB
    - ปรับเป็น 256×256 อัตโนมัติ
    """
    # 1. ตรวจสอบว่ามีโปรไฟล์
    profile = service.get_profile(db, user_id)
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ไม่พบโปรไฟล์: {user_id}"
        )

    # 2. ตรวจสอบไฟล์
    validate_image(file)

    # 3. ตรวจสอบขนาด
    contents = await file.read()
    if len(contents) > 2 * 1024 * 1024:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="ไฟล์ใหญ่เกิน — จำกัด 2 MB"
        )
    await file.seek(0)  # ย้ายตัวชี้กลับไปต้นไฟล์

    # 4. ลบรูปเก่า
    delete_old_avatar(profile.avatar_url)

    # 5. บันทึกรูปใหม่
    filename = generate_safe_filename(user_id, file.content_type)
    avatar_url = process_and_save_image(file, filename)

    # 6. อัปเดตในฐานข้อมูล
    updated = service.update_profile(db, user_id, schemas.ProfileUpdate(avatar_url=avatar_url))
    return updated
