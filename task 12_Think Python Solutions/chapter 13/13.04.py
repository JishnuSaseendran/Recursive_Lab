#Modify the previous program to read a word list (see Section 9.1) and then
# print all the words in the book that are not in the word list. How many of
# them are typos? How many of them are common words that should be in the word
# list, and how many of them are really obscure?

from string import punctuation, whitespace

origin = 'origin.txt' # Origin of Species, 1859
huck = 'huck.txt' # Huck Finn, 1884
don = 'don.txt' # Don Quixote, 1605
great = 'great.txt' # Expectations, 1860
meta = 'meta.txt' # morphisis, 1915
sherlock = 'sherlock.txt' # 1887
divine = 'divine.txt' # Comedy, 1308
journey = 'journey.txt'  # to the center of the earth, 1864

word_file = 'words.txt'
books = [origin, huck, don, great, meta, sherlock, divine, journey]

def words(book):
    list = []
    flag = False
    signal = "*** START OF"
    for line in book:
        if flag == True:
            for word in line.split():
                list.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    return list
    
def clean(word):
    result = ''
    for char in word:
        if (char in whitespace) or (char in punctuation):
            pass
        elif not char.isalpha():
            pass
        else:
            result += char.lower()
    return result

def stats():
    for book in books:
        book_words = set([clean(word) for word in words(open(book, 'r'))])
        words_ = set([word for word in open(word_file, 'r')])
        print "\n\n\nStats for %s" % open(book, 'r').name
        print "There are %s non-listed words." % len(book_words - words_)
	print "\nThe words not in the word list for the book %s is:\n" % open(book, 'r').name
	print book_words - words_        
stats()

