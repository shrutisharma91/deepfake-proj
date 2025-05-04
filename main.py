from fastapi import FastAPI
from routers.predict_router import router as predict_router

app = FastAPI()

# Root endpoint for testing
@app.get("/")
def read_root():
    return {"status": "API is running", "endpoints": ["/predict"]}

# Include the predict router
app.include_router(predict_router)