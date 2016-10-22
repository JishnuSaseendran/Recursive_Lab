'''
Problem 2: Python has a built-in function sum to find sum of all elements of a list. Provide an implementation for sum.
'''
def sum(x):
    _sum = 0
    for i in x:
        _sum += i
    return _sum
print sum([11,22,33,44,55,66,77])

