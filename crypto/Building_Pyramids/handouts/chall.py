from math import sin
from Crypto.Util.number import getRandomInteger
from Crypto.Cipher import AES
from hashlib import sha256
from Crypto.Util.Padding import pad
Flag = b"REDACTED"
x = getRandomInteger(1024)

key = float(str(sin(x) + 1)[:6])


def encrypt_flag(flag, key=key):
    key = sha256(str(key).encode()).digest() [:16]
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(flag)


with open("out.txt", "w") as f:
    f.write(str(encrypt_flag(pad(Flag, 16))))
