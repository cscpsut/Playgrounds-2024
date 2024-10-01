#!/bin/bash
sudo docker rm -f nile
sudo docker rmi -f nile
sudo docker build -t nile .
sudo docker run -p 1337:1337 nile
