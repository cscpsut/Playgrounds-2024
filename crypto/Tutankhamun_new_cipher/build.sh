#!/bin/bash

# sudo docker rm -f tutankhamun_new_cipher
# sudo docker rmi -f tutankhamun_new_cipher
sudo docker build -t tutankhamun_new_cipher .
sudo docker run -p 1337:1337 -e FLAG=PlaygroundsCTF{FAKE_FLAG_FOR_TESTING} tutankhamun_new_cipher