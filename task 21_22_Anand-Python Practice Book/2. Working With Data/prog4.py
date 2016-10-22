'''
Problem 4: Implement a function product, to compute product of a list of numbers.

>>> product([1, 2, 3])
6
'''
def product(x):
    prod = 1
    for i in x:
        prod *= i
    return prod
print product([1,2,3,4,5,6,7])

