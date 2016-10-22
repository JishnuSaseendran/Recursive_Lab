
SIZE=8

def printBoard(partial) :
  for digit in partial :
    col = int(digit)
    lin = ". "*(col-1) + "Q " + \
          ". "*(SIZE-col)
    print lin


def checkPlacement (partial, col) :
  row = len(partial)      # row we're adding
  if partial :
    spread = 1
    for prow in range(row-1,-1,-1) :   # previous rows
      if int(partial[prow]) in (col,col-spread,col+spread):
        return False
      spread += 1
  return True

def findSolutions() :
  partials = [""]    # empty board
  count = 0
  while partials :
    partial = partials.pop(0)
    if len(partial) >= SIZE :
      count += 1
      print partial # a solution
    else :
      for col in range(1,SIZE+1) :
        if checkPlacement (partial, col) :
           partials.append(partial+str(col))
  print('Total %d solutions found'%(count))


if __name__ == "__main__" :
  import time
  start = time.time()
  findSolutions()
  finish = time.time()
  print "Done. Took %.4f" % (finish-start)
