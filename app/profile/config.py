"""
⚙️ Avatar Upload Configuration
"""
from pathlib import Path

# ที่จัดเก็บรูป
AVATAR_UPLOAD_DIR = Path("uploads/avatars")
AVATAR_UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# ขนาดสูงสุด
MAX_FILE_SIZE = 2 * 1024 * 1024  # 2 MB

# ประเภทที่ยอมรับ
ALLOWED_MIME_TYPES = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp"
}

# ขนาดที่ปรับให้
AVATAR_SIZE = (256, 256)

# URL พื้นฐาน
AVATAR_BASE_URL = "/uploads/avatars/"
