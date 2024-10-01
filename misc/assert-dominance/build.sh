#!/bin/bash
sudo docker rm -f assert-dominance
sudo docker rmi -f assert-dominance
sudo docker build -t assert-dominance .
sudo docker run -it -p 4444:4444 --name assert-dominance assert-dominance
