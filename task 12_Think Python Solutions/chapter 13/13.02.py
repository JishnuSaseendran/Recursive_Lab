#Print the number of different words used in the book. Compare different 
#books by different authors, written in different eras. Which author uses 
#the most extensive vocabulary?

from string import punctuation, whitespace

origin = 'origin.txt'
huck = 'huck.txt'
frank = 'frank.txt'
great = 'great.txt'
meta = 'meta.txt'
sherlock = 'sherlock.txt'
tale = 'tale.txt'

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
    word = word.strip(punctuation + whitespace).lower()
    return(word) 

def histogram(data):
    hist = {}
    for word in data:
        hist[word] = hist.get(word, 0) + 1
    return hist

books = [origin, huck, frank, great, meta, sherlock, tale]

def stats():
    auther = {}
    for book in books:
        book = open(book, 'r')
        print "Details of the book %s:" % book.name
        data = [clean(word) for word in words(book)]
        book.close()
        print "  Book has total: %s" % len(data)
        print "  Book has unique words: %s" % len(histogram(data))
        auther[book]=auther.get(book,0)+len(histogram(data))
    l = [key for key,value in sorted(auther.items(),reverse=True)]  
    print "The author of the book %s has the most extensive vocabulary" % (l[0])      
   
stats()
