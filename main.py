import os
from fastapi import FastAPI
import tensorflow as tf
from pydantic import BaseModel
import uvicorn

# Define the input model
class InputData(BaseModel):
    protein: float
    fat: float
    carbohydrate: float

# Load the TensorFlow model
model = tf.keras.models.load_model("model/")

# Initialize FastAPI
app = FastAPI()

# Define API endpoint
@app.post("/predict")
async def predict(data: InputData):
    input_data = [[data.protein, data.fat, data.carbohydrate]]
    prediction = model.predict(input_data)
    prediction_value = float(prediction[0][0])  # Assuming prediction is a 2D array
    return {"calories": prediction_value}

@app.get("/")
def index():
    return f"Hello World"

@app.get("/test")
def index():
    return f"Hello test"

# Check the type and attributes of the loaded model
print(type(model))  # Check the type of the loaded model

# Print all attributes/methods of the loaded model
print(dir(model))

port = os.environ.get("PORT", 8000)
print(f"Listening to http://0.0.0.0:{port}/test")
uvicorn.run(app, host='0.0.0.0',port=port)

