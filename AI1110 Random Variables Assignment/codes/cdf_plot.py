#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy 
import mpmath as mp

#if using termux
import subprocess
import shlex
#end if


maxrange=50
maxlim = 4
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
#c1 = np.zeros(20)
#c2 = np.linspace(0,1,10)
#c3 = np.ones(20)
#c = np.concatenate([c1,c2,c3])
simlen = int(1e6) #number of samples
err = [] #declaring probability list
h = 2*maxlim/(maxrange-1)
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
#randvar = np.loadtxt('log_V.dat',dtype='double')
randvar = np.loadtxt('tria.dat',dtype='double')
for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list


def uni_cdf(x):
	if(x>=0 and x<=1):
		return x
	elif x<0:
		return 0.0
	else:
		return 1.0

def Q(x):
	return (1 - mp.erf(x/np.sqrt(2)))/2

def gauss_cdf(x):
	return 1 - Q(x)

def log_cdf(x):
	if(x>=0):
		return 1 - np.exp(-x/2.0)
	else:
		return 0.0

def tria_cdf(x):
	if(x<=0):
		return 0.0
	elif(x>0 and x<=1):
		return x**2/2
	elif(x>1 and x<2):
		return 1 - ((2-x)**2/2)
	else:
		return 1.0


#plt.plot(x.T,err)
#vectorize
vec_uni_cdf = scipy.vectorize(uni_cdf)
vec_gauss_cdf = scipy.vectorize(gauss_cdf)
vec_log_cdf = scipy.vectorize(log_cdf)
vec_tria_cdf = scipy.vectorize(tria_cdf)

#plotting the CDF
#plt.plot(x.T,err)
plt.plot(x[0:(maxrange)].T,err,'o')
#plt.plot(x,vec_uni_cdf(x))  #plotting the CDF
#plt.plot(x,vec_gauss_cdf(x))
#plt.plot(x,vec_log_cdf(x))  #plotting the CDF
plt.plot(x,vec_tria_cdf(x))  #plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])

#plt.savefig('../figs/U_CDF.png')

#plt.savefig('../figs/X_CDF.png')

#plt.savefig('../figs/V_CDF.png')

plt.savefig('../figs/T_CDF.png')
plt.show()

#if using termux
#plt.savefig('../figs/uni_cdf.pdf')
#plt.savefig('../figs/uni_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
#plt.show() #opening the plot windowpi