'''
Problem 7: How many multiplications are performed when each of the following lines of code is executed?

print square(5)
print square(2*5)
'''
numcalls = 0
def square(x):
    global numcalls
    numcalls = numcalls + 1
    return x * x

def multimes():
    print 'No od multiplications:', numcalls

print square(5)
multimes()
print square(2*5)
multimes()
