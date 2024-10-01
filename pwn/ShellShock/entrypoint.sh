#!/bin/bash

echo $FLAG > flag.txt
./ynetd -p 1337 ./ShellShock_shell
