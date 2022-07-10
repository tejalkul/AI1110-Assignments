#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy 
import mpmath as mp


maxrange=50
maxlim=2.0
a = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
a = []
simlen = int(1e6)
for i in range(11):
    a.append(0.1*i)

y = np.loadtxt('prob_err.dat',dtype='double')

log_y = []
for i in range(11):
    log_y.append(mp.log(y[i]))


def Q(x):
	return (1 - mp.erf(x/np.sqrt(2)))/2

def logarithm_Q(x):
    return mp.log(Q(x))




vec_Q = scipy.vectorize(Q)

vec_log_Q = scipy.vectorize(logarithm_Q)

plt.plot(a,log_y,'o')
plt.plot(a,vec_log_Q(a))
plt.grid() #creating the grid
plt.xlabel('$a$')
plt.ylabel('$Pe$')
plt.savefig('../figs/semilog.png')
plt.show()


