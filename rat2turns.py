import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
from pylab import plotfile, show, gca

data1 = np.genfromtxt('rat2turns.csv', delimiter=',', skip_header=0, names=['a', 'b', 'c', 'd'])

fig = plt.figure()
ax1 = fig.add_subplot(111)

p1=plt.bar(data1['a'], data1['d'], color='mediumpurple', label='Total turns', align='center')
p2=plt.bar(data1['a'], data1['c'], color='darkslategray', label='Right turns taken', align='center')
p3=plt.bar(data1['a'], data1['b'], color='lightseagreen', label='Right turns expected', align='center')


plt.legend()
plt.axis([0,12,0,10])
plt.xlabel('Session')

plt.title('Right Turn Bias')



 
show()