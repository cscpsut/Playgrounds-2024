FROM python:3.9-slim-buster

# Install necessary packages and Python dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends socat && \
    pip install pycryptodome && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy application files
COPY source/ .   
# COPY socat . 
COPY requirements.txt .
# Install Python requirements
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 1337

USER nobody

# Start the application
CMD ["socat", "-dd", "TCP-LISTEN:1337,reuseaddr,fork", "exec:python -u /app/chall.py"]