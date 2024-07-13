# if we want to use any of the built in python module
# then we have to import them inside our program and use it
# command line argument is always of string type

import sys

print(sys.argv)# print list of arguments

for value in sys.argv: 
    print(value)

print(len(sys.argv) - 1)# nak list semua arguments and -1 sebab nak buang cmdarguments.py tu

# we want to perform and addition of all the arguments
total = 0
for value in sys.argv[1:]: # we just wanna print out value of index 1 to last
    total = total + int(value)

print("Total: ", total)

#Parsing
