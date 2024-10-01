#!/bin/bash

ALLOWED="^[-A-Za-z0-9]{0,3}$"

if [[ $# == 2 && "$1" == "/usr/local/bin/python3" && "$2" == "/home/player/chall.py" ]]; then
  exec "$@"
elif [[ $# == 3 && "$1" == "/usr/local/bin/python3" && "$2" =~ $ALLOWED && "$3" == "/home/player/chall.py" ]]; then
  exec "$@"
else
  echo "Invalid command"
  exit 1
fi
