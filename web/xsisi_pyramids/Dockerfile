# Stage 1: Build Node.js application
FROM node:alpine AS node-build

WORKDIR /app/bot
COPY ./source/bot /app/bot

# Install dependencies
RUN npm install

# Stage 2: Build Python application
FROM python:3-alpine

# Install necessary packages
RUN apk update && apk add --no-cache \
    supervisor \
    chromium \
    nodejs \
    npm \
    && rm -rf /var/cache/apk/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy Python application source code
COPY ./source /app

# Copy Node.js application from the previous stage
COPY --from=node-build /app/bot /app/bot

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Setup supervisor
RUN mkdir -p /var/log/supervisor /var/run/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose the necessary port
EXPOSE 80

# Start both applications using supervisor
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]