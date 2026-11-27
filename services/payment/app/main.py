from fastapi import FastAPI

app = FastAPI(title="payment Service", version="0.1.0")

@app.get("/health", tags=["health"])
def health():
    return {"success": True, "code": "OK", "message": "service is healthy", "data": {"service": "payment", "database": "payment_db"}}
