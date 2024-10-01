Import the file into VBA editor inside excel

After deobfuscating the script and some analysis you'll see what each cell should contain
Which is:

D12: "_r"
H20: "_n"
I27: "e_"
X33: "_p"
Z43: "e_"
J71: "ht"
A89: ":)"
L91: "ig"
Y99: "ve"
Q101: "fl"
M152: "ow"
T199: "th"
T239: "gi"
F267: "ls"
Y303: "_m"
B339: "ag"

From there you can either fill them manually or using a VBA script 

After running the solver macro run the one given in the challenge anth the flag will be displayed in base64 format, you might not be able to extract the text from the message box but you can edit the macro to assign the string to another celll so you can copy it from there.

