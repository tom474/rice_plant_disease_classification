# Base Python image with pip, suitable for FastAPI + TensorFlow
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy only requirements first to install dependencies early (cache)
COPY requirements.txt .

# Install system deps and Python packages
RUN apt-get update && \
    apt-get install -y gcc tzdata && \
    ln -fs /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy all backend files
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Set environment variables for TensorFlow
ENV TZ=Asia/Ho_Chi_Minh

# Default command to run FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
