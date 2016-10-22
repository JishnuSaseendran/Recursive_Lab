'''
Problem 7: Python has built-in functions min and max to compute minimum and maximum of a given list. Provide an implementation for these functions. What happens when you call your min and max functions with a list of strings?
'''
def min(x):
    x.sort()
    return x[0]

def max(x):
    x.sort()
    return x[-1]


z = [25,456,26,49,22,66,454,55,66,45,522,466]
print min(z)
print max(z)
