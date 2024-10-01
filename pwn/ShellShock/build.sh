#!/bin/bash
sudo docker rm -f shellschok
sudo docker rmi -f shellschok
sudo docker build -t shellschok .
sudo docker run -it -p 1337:1337 --name shellschok shellschok
