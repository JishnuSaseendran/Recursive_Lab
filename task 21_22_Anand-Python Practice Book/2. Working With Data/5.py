'''
Problem 5: Write a function factorial to compute factorial of a number. Can you use the product function defined in the previous example to compute factorial?
'''

import prog4
def factorial(x):
    return prog4.product(range(1,x+1))


print(factorial(10))
