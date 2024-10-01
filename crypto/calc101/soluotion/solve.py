# write your code with explanation.
from pwn import * 
from Crypto.Cipher import AES
from hashlib import sha256
from Crypto.Util.Padding import unpad
r = process(["python3", "chall.py"])

r.recvuntil(b"integer: ")

r.sendline(b"10000")

r.recvuntil(b"text: ")


ct = r.recvline().strip()
r.close()

ct = bytes.fromhex(ct.decode())

def decrypt(ct, k):

    key = sha256(k).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ct)

    
pt = decrypt(ct, str(0).encode())
print(unpad(pt, 16).decode())