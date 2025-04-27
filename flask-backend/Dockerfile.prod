# ✅ This will:

#     Use gunicorn instead of flask run
    
#     Proper for production (more stable, better performance)
    
#     No live-reload

# Use the official lightweight Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r requirements.txt

# Copy the whole project
COPY . .

# Expose port 5000 (or whatever your production port is)
EXPOSE 5000

# Command to run Gunicorn WSGI server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
