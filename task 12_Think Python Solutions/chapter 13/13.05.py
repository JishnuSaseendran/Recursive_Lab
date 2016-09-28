import random

def hist(x):
    d = {}
    for item in x:
        d[item] = d.get(item, 0) + 1
    return d


def choose_from_hist(hist):
    total_letters = sum(hist.values())
    choice = random.choice(hist.keys())
    freq = hist[choice]
    print(choice + ': probability = ' + str(freq) + '/' + str(total_letters))

hist = hist('jishnu saseendran')
print(choose_from_hist(hist))    
    

