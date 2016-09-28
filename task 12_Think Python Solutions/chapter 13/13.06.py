import string
def process_file(filename):
  hist = dict()
  fp = open(filename)
  for line in fp:
    process_line(line, hist)
  return hist

def process_line(line, hist):
  line = line.replace('-', ' ')
  for word in line.split():
    word = word.strip(string.digits+string.punctuation + string.whitespace)
    word = word.lower()
    hist[word] = hist.get(word, 0) + 1
  return(hist)


def set_difference(hist,wordlist):# wordlist is a set
  words=[key for key,value in hist.items()]
  words=set(words)
  difference=words-wordlist
  return(difference)


hist=process_file('the boring stuff.txt')
print(set_difference(hist,{'the','me','where','out','there','what','get'}))
