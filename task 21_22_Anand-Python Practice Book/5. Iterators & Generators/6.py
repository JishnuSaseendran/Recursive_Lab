'''
Problem 6: Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively.
'''
import sys
import os
count = 0

def readDir(d):
    return (os.path.join(d, f)
            for f in os.listdir(d))

def lineCount(d):
     global count
     for f in readDir(d):
        if  os.path.isfile(f):
            if os.path.splitext(f)[-1].lower() == '.py':
                for line in open(f):
                    if line[0]!='#' and line != "\n":
                        count += 1
        else:
            lineCount(f)
     return count       

print 'Total no of lines in the python files gnoring empty and comment lines are %s : %d'%(sys.argv[1], lineCount(sys.argv[1])) 
