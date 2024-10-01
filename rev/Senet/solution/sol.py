import hashlib
import itertools


target_hash = "5366dcb274410ad1613ee90d3b568af34b3ba90e"


characters = ['R', 'L', 'F']


for combination in itertools.product(characters, repeat=9):
    combination_str = ''.join(combination)
    combination_hash = hashlib.sha1(combination_str.encode()).hexdigest()

    if combination_hash == target_hash:
        print(combination_str) # RFFLRLLFF
        break
