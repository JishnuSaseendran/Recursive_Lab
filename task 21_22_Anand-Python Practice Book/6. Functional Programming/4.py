'''
Problem 4: Write a function treemap to map a function over nested list.

>>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
[1, 4, [9, 16, [25]]]
'''


def treemap(fun, lis, result = None):
    if result == None:
        result = []
    for i in lis:
        if  isinstance(i, list):
            result.append(treemap(fun, i))
        else:
            result.append(fun(i))
    return result

print(treemap(lambda x: x*x, [1, 2, [3, 4, [5]]]))
