'''
Problem 11: Write a function vectorize which takes a function f and return a new function, which takes a list as argument and calls f for every element and returns the result as a list.

>>> def square(x): return x * x
...
>>> f = vectorize(square)
>>> f([1, 2, 3])
[1, 4, 9]
>>> g = vectorize(len)
>>> g(["hello", "world"])
[5, 5]
>>> g([[1, 2], [2, 3, 4]])
[2, 3]
'''

def vectorize(f):
    def sqr(l):
        return map(f, l)
    return sqr

def square(x): 
    return x * x
f = vectorize(square)
print f([1,2,3])

h = vectorize(lambda x: x*x)
print h([4,5,6])

g = vectorize(len)
print g(["hello", "world"])
