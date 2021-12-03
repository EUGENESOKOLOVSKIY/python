from numpy import *
import matplotlib.pyplot as plt


x = linspace(-1, 2, 51)
y=(3**x)+cos(15*x)

plt.plot(x, y, 'mp-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('25 version')
plt.savefig('1.png', dpi=200)
plt.show()
