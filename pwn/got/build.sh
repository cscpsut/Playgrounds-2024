#!/bin/bash
sudo docker rm -f got
sudo docker rmi -f got
sudo docker build -t got .
sudo docker run -it -p 1337:1337 --name got got