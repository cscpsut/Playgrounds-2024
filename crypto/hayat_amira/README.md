# حياة اميرة

## Description

Cleopatra suspects that ceaser has been talking to a few other "pharaohs", can you help her find out what he was telling them.

## Solution

All the messages were XORed with the same key, we know that the messages are all plain text and that the key length is 36, firstly we xor with the flag format to get part of the key, then we continue words within the messages to get more of the key until we find the whole thing.

## Flag

```python
PlaygroundsCTF{Mohamed_Henedi_was_a_player_https://www.youtube.com/watch?v=xdH719gmtEE}
```