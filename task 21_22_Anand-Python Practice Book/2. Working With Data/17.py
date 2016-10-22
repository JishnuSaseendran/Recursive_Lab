'''
Problem 17: Write a program reverse.py to print lines of a file in reverse order.
'''
f = open('she.txt')
lines = []
for line in f:
    lines.append(line)
for i in range(-1,-len(lines) -1, -1):
    print(lines[i])
