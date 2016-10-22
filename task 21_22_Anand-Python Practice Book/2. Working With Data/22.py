'''
Problem 23: Write a program center_align.py to center align all lines in the given file.

$ python center_align.py she.txt
  I'm sure that the shells are seashore shells.
    So if she sells seashells on the seashore,
The shells that she sells are seashells I'm sure.
       She sells seashells on the seashore;
'''

import sys
def center_alignment(filename):
	f=open(filename).readlines()
	x=len(f)
	for line in f:
		##p=(x-len(line))/2
		print line 
center_alignment(sys.argv[1])
