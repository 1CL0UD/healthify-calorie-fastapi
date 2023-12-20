# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the FastAPI app code into the container
COPY ./app /app

# Install dependencies
RUN pip install fastapi uvicorn tensorflow

# Expose the port your FastAPI app runs on
EXPOSE 8000

# Command to run the FastAPI app using Uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
