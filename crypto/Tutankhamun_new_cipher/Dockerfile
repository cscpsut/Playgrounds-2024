FROM python:3.10-slim

RUN apt update -y && apt install -y socat && \
rm -rf /var/lib/apt/lists/*
# Make a directory for the challenge
RUN mkdir /chall
WORKDIR /chall

# Copy chall file
COPY source .

# Install requirements from requirements.txt
RUN pip install -r requirements.txt

EXPOSE 1337
USER nobody
# ENTRYPOINT ["/chall/entrypoint.sh"]
CMD ["socat", "-dd", "TCP-LISTEN:1337,reuseaddr,fork", "exec:python -u /chall/chall.py"]
