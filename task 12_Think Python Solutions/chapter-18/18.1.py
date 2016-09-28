class Time(object):
  def __init__(self,hour=0,minute=0,second=0):
    self.hour=hour
    self.minute=minute
    self.second=second
  
  def __str__(self):
    return("%d:%d:%d"%(self.hour,self.minute,self.second))

  def __cmp__(self,other):
    t1=self.hour,self.minute,self.second
    t2=other.hour,other.minute,other.second
    return cmp(t1,t2)
def main():
    p1=Time(4,12,55)
    p2=Time(5,42,20)
    print(p1>p2)

if __name__=='__main__':
  main()

