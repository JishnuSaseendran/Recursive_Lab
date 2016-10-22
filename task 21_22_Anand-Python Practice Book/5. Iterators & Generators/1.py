'''
Problem 1: Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction. ::
'''

class reverse_iter:
	def __init__(self,i):
		self.i = i
	def __iter__(self):
		return self
	def next(self):
		if self.i >= 0:
			i = self.i
			self.i -= 1
			return i
    		else:
      			raise StopIteration()
for i in reverse_iter(5):
  	print i 
