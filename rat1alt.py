import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
from pylab import plotfile, show, gca

data1 = np.genfromtxt('rat1alt.csv', delimiter=',', skip_header=0, names=['a', 'b', 'c', 'd', 'e'])
fig = plt.figure()
ax1 = fig.add_subplot(111)

x1=data1['a']-.34
x2=data1['a']+.17

y1=data1['c']/data1['b']*100
y2=data1['e']/data1['d']*100



plt.bar(x1, y1, color='seagreen', width=0.34, label='% correct if previous turn was opposite direction of correct turn')
plt.bar(x2, y2, color='orangered', width=0.34, label='% incorrect if previous turn was opposite direction of correct turn', align='center')


plt.legend(loc=2)
plt.axis([0,7,0,119.9])
plt.xlabel('Day')



show()


#p1=plt.bar(data1['a'], data1['c']/data1['b'], color='seagreen', label='% correct if previous turn was opposite direction', align='center')
#p1=plt.bar(data1['a'], data1['e']/data1['d'], color='orangered', label='% incorrect if previous turn was opposite direction', align='center')
