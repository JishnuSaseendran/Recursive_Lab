'''
Problem 35: Write a program to count frequency of characters in a given file. Can you use character frequency to tell whether the given file is a Python program file, C program file or a text file?


'''
from string import ascii_lowercase
f = open('21.txt')
text = f.read().strip()
freq = {}
for x in ascii_lowercase:
	freq[x] = text.count(x)
print(freq)
