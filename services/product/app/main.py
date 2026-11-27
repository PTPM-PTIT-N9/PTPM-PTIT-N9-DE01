from fastapi import FastAPI

app = FastAPI(title="product Service", version="0.1.0")

@app.get("/health", tags=["health"])
def health():
    return {"success": True, "code": "OK", "message": "service is healthy", "data": {"service": "product", "database": "product_db"}}
