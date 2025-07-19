# Use a slim Python base for lightweight builds
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency list and install required packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire backend folder, including main.py
COPY backend/ ./backend/

# Expose port used by FastAPI
EXPOSE 80

# Start FastAPI app from backend.main module
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "80"]
