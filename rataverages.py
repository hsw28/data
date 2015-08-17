import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
from pylab import plotfile, show, gca

data1 = np.genfromtxt('rat1av.csv', delimiter=',', skip_header=0, names=['a', 'b'])
data2 = np.genfromtxt('rat2av.csv', delimiter=',', skip_header=0, names=['c', 'd'])
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(data1['a'], data1['b'], color='r', label='rat 1')
ax1.plot(data2['c'], data2['d'], color='b', label='rat 2')
plt.axis([1,12,0,100])
plt.legend()
plt.xlabel('Session')
plt.ylabel('Percent Correct')

plt.title('Performance Averages')

show()