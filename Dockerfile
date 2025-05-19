# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]
