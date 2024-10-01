from Crypto.Cipher import AES
import random
from Crypto.Util.Padding import *

cipher = b"\xf1g\xb7\x15c\x1a\xc7\x83\xd3\x9c\x8a\x8b\x11#Z\x97zYfKg\x84\x9d\xb3\xf7\x8e*W\x00D\xce\\ID\xa2\x93\x81\xff\x17\xc4\x88\xb0\xf9\xe4F\x11\xcb\xcd\xd3:\xb2\x8d\xe0\x85x\x14\x89\xde\xa3|N\xd1G\xdb\xd5\xb4d\x9c6\x88\xbeJ\xc7\xee\xcf\xf2>\x8c\xd8s\xc2\xc9\xbc\xcc\x1b\xdd\xbe\x16T'usC\xe1\xb7\x9b"

عشوائي = random.choice
اطبع = print
تهشيم = pad
مصفوفة_اللقمات = bytearray

التشفير_المتقدم_الموحد = AES.new
كتاب_الرموز_الإلكترونية = AES.MODE_ECB

def التشفير(النص, المفتاح):
    return التشفير_المتقدم_الموحد(المفتاح, كتاب_الرموز_الإلكترونية).decrypt(النص)

def بالليل(النص):
    المفتاح = "تعبانننن".encode('utf-8')
    return التشفير(النص, المفتاح)

def بالصبح(النص):
    المفتاح = "زهقانننن".encode('utf-8')
    return التشفير(النص, المفتاح)


def solve(ct, count):
    if count == 12:
        if b"PlaygroundsCTF" in ct:
            print(ct)
        return
    solve(بالليل(ct), count + 1)
    solve(بالصبح(ct), count + 1)
    
    
solve(cipher, 0)