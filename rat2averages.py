import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
from pylab import plotfile, show, gca

data2 = np.genfromtxt('rat2av.csv', delimiter=',', skip_header=0, skip_footer=17, names=['c', 'd'])
data4 = np.genfromtxt('rat2av.csv', delimiter=',', skip_header=28, names=['g', 'h'])

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(data2['c'], data2['d'], color='b', linestyle='dashed', label='rat 2 average/session')
ax1.plot(data4['g'], data4['h'], color='b', linewidth=4, label='rat 2 average/day')


plt.axis([0,27,0,100])
plt.legend(loc=2)
plt.xlabel('Session')
plt.ylabel('Percent Correct')

plt.title('Performance Averages')

show()