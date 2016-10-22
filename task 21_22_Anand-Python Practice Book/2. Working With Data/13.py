'''
Problem 13: Write a function lensort to sort a list of strings based on length.

>>> lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
['c', 'perl', 'java', 'ruby', 'python', 'haskell']
'''

def lensort(n):
	print sorted(n, key=len)
lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
