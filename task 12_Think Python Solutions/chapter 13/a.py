
from pylab import*
x = linspace(0, 2*pi, 400)
y = sin(x) + (1.0/3)*sin(3*x) + (1.0/5)*sin(5*x)
plot(x, y)
show()
