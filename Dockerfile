# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Run the ETL script
CMD ["python", "etl_script.py"]
