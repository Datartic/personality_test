# Use the official Python image from the DockerHub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 for the app
EXPOSE 8080

# Run the application using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
