'''
Problem 5: Write a function to compute the total number of lines of code in all python files in the specified directory recursively.

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
                    count += 1
        else:
            lineCount(f)
     return count       

print 'Total no of lines in the python files are %s : %d'%(sys.argv[1], lineCount(sys.argv[1])) 
