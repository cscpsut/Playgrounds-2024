FROM python:3.9-slim

RUN apt-get update && apt-get install -y ncat sudo

RUN useradd -m player

COPY entrypoint.sh /home/player/entrypoint.sh
COPY source/chall.py /home/player/chall.py
COPY source/check.sh /usr/local/bin/check.sh
COPY source/password /root/password
COPY ynetd /home/player/ynetd
RUN chmod 755 /usr/local/bin/check.sh && chmod 700 /home/player/entrypoint.sh && chmod 701 /home/player/ynetd 


RUN echo "player ALL=(ALL) NOPASSWD: /usr/local/bin/check.sh" > /etc/sudoers.d/player

EXPOSE 4444

WORKDIR /home/player/
ENTRYPOINT ["./entrypoint.sh"]
