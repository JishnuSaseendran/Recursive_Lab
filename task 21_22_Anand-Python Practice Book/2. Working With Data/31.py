'''
Problem 31: Generalize the above implementation of csv parser to support any delimiter and comments.

>>> print open('a.txt').read()
# elements are separated by ! and comment indicator is #
a!b!c
1!2!3
2!3!4
3!4!5
>>> parse('a.txt', '!', '#')
[['a', 'b', 'c'], ['1', '2', '3'], ['2', '3', '4'], ['3', '4', '5']]

'''

def parse(filename, delimitter, comments):
    f = open(filename)
    return [ line.strip().split(delimitter) 
           for line in f 
           if not line.startswith(comments)]

print parse('31.txt', '!', '#')
