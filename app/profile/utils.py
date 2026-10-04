"""
🛠️ Avatar Utilities — ตรวจสอบ + ปรับขนาด + ตั้งชื่อ
"""
import uuid
from pathlib import Path
from PIL import Image
from fastapi import UploadFile, HTTPException, status
from .config import (
    AVATAR_UPLOAD_DIR, ALLOWED_MIME_TYPES,
    MAX_FILE_SIZE, AVATAR_SIZE, AVATAR_BASE_URL
)


def validate_image(file: UploadFile) -> None:
    """ตรวจสอบประเภทและขนาดไฟล์"""
    # ตรวจสอบประเภท
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"ประเภทไฟล์ไม่รองรับ — ยอมรับ: {', '.join(ALLOWED_MIME_TYPES.keys())}"
        )

    # ตรวจสอบนามสกุล
    ext = Path(file.filename).suffix.lower()
    if ext not in {".jpg", ".jpeg", ".png", ".webp"}:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="นามสกุลไฟล์ไม่ถูกต้อง"
        )


def generate_safe_filename(user_id: str, content_type: str) -> str:
    """สร้างชื่อไฟล์แบบสุ่ม ป้องกันการโจมตี"""
    ext = ALLOWED_MIME_TYPES[content_type]
    random_str = uuid.uuid4().hex[:12]  # สุ่ม 12 ตัวอักษร
    return f"{user_id}_{random_str}{ext}"


def process_and_save_image(file: UploadFile, filename: str) -> str:
    """ปรับขนาดรูปและบันทึก → คืน URL เข้าถึง"""
    path = AVATAR_UPLOAD_DIR / filename

    # อ่านและประมวลผล
    with Image.open(file.file) as img:
        # แปลงเป็น RGB ถ้าเป็นภาพโปร่งแสง
        if img.mode in ("RGBA", "P"):
            background = Image.new("RGB", img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
            img = background

        # ปรับขนาดคงสัดส่วน
        img.thumbnail(AVATAR_SIZE, Image.Resampling.LANCZOS)

        # สร้างภาพขนาดตรงตามเป้าหมาย (จัดกึ่งกลาง)
        output = Image.new("RGB", AVATAR_SIZE, (255, 255, 255))
        paste_x = (AVATAR_SIZE[0] - img.width) // 2
        paste_y = (AVATAR_SIZE[1] - img.height) // 2
        output.paste(img, (paste_x, paste_y))

        # บันทึก
        output.save(path, quality=85, optimize=True)

    return f"{AVATAR_BASE_URL}{filename}"


def delete_old_avatar(url: str | None) -> None:
    """ลบรูปเก่าเมื่ออัปโหลดใหม่"""
    if not url or not url.startswith(AVATAR_BASE_URL):
        return
    filename = url.replace(AVATAR_BASE_URL, "")
    path = AVATAR_UPLOAD_DIR / filename
    if path.exists():
        path.unlink()
