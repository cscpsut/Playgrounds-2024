#!/bin/bash

sudo docker rm -f test_kila
sudo docker rmi -f test_kila
sudo docker build -t test_kila .
sudo docker run -p 1337:1337 test_kila