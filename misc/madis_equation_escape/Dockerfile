FROM python:3.10-slim
# Install dependencies
RUN apt update -y && apt install -y socat 

# Make a directory for the challenge
RUN mkdir /chall
WORKDIR /chall

# Copy binary file
COPY source/chall.py .

# Prefered not to edit the below lines
EXPOSE 1337
CMD ["socat", "-dd", "TCP-LISTEN:1337,reuseaddr,fork", "exec:python /chall/chall.py"]