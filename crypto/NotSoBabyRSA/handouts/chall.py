from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long
from random import randint

FLAG = b"REDACTED"
key = RSA.generate(2048)
n = key.n
e = key.e
p = key.p
q = key.q
phi = (p-1)*(q-1)
coeff = randint(1,2**1024)

ct = pow(bytes_to_long(FLAG), e, n)

with open("out.txt", "w") as f:
    f.write(f"e = {e}\n")
    f.write(f"phi = {phi}\n")
    f.write(f"ct = {ct}\n")
    f.write(f"hint = {coeff * phi + p}\n")
 
