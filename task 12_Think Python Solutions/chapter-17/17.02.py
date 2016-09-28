class point(object):
  def __init__(self,x=0.0,y=0.0):
    self.x=x
    self.y=y
  def printp(self):
    print('x value -> %d \n y value -> %d'%(self.x,self.y))


a=point(2)
b=point(3.2,5)
a.printp()
b.printp()
