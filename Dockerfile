# Use a slim Python base for lightweight builds
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency list and install packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire backend folder
COPY backend/ ./backend/

# Ensure backend is treated as a Python module
RUN touch backend/__init__.py

# Set PYTHONPATH so Python finds your backend modules
ENV PYTHONPATH=/app

# Start FastAPI app via backend.main
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "80"]

# Open port 80 for traffic
EXPOSE 80
