'''
Problem 9: Write a function permute to compute all possible permutations of elements of a given list.

>>> permute([1, 2, 3])
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
'''
permute_list = []
def permute(lis, l, r):
    if l == r:
        permute_list.append(lis[:])
    else:
        for i in range(l,r+1):
            lis[l], lis[i] = lis[i], lis[l]
            permute(lis, l+1, r)
            lis[l], lis[i] = lis[i], lis[l]
    return permute_list

lis = [1,2,3]
n = len(lis)

print permute(lis, 0, n-1)
