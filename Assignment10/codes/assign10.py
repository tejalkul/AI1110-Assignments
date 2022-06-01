#Name : Tejal Kulkarni
#Roll Number:CS21BTECH11058
#Date: 31/05/2022

#Python Code to plot graph


from turtle import color
import matplotlib.pyplot as plt
import numpy as np



plt.subplot(1, 2, 1)
plt.axhline(0,color='black') # x = 0
plt.axvline(0,color='black') # y = 0
x1 = np.arange(0,3,0.01)
y1 = 3
y2 = 2
a1 = np.minimum(y1,y2)

x2 = np.arange(0,2,0.01)


plt.xlabel('X')
plt.ylabel('Y')

plt.vlines(x = 2, ymin = 2, ymax = 4, colors = 'black', linestyle = 'solid')
plt.hlines(y = 2, xmin = 2, xmax = 4, colors = 'black', linestyle = 'solid')

plt.vlines(x = 3, ymin = 0, ymax = 3, colors = 'black', linestyle = 'solid')
plt.hlines(y = 3, xmin = 0, xmax = 3, colors = 'black', linestyle = 'solid')

plt.annotate('(w, w)', (1, 0.5),xytext = (3.1,3.1),textcoords = 'data')
plt.annotate('y = z', (1, 0.5),xytext = (3.2,1.8),textcoords = 'data')
plt.annotate('x = z', (1, 0.5),xytext = (1.2,3.8),textcoords = 'data')
plt.annotate('w >= z', (1, 0.5),xytext = (3,4),textcoords = 'data')

plt.fill_between(x1,a1,color = "green",alpha = 0.8)
plt.fill_between(x2,y1,color = "green",alpha = 0.8)




plt.subplot(1, 2, 2)
plt.axhline(0,color='black') # x = 0
plt.axvline(0,color='black') # y = 0

x3 = np.arange(0,1,0.01)
y3 = 1 

plt.xlabel('X')
plt.ylabel('Y')

plt.vlines(x = 1, ymin = -0.5, ymax = 1, colors = 'black', linestyle = 'solid')
plt.hlines(y = 1    , xmin = -0.5, xmax = 1, colors = 'black', linestyle = 'solid')

plt.vlines(x = 2, ymin = 2, ymax = 3, colors = 'black', linestyle = 'solid')
plt.hlines(y = 2, xmin = 2, xmax = 3, colors = 'black', linestyle = 'solid')

plt.annotate('(w, w)', (1, 0.5),xytext = (1.1,1),textcoords = 'data')
plt.annotate('(z, z)', (1, 0.5),xytext = (2.1,2.1),textcoords = 'data')
plt.annotate('y = w', (1, 0.5),xytext = (0.2,1.1),textcoords = 'data')
plt.annotate('x = w', (1, 0.5),xytext = (1.2,-0.4),textcoords = 'data')
plt.annotate('w < z', (1, 0.5),xytext = (1,3),textcoords = 'data')

plt.fill_between(x3,y3,color = "green",alpha = 0.8)


plt.tight_layout() #Space the subplots properly
plt.savefig("C:\\Users\\Tejal Kulkarni\\OneDrive\\Pictures\\Saved Pictures\\Graph.png")





