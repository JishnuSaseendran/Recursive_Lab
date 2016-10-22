'''
Problem 7: Implement a program dirtree.py that takes a directory as argument and prints all the files in that directory recursively as a tree.
'''
import os
import sys
a='|   '
i=0
def dirtree(dir,i):
   filenames=os.listdir(dir)
   for filename in filenames:
      if not os.path.isdir(os.path.abspath(dir+'/'+filename)):
         if filename==filenames[-1]:	
            print a*i+'\--',filename
         else:
            print a*i+'|--',filename
      else:
         print a*i+'|--',filename
         dir=dir+'/'+filename
         dirtree(dir,i+1)

dir=sys.argv[1]
print dir
dirtree(dir,i)
