'''
Problem 19: Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.
'''
import sys

def head(l):
   if len(l)>10:
      for i in range(10):
          print l[i]
   else:
      print len(l)

def tail(l):
    if len(l)>10:
       for i in range(len(l)-10,len(l)):
          print l[i]
    else:
       print len(l)
f=open('19.txt','r')
l=[]
for lines in f:
    l.append(lines)		
print 'First 10 lines'
head(l)
print 'Last 10 Lines'
tail(l)

