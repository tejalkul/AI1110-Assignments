#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if


maxrange=50
maxlim=4.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1)
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
#randvar = np.loadtxt('tria.dat',dtype='double')
#randvar = np.loadtxt('chi.dat',dtype='double')
randvar = np.loadtxt('root_V.dat',dtype='double')


for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

def gauss_pdf(x):
	return 1/mp.sqrt(2*np.pi)*np.exp(-x**2/2.0)

def tria_pdf(x):
	if(x<0):
		return 0.0
	elif(x>=0 and x<1):
		return x
	elif(x==1):
		return 1.0
	elif(x>1 and x<=2):
		return (2-x)
	else:
		return 0.0
	
def chi_pdf(x):
	if(x>=0):
		return np.exp(-x/2.0)/2
	else:
		return 0.0

def root_V(x):
	if(x>=0):
		return (np.exp(-x**2/2))*x
	else:
		return 0.0
		
vec_gauss_pdf = scipy.vectorize(gauss_pdf)
vec_tria_pdf = scipy.vectorize(tria_pdf)
vec_chi_pdf = scipy.vectorize(chi_pdf)
vec_root_V = scipy.vectorize(root_V)

plt.plot(x[0:(maxrange-1)].T,pdf,'o')
#plt.plot(x,vec_chi_pdf(x))
#plt.plot(x,vec_tria_pdf(x))
plt.plot(x,vec_root_V(x))
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])
#plt.savefig('../figs/X_PDF.png')
#plt.savefig('../figs/T_PDF.png')
#plt.savefig('../figs/V2_PDF.png')
plt.savefig('../figs/A_PDF.png')


#if using termux
#plt.savefig('../figs/uni_pdf.pdf')
#plt.savefig('../figs/uni_pdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_pdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_pdf.pdf')
#plt.savefig('../figs/gauss_pdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_pdf.pdf"))
#else
#plt.show() #opening the plot window