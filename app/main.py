from fastapi import FastAPI
from app.profile.routes import router as profile_router

app = FastAPI(
    title="ZyntroAI New-Crystalcastle",
    version="1.0.0"
)

# ✅ ลงทะเบียนโมดูล
app.include_router(profile_router)
