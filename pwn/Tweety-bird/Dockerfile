FROM ubuntu:24.04


RUN apt update -y && apt install g++ libssl-dev build-essential -y


RUN mkdir /chal
WORKDIR /chal

COPY source/chall .

RUN mkdir glibc
COPY source/glibc/libc.so.6 ./glibc/libc.so.6
COPY source/glibc/ld-linux-x86-64.so.2  ./glibc/ld-linux-x86-64.so.2 
RUN chmod +x ./glibc/libc.so.6 ./glibc/ld-linux-x86-64.so.2


EXPOSE 1337
COPY ynetd .
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
RUN chmod +x ynetd
RUN chmod +x chall
ENTRYPOINT ["/chal/entrypoint.sh"]
