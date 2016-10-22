'''
Problem 21: Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.

$ python wrap.py she.txt 30
I'm sure that the shells are s
eashore shells.
So if she sells seashells on t
he seashore,
The shells that she sells are
seashells I'm sure.
She sells seashells on the sea
shore;
'''

import sys
import textwrap
c = int(sys.argv[2])
f = open(sys.argv[1])
##print f.read()
print (textwrap.fill(f.read(), width = c))
