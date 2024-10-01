FROM python:3.10-slim

# Make a directory for the challenge
RUN mkdir /chal
WORKDIR /chal

# Copy chall file
COPY  ./source/q.py /chal/


EXPOSE 1337
COPY ./ynetd .
COPY ./entrypoint.sh .
RUN chmod +x ./entrypoint.sh && chmod +x ./ynetd
ENTRYPOINT ["/chal/entrypoint.sh"]

