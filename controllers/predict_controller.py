from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np
import os
from io import BytesIO
from model.meso4 import Meso4
from utils.face_extractor import extract_face

# Load the model once here
model = Meso4()
# Get the absolute path to the model file
model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "model", "Meso4_DF.h5")
model.load_weights(model_path)

async def predict_image(file):
    contents = await file.read()
    image = Image.open(BytesIO(contents)).convert("RGB")
    img_array = np.array(image)
   
    face = extract_face(img_array)
    if face is None:
        return JSONResponse(content={"error": "No face detected"}, status_code=400)
   
    face = np.expand_dims(face, axis=0)
    prediction = model.predict(face)[0][0]
    label = "Fake" if prediction > 0.5 else "Real"
   
    return {"label": label, "confidence": float(prediction)}