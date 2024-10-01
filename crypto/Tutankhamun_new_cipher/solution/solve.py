from Crypto.Util.number import *
from pwn import *
context.log_level = 'DEBUG'


r = process(['python3', './Tutankhamun_new_cipher.py'])


r.recvuntil("choice: ")
r.sendline("1")
n1 = int(r.recvline().strip())
r.recvuntil("choice: ")
r.sendline("1")
n2 = int(r.recvline().strip())

r.close()


flag = long_to_bytes(GCD(n1, n2))
print(flag)