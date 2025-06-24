#1. Prepration stage
FROM python:3.10-slim AS builder

# Set working directory
WORKDIR /app

# Environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install pip and Python dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install system-level build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*


# 2. Production stage
FROM python:3.10-slim

# Set environment variables again
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy Python packages and binaries from builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Install required system packages for runtime
RUN apt-get update && apt-get install -y \
    nginx \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

# Copy your Django project code
COPY . .

# Copy env file
COPY NoteMagnet/.env /app/.env

# Copy and configure Supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Copy nginx config to correct location
COPY nginx.conf /etc/nginx/nginx.conf

# Ensure entrypoint is executable (used by gunicorn program in supervisor)
RUN chmod +x /app/entrypoint.prod.sh

# Create folders if not present
RUN mkdir -p /static /media

# Expose port 80 (used by nginx)
EXPOSE 80

# Start all processes using Supervisor
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
