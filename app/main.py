from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles  # ✅ เพิ่ม
from app.profile.routes import router as profile_router

app = FastAPI(
    title="ZyntroAI New-Crystalcastle",
    version="1.0.0",
    description="แพลตฟอร์ม AI & Collaboration"
)

# ✅ ให้เข้าถึงรูปผ่าน URL ได้
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Router
app.include_router(profile_router)


@app.get("/health", tags=["System"])
def health_check():
    return {"status": "ok", "service": "new-crystalcastle"}
