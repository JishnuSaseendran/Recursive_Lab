'''
Problem 8: Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. Write a function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of strings?

>>> cumulative_sum([1, 2, 3, 4])
[1, 3, 6, 10]
>>> cumulative_sum([4, 3, 2, 1])
[4, 7, 9, 10]

'''

def cumulative_sum(x):
	a = []
	if type(x[0]) == int:
		z = 0	
	else:
		z = ''
	for i in x:
		z += i 
 		a.append(z)
	return a


print cumulative_sum([1,2,3,4,5,])
print cumulative_sum(['Jishnu ','Thannikkunnath ','Saseendran'])	
