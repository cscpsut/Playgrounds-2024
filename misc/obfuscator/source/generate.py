x = "'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[\\]^_`{|}~ \n"

f = "__main__"

for c in f:
    print(f"x[{x.index(c)}]+", end='')