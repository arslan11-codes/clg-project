# Use the official lightweight Python image.
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . .

# Run the web server
CMD ["python", "main.py"]
