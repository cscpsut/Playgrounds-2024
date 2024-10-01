#!/bin/bash
sudo docker rm -f the_break_in
sudo docker rmi -f the_break_in
sudo docker build -t the_break_in .
sudo docker run -p 1337:1337 --rm -e FLAG=PlaygroundsCTF{FAKE_FALG_FOR_TESTING} the_break_in