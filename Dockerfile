# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set environment variables to prevent Python from buffering output
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app



# Expose port 8080 for the server
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]
