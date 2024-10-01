#!/bin/bash
sudo docker rm -f chall
sudo docker rmi -f chall
sudo docker build -t chall .
sudo docker run -it -p 1337:1337 --name chall chall
