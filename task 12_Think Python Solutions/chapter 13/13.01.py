from string import punctuation, whitespace

book = 'the boring stuff.txt'

b=open(book, 'r')

words = b.read().split()

def clean(word):
    
    word = word.strip(punctuation + whitespace).lower()
    return(word)
       
print "{} has {} 'words'".format(book, len([clean(word) for word in words]))
