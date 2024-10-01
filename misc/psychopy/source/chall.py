#!/usr/bin/python3 -S
import string
import os
flag = os.environ.get("FLAG")
eval(''.join([_ for _ in input()[:8] if _ in string.printable]))