# write your code with explanation.
from Crypto.Cipher import AES
from hashlib import sha256
from Crypto.Util.Padding import unpad

ct = b'\xd9\xa1:m\xad\x02\xd9j\x04\n_h\x81}\r\x8e\xe1\xc4}\x86\xad1\x83\xad\xbaPo\xaa\x9e\xd6\x03n\x8ek\xa1\xea3\xdf\xf4\xe5\xc9\xc8\t\x04\xc7\xc2\xe6\xdbT\xbdTq\x0ed\x08F\xf8\xcc6&\x03\xc0\xc0\xb1'

def decrypt_flag(ciphertext, key):
    key = sha256(str(key).encode()).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)
from numpy import arange

for i in arange(0, 2, 0.0001):
    key = i.round(4)
    if b"Play" in decrypt_flag(ct, key):
        print(unpad(decrypt_flag(ct, key),16).decode())
        break