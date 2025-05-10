# Start from an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Make port 8000 available to the world outside this container
# This is the port Gunicorn will run on within the container
EXPOSE 8000

# Define environment variable for Gunicorn (optional, but good practice)
ENV FLASK_APP app:app
ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:8000"

# Run app.py when the container launches
# CMD ["python", "app.py"] # This would use Flask's dev server

# Use Gunicorn for a production-ready server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
