def unique(x):
	a = set([])
	for i in x:
		if i not in a:
			a.add(i)
	return a

print unique(set([1, 2, 1, 3, 2, 5]))
