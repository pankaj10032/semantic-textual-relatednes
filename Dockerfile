# Use the official Python image as a base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container at /app/
# COPY requirements.txt /app/

COPY requirements.txt .
# Install Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt

RUN pip install -r requirements.txt

# Copy the Flask app code into the container
COPY . /app/ 
# copy all the thing to the app folder

# Expose the port on which the Flask app will run
EXPOSE 5002

# Command to run the Flask application
CMD ["python", "app.py"]
