from Crypto.Util.number import *
from sympy.ntheory import sqrt_mod
from sympy.ntheory.modular import crt
import json
import os

flag = os.environ.get('FLAG')
flag = flag.encode()

menu = "1- [E]ncrypt flag\n2- [S]quare root\n3- [Q]uit\n"

FLAG = bytes_to_long(flag)
p, q = getPrime(512), getPrime(512)
n = p * q
e = 0x10001

def get_flag():
    ct = pow(FLAG, e, n)
    return json.dumps({"ct": hex(ct), "n": n, "e": hex(e)})


def square_root(a):
    roots_p = sqrt_mod(a, p, all_roots = True)
    roots_q = sqrt_mod(a, q, all_roots = True)
    roots = []
    for r1 in roots_p:
        for r2 in roots_q:
            roots.append(hex(crt([p, q], [r1, r2])[0]))
    return roots

def main():
    while True:
        try:
            print(menu)
            option = input("> ").lower()
            if option == "e":
                ct = get_flag()
                print(f"ct: {ct}")
            elif option == "s":
                a = int(input("a (hex)= > "), 16)
                print(f"roots: {square_root(a)}")
            elif option == "q":
                break
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")
            continue





if __name__ == '__main__':
    main()