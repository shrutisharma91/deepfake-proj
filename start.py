import os
import uvicorn

if __name__ == "__main__":
    # Get port from environment variable or use 10000 (Render's default)
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)