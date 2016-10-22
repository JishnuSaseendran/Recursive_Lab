'''
Problem 2: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

>>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
{'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
'''

flatten={}
def flatten_dict(d):
      temp={}
      for x,y in d.items():
         if isinstance(y,dict):
	    for i,j in y.items():
	       temp[x+'.'+i]=j
	    flatten_dict(temp)
         else:
	    flatten[x]=y
      return flatten

print flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
