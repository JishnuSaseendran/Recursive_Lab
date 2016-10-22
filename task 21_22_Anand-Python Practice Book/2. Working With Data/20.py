'''
Problem 20: Implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.

$ python grep.py she.txt sure
The shells that she sells are seashells I'm sure.
I'm sure that the shells are seashore shells.
'''


import sys
x = sys.argv[2]
f = open(sys.argv[1])
for line in f:
    if x in line:
        print(line)
    else:
        pass
