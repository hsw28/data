import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
from pylab import plotfile, show, gca

data1 = np.genfromtxt('rat1.csv', delimiter=',', skip_header=2, names=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
data2 = np.genfromtxt('rat2.csv', delimiter=',', skip_header=2, names=['h', 'i', 'j', 'k', 'l', 'm', 'n'])


f, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=True)
ax1.plot(data1['a'], data1['g'], color='r')

ax1.set_title('Rat 1')
plt.axis([1,72,0,6])
plt.ylabel('Turns Until Correct')

ax2.plot(data2['h'], data2['n'], color='b')



ax2.set_title('Rat 2')
plt.axis([1,72,0,6])

plt.xlabel('Trials')
plt.ylabel('Turns Until Correct')

f.subplots_adjust(hspace=.2)


plt.show()