#1. Prepration stage
FROM python:3.10-slim AS builder

# Set the working directory
WORKDIR /app

# Set env variables to optimize python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#install dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Install system libraries.
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*




# 2. Production stage
FROM python:3.10-slim

#Copy dependecies from the builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages/  /usr/local/lib/python3.10/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . .

# Set env variables to optimize python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Expose the port
EXPOSE 8000

# Make entry file executable
RUN chmod +x /app/entrypoint.prod.sh

# Start the app using gunicorn
CMD [ "/app/entrypoint.prod.sh" ]