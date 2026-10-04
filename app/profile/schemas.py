from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProfileBase(BaseModel):
    display_name: str = Field(..., min_length=2, max_length=50, description="ชื่อที่แสดง")
    bio: Optional[str] = Field(None, max_length=500, description="ประวัติย่อ")
    avatar_url: Optional[str] = Field(None, max_length=500, description="ลิงก์รูปประจำตัว")

class ProfileCreate(ProfileBase):
    user_id: str = Field(..., description="รหัสผู้ใช้จากระบบ")

class ProfileUpdate(BaseModel):
    display_name: Optional[str] = Field(None, min_length=2, max_length=50)
    bio: Optional[str] = Field(None, max_length=500)
    avatar_url: Optional[str] = None

class ProfileResponse(ProfileBase):
    user_id: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
