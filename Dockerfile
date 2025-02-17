# Use Python 3.10 as base image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . .

# Make start script executable
RUN chmod +x start.sh

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose a port (Railway assigns it dynamically)
EXPOSE 8000

# Run the application using the shell script
CMD ["./start.sh"]