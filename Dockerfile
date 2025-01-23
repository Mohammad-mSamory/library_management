# Use the official Python image from Docker Hub
FROM python:3.13-alpine

# Update and install system dependencies
RUN apk add --no-cache libpq-dev gcc musl-dev

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "app.web.main:app", "--host", "0.0.0.0", "--port", "8000"]
