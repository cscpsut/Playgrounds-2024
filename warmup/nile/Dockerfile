FROM ubuntu:24.04
# Install dependencies
RUN apt update -y && apt install g++ libssl-dev build-essential -y

# Make a directory for the challenge
RUN mkdir /chal
WORKDIR /chal

# Copy binary file
COPY source/chall .


# Prefered not to edit the below lines
EXPOSE 1337
COPY ynetd .
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh ynetd chall
ENTRYPOINT ["/chal/entrypoint.sh"]