'''
Problem 10: Write a function unique to find all the unique elements of a list.

>>> unique([1, 2, 1, 3, 2, 5])
[1, 2, 3, 5
'''

def unique(x):
	a = []
	a.append(x[0])
	for i in x:
		if i not in a:
			a.append(i)
	return a

print unique([1, 2, 1, 3, 2, 5])
