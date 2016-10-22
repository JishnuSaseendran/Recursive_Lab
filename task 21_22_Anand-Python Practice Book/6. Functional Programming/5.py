'''
Problem 5: Write a function tree_reverse to reverse elements of a nested-list recursively.

>>> tree_reverse([[1, 2], [3, [4, 5]], 6])
[6, [[5, 4], 3], [2, 1]]
'''
'''
def tree_reverse(lis):
   lis.reverse()
   return lis
print tree_reverse([[1, 2], [3, [4, 5]], 6])
'''
def tree_reverse(lis,result=None):
    if result == None:
        result = []
    for i in lis:
        if isinstance(i,list):
            result.insert(0,tree_reverse(i))
        else:
            result.insert(0,i)
    return result

print tree_reverse([[1, 2], [3, [4, 5]], 6])        
