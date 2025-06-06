from fastapi import FastAPI
# from app.routers import auth_router, config_router

app = FastAPI()

# app.include_router(auth_router.router, prefix="/api/auth", tags=["Auth"])
# app.include_router(config_router.router, prefix="/api/config", tags=["Config"])

@app.get("/")
def root():
    return {"message": "MMM FastAPI backend running"}