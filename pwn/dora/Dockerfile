FROM ubuntu:24.04
# Install dependencies
RUN apt update -y && apt install g++ libssl-dev build-essential -y

# Make a directory for the challenge
RUN mkdir /dora
WORKDIR /dora

# Copy binary file
COPY source/. .

# Prefered not to edit the below lines
EXPOSE 1337
COPY ynetd .
RUN chmod +x ynetd
RUN chmod +x dora

CMD ["./ynetd", "-p", "1337", "./dora"]