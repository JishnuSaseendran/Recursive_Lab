'''
Problem 2: Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.
'''


import sys
def line40(filename):
        return (line for f in filename
                for line in open(f)
                if len(line) > 40)

r = line40(sys.argv[1:])
for line in r:
        print line

  
