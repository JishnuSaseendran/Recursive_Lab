'''
Problem 37: Write a function valuesort to sort values of a dictionary based on the key.

>>> valuesort({'x': 1, 'y': 2, 'a': 3})
[3, 1, 2]
'''


def valuesort(d):
	return [d[x] for x in sorted(d.keys())]
print valuesort({'x': 1, 'y': 2, 'a': 3})
