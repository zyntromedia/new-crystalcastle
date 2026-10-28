from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from background_worker import router as worker_router
import uvicorn

app = FastAPI(
    title="ZyntroAI Background Worker API",
    version="1.0.0",
    docs_url="/",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(worker_router)

@app.get("/v1/status")
async def health():
    return {
        "ok": True,
        "timestamp": __import__("datetime").datetime.utcnow().isoformat() + "Z",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8787, reload=True)
