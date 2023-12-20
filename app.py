from fastapi import FastAPI
import tensorflow as tf
from pydantic import BaseModel

# Define the input model
class InputData(BaseModel):
    protein: float
    fat: float
    carbohydrate: float

# Load the TensorFlow model
model = tf.saved_model.load("/content/drive/MyDrive/Model")

# Initialize FastAPI
app = FastAPI()

# Define API endpoint
@app.post("/predict/")
async def predict(data: InputData):
    input_data = [[data.protein, data.fat, data.carbohydrate]]
    prediction = model.predict(tf.constant(input_data, dtype=tf.float32))
    return {"calories": prediction[0][0]}
