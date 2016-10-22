'''
Problem 2: Write a program extcount.py to count number of files for each extension in the given directory. The program should take a directory name as argument and print count and extension for each available file extension.

$ python extcount.py src/
14 py
4 txt
1 csv
'''
import os
import re
def extcount(filename):
  d={}
  l=[]
  _list=os.listdir(filename)
  fl=[re.findall('\.\w+',item) for item in _list]
##  print fl
##  print list
  for i in fl:
    i=i[0][1:]
    l.append(i)
  for i in l:
    d[i]=d.get(i,0)+1
  for key, value in d.items():
    print key, value
extcount('/home/jishnu/tasks/task 21/2. Working With Data')
