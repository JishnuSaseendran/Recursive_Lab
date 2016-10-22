'''
Problem 9: Write a function cumulative_product to compute cumulative product of a list of numbers.
'''
def cumulative_prod(x):
	a = []
	z = 1	
	for i in x:
		z *= i 
 		a.append(z)
	return a


print cumulative_prod([1,2,3,4,5,])
