#!/bin/bash
sudo docker rm -f dora
sudo docker rmi -f dora
sudo docker build -t dora .
sudo docker run -it -p 1337:1337 --name dora dora