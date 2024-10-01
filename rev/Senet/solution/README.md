Running the program with ltrace or gdb will show strcmp being used (this is also apparent in the decompiled code), if the strings match you'll win the game.

So to win we need to figure out what the program is comparing to match it and get the flag.

We can also see a function named sha1_hash so we know something is being hashed using the sha1 hashing algorithm. Further analysis shows that the game is hashing a string and comparing it with a known hash. 

The game gives the player 3 options: L, R, F
It will store the options chosen by the player in a string, hash it and thenn compare it with 5366dcb274410ad1613ee90d3b568af34b3ba90e

Since there are 9 moves to be made the string will be of length 9, to figure out the sequence, we can generate all possible combinations of L, R, F hash them and compare it to the hash we have, this can be done using a python script.

After executing the script we get the winning sequence of moves which is RFFLRLLFF