import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
from pylab import plotfile, show, gca

data1 = np.genfromtxt('rat1alt.csv', delimiter=',', skip_header=0, names=['a', 'b', 'c', 'd', 'e'])

# day, turns that would require alternating, correct turns of alternating turns, turns that don't require alternating, correct turns of non-alternating

fig = plt.figure()
ax1 = fig.add_subplot(111)

x1=data1['a']-.34
x2=data1['a']+.17

y1=data1['c']/data1['b']*100
y2=data1['e']/data1['d']*100



plt.bar(x1, y1, color='darkslategray', width=0.34, label='% of correct turns that required alternating from last visited arm')
plt.bar(x2, y2, color='mediumpurple', width=0.34, label='% of correct turns that required NOT alternating from last visited arm', align='center')


plt.legend(loc=2)
plt.axis([0,17.5,0,119.9])
plt.xlabel('Day')



show()


#p1=plt.bar(data1['a'], data1['c']/data1['b'], color='darkslategray', label='% correct if previous turn was opposite direction', align='center')
#p1=plt.bar(data1['a'], data1['e']/data1['d'], color='orangered', label='% incorrect if previous turn was opposite direction', align='center')
