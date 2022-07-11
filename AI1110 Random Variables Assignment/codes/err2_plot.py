#Importing numpy, scipy, mpmath and pyplot
from cmath import log
import numpy as np
import matplotlib.pyplot as plt
import scipy 
import mpmath as mp


maxrange=100
maxlim=10.0
x = np.linspace(0,maxlim,maxrange)#points on the x axis
a = []
simlen = int(1e6)
for i in range(0,11):
    a.append(i)

y = np.loadtxt('prob_err.dat',dtype='double')

log_y = []
for i in range(0,11):
    log_y.append(mp.log(y[i]))

def err(x):
    #x = 10**(x/10.0)
    return 0.5*(1 - ((x/(x+2))**(0.5)))

def logarithm_err(x):
    return mp.log(err(x))

vec_err = scipy.vectorize(err)
vec_log_err = scipy.vectorize(logarithm_err)


plt.plot(a,log_y,'o')
plt.plot(x,vec_log_err(x))
plt.grid() #creating the grid
plt.xlabel('$\gamma$')
plt.ylabel('$log(P_e\gamma)$')
#plt.savefig('../figs/P_e vs gamma.png')
plt.savefig('../figs/Pe_semilog.png')
plt.show()

