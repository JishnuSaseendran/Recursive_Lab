'''
Problem 4: Write a function to compute the number of python files (.py extension) in a specified directory recursively.
'''
import sys
import os
count = 0
def readDir(dir):
    return (os.path.join(dir, f)
            for f in os.listdir(dir))
            
def pyCount(dir):
     global count
     for f in readDir(dir):
        if  os.path.isfile(f):
            if os.path.splitext(f)[-1] == '.py':
                count += 1
        else:
            pyCount(f)
     return count       

print 'Total number of python files are :', pyCount(sys.argv[1])
