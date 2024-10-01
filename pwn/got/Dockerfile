FROM ubuntu:24.04


RUN apt update -y && apt install g++ libssl-dev build-essential -y


RUN mkdir /got
WORKDIR /got


COPY source/ .
COPY entrypoint.sh .


EXPOSE 1337
COPY ynetd .
RUN chmod +x ynetd got entrypoint.sh 
ENTRYPOINT ["/got/entrypoint.sh"]  
