FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY backend/ .

# Create generated directory
RUN mkdir -p /app/generated

# Expose port
EXPOSE 8000

# Default command
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
