# Use a small official Python image as the base
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy only requirements first, to install them early and cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Expose port 8000 for the API
EXPOSE 8000

# Run the FastAPI app using Uvicorn
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
