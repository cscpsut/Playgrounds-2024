FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends socat && \
    rm -rf /var/lib/apt/lists/*

    WORKDIR /chall
COPY ./source/chall.py .

EXPOSE 1337
USER nobody
CMD ["socat", "-dd", "TCP-LISTEN:1337,reuseaddr,fork", "exec:python /chall/chall.py"]