'''
Problem 11: Write a python program zip.py to create a zip file. The program should take name of zip file as first argument and files to add as rest of the arguments.

$ python zip.py foo.zip file1.txt file2.txt
'''
import sys
import zipfile
name=sys.argv[1]
z=zipfile.ZipFile(name,'w')
for i in range(2,len(sys.argv)):
  z.write(sys.argv[i])
