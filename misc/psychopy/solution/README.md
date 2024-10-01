Create an empty dictionary {} and use a variable name as the key. This will cause a KeyError and print the flag.

so the full payload with the error will be like this: 

```python
{}[flag]
Traceback (most recent call last):
  File "chall.py", line 4, in <module>
    eval(''.join([_ for _ in input()[:8] if _ in string.printable]))
  File "<string>", line 1, in <module>
KeyError: 'PlayGroundCTF{redacted}'
```

Now we can see the flag.