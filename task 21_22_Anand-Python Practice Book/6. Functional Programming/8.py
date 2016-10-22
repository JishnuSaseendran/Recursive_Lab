'''
Problem 8: Write a function count_change to count the number of ways to change any given amount. Available coins are also passed as argument to the function.

>>> count_change(10, [1, 5])
3
>>> count_change(10, [1, 2])
6
>>> count_change(100, [1, 5, 10, 25, 50])
292
'''

def count_change(amount,ways):
   """Return the number of ways to change the amount using given coins."""
   if amount == 0:
      return 1
   if amount < 0 or len(ways) == 0:
      return 0
   n = ways[0]
   return count_change(amount,ways[1:]) + count_change(amount-n,ways)
ways=(1,5)
print count_change(10,ways)
