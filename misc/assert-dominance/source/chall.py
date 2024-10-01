import os 
import sys

x = input("Enter secret: ").strip()
try:
	assert(x == open("/root/password", 'r').read())
except :
	print("GET OUT!!!!!!")
	exit()

print("Welcome admin")
os.system('/bin/bash')


