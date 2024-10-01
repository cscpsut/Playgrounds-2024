import random
# passwd = "Wubba_Lubba_dub_dub"
passwd = "Wubba_Lubba_dub_dub"
starting = 0x1a
ifs = []
hex_val = []

# for i, c in enumerate(passwd):
#     s = f"if (password[{i}] != ({hex(starting + i)} ^ {hex((starting + i) ^ ord(c))}) ) " + "{ correct = 0; }"
#     # print(s)
#     ifs.append(s)

for i, c in enumerate(passwd):
    s = f"if ( (password[{i}] ^ hex_val{i}) != {hex(starting + i)} )" + "{ correct = 0; }"
    # print(s)
    ifs.append(s)
    hex_val.append(hex((starting + i) ^ ord(c)))


print(hex_val)

random.shuffle(ifs)
for i in ifs:
    print(i)
    
    
