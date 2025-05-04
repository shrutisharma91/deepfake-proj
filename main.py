from fastapi import FastAPI
from routers.predict_router import router as predict_router
import os

app = FastAPI()

# Root endpoint for testing
@app.get("/")
def read_root():
    return {"status": "API is running", "endpoints": ["/predict"]}

# Health check endpoint specifically for Render
@app.get("/health")
def health_check():
    return {"status": "healthy", "port": os.environ.get("PORT", 10000)}

# Include the predict router
app.include_router(predict_router)

# For local development
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)