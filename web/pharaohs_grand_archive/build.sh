#!/bin/bash

docker rm -f the_pharaohs_scrolls
docker rmi -f the_pharaohs_scrolls
docker build -t the_pharaohs_scrolls . 
docker run -p 1337:1337 -it  -e FLAG=PlaygroundsCTF{FAKE_FALG_FOR_TESTING} the_pharaohs_scrolls