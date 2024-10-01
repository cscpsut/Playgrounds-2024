#!/bin/bash
sudo docker rm -f senet
sudo docker rmi -f senet
sudo docker build -t senet .
sudo docker run -p 1337:1337 -e FLAG=PlaygroundsCTF{FAKE_FLAG_FOR_TESTING} senet
