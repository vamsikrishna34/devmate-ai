# Use a slim Python base for lightweight builds
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency list and install packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ backend/
RUN touch backend/__init__.py

# Copy main.py from backend folder (since it’s located there)
COPY backend/main.py .

# Expose port used by FastAPI
EXPOSE 80

# Start FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
