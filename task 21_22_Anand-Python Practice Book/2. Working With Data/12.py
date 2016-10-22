'''
Problem 12: Write a function group(list, size) that take a list and splits into smaller lists of given size.

>>> group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
[[1, 2, 3, 4], [5, 6, 7, 8], [9]]

'''
def group(x, size):
	z = []
	c = 0
	no = len(x)//size
	lst = len(x)%size
	if lst != 0:
		nolst = no + lst
		for i in range(nolst):
			z.append(x[c:c+size])
			c += size
	else:
		for i in range(no):
                        z.append(x[c:c+size])
                        c += size
	return z


 

print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4) 
