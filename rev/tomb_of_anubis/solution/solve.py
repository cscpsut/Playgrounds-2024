def reverse_rtr(a):
    """Reverse the right rotation by 1 bit."""
    return ((a << 1) & 0xFF) | (a >> 7)

def reverse_eor(a):
    """Reverse the XOR with 0x07."""
    return a ^ 0x07

e = [0x18, 0x6f, 0x98, 0x19, 0x58, 0x70, 0xb0, 0x9a, 0x2b, 0xdc, 0x0b, 0x6a, 0x4b, 0xa6, 0x9c, 0x2c, 0x6c, 0x99, 0x58, 0x2c, 0x36, 0x9f, 0x8c, 0x35, 0x66, 0x64, 0x1a]

flag = ""
flag += chr(reverse_eor(reverse_rtr(e[0])))
flag += chr(reverse_eor(e[1]))
flag += chr(reverse_rtr(e[2]))
flag += chr(reverse_eor(reverse_rtr(e[3])))
flag += chr(reverse_eor(e[4]))
flag += chr(reverse_eor(e[5]))
flag += chr(reverse_rtr(e[6]))
flag += chr(reverse_rtr(e[7]))
flag += chr(reverse_eor(reverse_rtr(reverse_eor(e[8]))))
flag += chr(reverse_rtr(reverse_eor(reverse_rtr(reverse_eor(e[9])))))
flag += chr(reverse_eor(reverse_rtr(reverse_rtr(reverse_rtr(e[10])))))
flag += chr(reverse_eor(reverse_eor(reverse_eor(e[11]))))
flag += chr(reverse_rtr(reverse_rtr(reverse_eor(e[12]))))
flag += chr(reverse_rtr(reverse_rtr(reverse_rtr(e[13]))))  
flag += chr(reverse_rtr(reverse_eor(reverse_eor(reverse_eor(e[14])))))
flag += chr(reverse_rtr(reverse_rtr(reverse_rtr(e[15]))))
flag += chr(reverse_eor(e[16]))
flag += chr(reverse_rtr(e[17]))
flag += chr(reverse_eor(reverse_eor(reverse_eor(e[18]))))
flag += chr(reverse_rtr(reverse_rtr(reverse_rtr(e[19]))))
flag += chr(reverse_eor(e[20]))
flag += chr(reverse_rtr(reverse_rtr(reverse_eor(e[21]))))
flag += chr(reverse_rtr(reverse_rtr(e[22])))
flag += chr(reverse_eor(reverse_rtr(reverse_eor(e[23]))))
flag += chr(reverse_rtr(reverse_rtr(reverse_rtr(e[24]))))      
flag += chr(reverse_eor(reverse_eor(e[25])))
flag += chr(reverse_rtr(e[26]))

print("PlaygroundsCTF{" + flag + "}")