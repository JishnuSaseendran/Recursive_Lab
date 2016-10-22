'''
Problem 3: What happens when the above sum function is called with a list of strings? Can you make your sum function work for a list of strings as well.

>>> sum(["hello", "world"])
"helloworld"
>>> sum(["aa", "bb", "cc"])
"aabbcc"
'''
def strsum(x):
    _sum = ''
    for i in x:
        _sum += i
    return _sum
print strsum(["Jishnu", "Saseendran"])
