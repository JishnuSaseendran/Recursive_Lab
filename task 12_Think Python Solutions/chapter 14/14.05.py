#!/usr/bin/env python 

def linecount(filename): 
    count = 0
    for line in open(filename): count += 1
    return count


def main():
    return __name__

if __name__ == '__main__':
    print linecount('wc.py')
##    print "Value of main is ", __name__
    print main()
    
    
