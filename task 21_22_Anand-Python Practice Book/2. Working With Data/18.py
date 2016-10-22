'''
Problem 18: Write a program to print each line of a file in reverse order.


'''

f = open('she.txt', 'r')
for line in f:
	print line[::-1]
