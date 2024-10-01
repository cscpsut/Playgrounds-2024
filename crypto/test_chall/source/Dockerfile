# this is a temp structure 


FROM python:3.9-slim-buster
RUN apt update && \
 apt install -y socat && \
 pip install pycryptodome
# Add application
WORKDIR /app
COPY challenge .
# Expose the port
EXPOSE 1337
# Switch to use a non-root user from here on
USER nobody

# Start the python application
CMD ["socat", "-dd", "TCP-LISTEN:1337,reuseaddr,fork", "exec:python -u /app/server.py"]