'''
Problem 9: The built-in function enumerate takes an iteratable and returns an iterator over pairs (index, value) for each value in the source.

>>> list(enumerate(["a", "b", "c"])
[(0, "a"), (1, "b"), (2, "c")]
>>> for i, c in enumerate(["a", "b", "c"]):
...     print i, c
...
0 a
1 b
2 c

'''

import itertools
def my_enumerate(list):
  return (itertools.izip(range(len(list)),list))
print list(my_enumerate(['a','b','c']))
for i,c in my_enumerate(['a','b','c']):
   print i,c
