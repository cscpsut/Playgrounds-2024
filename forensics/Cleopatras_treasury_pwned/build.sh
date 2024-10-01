#!/bin/bash
sudo docker rm -f pwned
sudo docker rmi -f pwned
sudo docker build -t pwned .
sudo docker run -p 1337:1337 --rm -e FLAG=PlaygroundsCTF{FAKE_FALG_FOR_TESTING} pwned