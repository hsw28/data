import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
from pylab import plotfile, show, gca

data1 = np.genfromtxt('rat2alt-binned.csv', delimiter=',', skip_header=0, skip_footer=17, names=['a', 'b', 'c', 'd', 'e'])
data2 = np.genfromtxt('rat2alt-binned.csv', delimiter=',', skip_header=10, names=['f', 'g'])
fig = plt.figure()
ax1 = fig.add_subplot(111)

x1=data1['a']-.34
x2=data1['a']+.17

y1=data1['c']/data1['b']*100
y2=data1['e']/data1['d']*100

ax1.plot(data2['f'], data2['g'], color='gray', linewidth=2, label='Total average/day')

plt.bar(x1, y1, color='darkslategray', width=0.34, label='% of correct turns that required alternating')
plt.bar(x2, y2, color='mediumpurple', width=0.34, label='% of correct turns that required NOT alternating', align='center')

plt.legend(loc=2, fontsize=10)
plt.axis([1,17.5,0,100])
plt.xlabel('Day')




show()

