'''
Problem 11: Write a function dups to find all duplicates in the list.

>>> dups([1, 2, 1, 3, 2, 5])
[1, 2]
'''

def dups(x):
	a = []
	b = []
	for i in x:
		if i not in a:
			a.append(i)
		else:
			b.append(i)		
	return b

print dups([1, 2, 1, 3, 2, 5])
