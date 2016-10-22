'''
Problem 13: Write a function istrcmp to compare two strings, ignoring the case.

>>> istrcmp('python', 'Python')
True
>>> istrcmp('LaTeX', 'Latex')
True
>>> istrcmp('a', 'b')
False
'''

def istrcmp(x, y):
    return x.upper()==y.upper()

print(istrcmp('python','Python'))



