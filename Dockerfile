FROM python:3.9-slim
#avoid buffering issues
ENV PYTHONUNBUFFERED=1


WORKDIR /app


COPY . /app

# Install required packages from requirements.txt 
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 to allow external traffic to the container
EXPOSE 80

# Run a custom entrypoint script to show runtime information
ENTRYPOINT ["sh", "-c", "echo 'Starting Order Management System'; echo 'Running on $(hostname) at $(date)'; python cs330_04_1.py"]
