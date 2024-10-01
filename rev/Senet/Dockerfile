FROM ubuntu:24.04
# Install dependencies
RUN apt update -y && apt install -y socat 

# Make a directory for the challenge
RUN mkdir /chal
WORKDIR /chal

# Copy binary file
COPY source/chall .

# Prefered not to edit the below lines
EXPOSE 1337
RUN chmod +x chall
CMD ["socat", "-dd", "TCP-LISTEN:1337,reuseaddr,fork", "exec:/chal/chall"]