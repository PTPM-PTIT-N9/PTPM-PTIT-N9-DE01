from fastapi import FastAPI

app = FastAPI(title="auth Service", version="0.1.0")

@app.get("/health", tags=["health"])
def health():
    return {"success": True, "code": "OK", "message": "service is healthy", "data": {"service": "auth", "database": "auth_db"}}
