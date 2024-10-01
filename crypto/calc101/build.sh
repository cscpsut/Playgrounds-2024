#!/bin/bash
sudo docker rm -f calc101
sudo docker rmi -f calc101
sudo docker build -t calc101 .
sudo docker run -p 1337:1337 -e FLAG=PlaygroundsCTF{FAKE_FLAG_FOR_TESTING} calc101
