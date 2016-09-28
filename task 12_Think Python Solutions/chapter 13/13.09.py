
# Current Status: Incomplete
from pylab import*
import string
import math
def word_clean(word):
  word = word.strip(string.punctuation + string.whitespace + string.digits).lower()
  return(word)

def create_dict(filename):
  word_dict={}
  f=open(filename,'r')
  words=f.read().split()
  words=[word_clean(word) for word in words]
  for word in words:
    word_dict[word]=word_dict.get(word,0)+1
  return(word_dict)


def create_ranks(d):
  res = []
  for key, value in d.items():
    res += [(value, key)]
  res.sort(reverse = True)
  return res

def plot(ranks):
  f = open("plot_res.csv", "w")
  for i in range(len(ranks)):
    line = str(math.log(ranks[i][0])) + ", " + str(math.log(i + 1)) + "\n"
    f.write(line)
    plot(rank)
    show()
  f.close()

dict_=create_dict('meta.txt')
ranks=create_ranks(dict_)
#plot(ranks)
#show()

