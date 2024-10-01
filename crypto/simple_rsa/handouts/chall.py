from Crypto.Util.number import *

Flag = b"REDACTED"

p = getPrime(1024)
q = getPrime(1024)

assert p != q

n = p*q

e = 0x10001

ct = []
for c in Flag:
    ct.append((pow((c), e, n)))

with open("out.txt", "w") as f:
    f.write(f'ct = {str(ct)}\n')
    f.write(f'n = {str(n)}')

