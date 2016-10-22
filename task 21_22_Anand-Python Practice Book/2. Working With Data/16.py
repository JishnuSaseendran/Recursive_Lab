'''
Problem 16: Write a function extsort to sort a list of files based on extension.

>>> extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']
'''

def extSort(x):
	x.sort(key = lambda x:x.split('.')[1])
	return x
print extSort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
