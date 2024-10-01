FROM ubuntu:latest


# install dependencies
RUN apt update -y && apt install g++ libssl-dev build-essential -y
RUN apt install  build-essential -y
# make a directory for the challenge
RUN mkdir /chal
WORKDIR /chal
COPY source/ShellShock_shell .
COPY ynetd .
COPY entrypoint.sh .
# COPY libc.so.6 /lib/x86_64-linux-gnu/libc.so.6
# COPY ld-linux-x86-64.so.2 /lib64/ld-linux-x86-64.so.2


 
EXPOSE 1337

RUN chmod +x ynetd
RUN chmod +x ShellShock_shell
RUN chmod +x /lib/x86_64-linux-gnu/libc.so.6
RUN chmod +x /lib64/ld-linux-x86-64.so.2 


# add non root user
RUN groupadd -g 10001 user && \
   useradd -u 10000 -g user user \
   && chown -R user:user /chal



# switch to non root user and run the app

RUN chmod +x entrypoint.sh
USER user:user
ENTRYPOINT ["/chal/entrypoint.sh"]
