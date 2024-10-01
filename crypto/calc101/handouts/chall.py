import sys
import sympy as sp
from random import randint
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import sha256
import os 

flag = "PlaygroundsCTF{FAKE_FLAG_FOR_TESTING}".encode()

sys.set_int_max_str_digits(1000000)
x = sp.symbols('x')

poly = x**70 - 100*x**8 + 99*x**169 - 100*x**2 + 1


def encrypt(pt, key):
    key = sha256(key).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(pt, 16))

def get_derivative(n,inp,poly=poly):
    for i in range(n):
        poly = sp.diff(poly)

    return poly.subs(x,inp)

def main():
    randx = randint(1, 2**1024)
    n = abs(int(input("enter a positive integer: ")))
    key = get_derivative(n,randx)
    ct = encrypt(flag, str(key).encode())
    print(f"Here is the ciphertext: {ct.hex()}")    

if __name__ == "__main__":
    main()
