#!/bin/bash
echo $FLAG > /chal/flag.txt
./ynetd -p 1337 "python /chal/q.py"
