'''
Problem 12: Write a program mydoc.py to implement the functionality of pydoc. The program should take the module name as argument and print documentation for the module and each of the functions defined in that module.

$ python mydoc.py os
Help on module os:

DESCRIPTION

os - OS routines for Mac, NT, or Posix depending on what system we're on.
...

FUNCTIONS

getcwd()
    ...
'''
import sys
from inspect import *
def mypydoc(x):
	p=__import__(x)
	print 'DESCRIPTION:\n----------\n',p.__doc__
	for y in getmembers(p, predicate=lambda x: isfunction(x)):
			print y[0]
mypydoc(sys.argv[1])
