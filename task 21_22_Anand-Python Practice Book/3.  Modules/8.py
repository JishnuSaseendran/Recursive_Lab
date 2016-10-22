'''
Problem 8: Write a program links.py that takes URL of a webpage as argument and prints all the URLs linked from that webpage.
'''
from string import find
from urllib import urlopen
def links(x):
	n=1
	s=[]
	f=urlopen(x).read()
	while n>0:
		n=f.find('"http://')
		f=f[n+1:]
		n=f.find('"')
		s.append(f[:n])
		f=f[n:]
	print s
import sys
links(sys.argv[1])
