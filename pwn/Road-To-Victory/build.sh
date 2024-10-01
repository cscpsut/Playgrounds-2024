#!/bin/bash
sudo docker rm -f victory
sudo docker rmi -f victory
sudo docker build -t victory .
sudo docker run -it -p 1337:1337 --name victory victory

