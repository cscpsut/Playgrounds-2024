# write your code with explanation.
ct = b"myyux?44|||3~tzyzgj3htr4|fyhmD{BpXpNS_pvr9V"

flag = "PlaygroundsCTF{"

for i in ct:
    flag += chr(i  - 5)

flag += "}"

print(flag)
