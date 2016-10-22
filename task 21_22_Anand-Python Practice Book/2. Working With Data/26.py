'''
Problem 26: Python provides a built-in function filter(f, a) that returns items of the list a for which f(item) returns true. Provide an implementation for filter using list comprehensions.

>>> def even(x): return x %2 == 0
...
>>> filter(even, range(10))
[0, 2, 4, 6, 8]
'''
def filter(fun, l):
	return [ i for i in l if fun(i)]
def even(x):
	return x%2 == 0
print filter(even, range(10))
