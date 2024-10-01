run this command to decompile the file:

```bash
$ uncompyle6 chall.pyc 
```

then u will get Ciphertext, just xor it with 0xd1. 

```python
flag = [
 129, 189, 176, 168, 182, 163, 190, 164, 191, 181, 162, 146, 133, 151, 
 170, 130, 191, 229, 229, 229, 229, 229, 186, 226, 142, 147, 168, 
 165, 226, 226, 226, 226, 226, 226, 172]

 for i in range(len(flag)):
 	print(chr(flag[i] ^ 0xd1), end='')
```