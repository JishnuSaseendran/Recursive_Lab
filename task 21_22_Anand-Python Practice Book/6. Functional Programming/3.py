'''
Problem 3: Write a function unflatten_dict to do reverse of flatten_dict.

>>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
{'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
'''

def unflatten(dictionary):
     resultDict = dict()
     for key, value in dictionary.iteritems():
        parts = key.split(".")
        d = resultDict
        print d
        for part in parts[:-1]:
            if part not in d:
                d[part] = dict()
            d = d[part]
        d[parts[-1]] = value
     return resultDict

print unflatten({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
