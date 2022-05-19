#Name : Tejal Kulkarni
#Roll Number:CS21BTECH11058
#Date: 20/05/2022

#Python Code to find probability of getting atleast one defective egg and to plot the PMF and CDF of given binomial distribution

from re import A
from telnetlib import XAUTH
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import stem
from scipy.stats import binom



#Function for batch implementation of binom.pmf
#To return a numpy.ndarray with required pmf values
def getpmf(n, p):
    A = np.zeros(n + 1)
    for i in range(n + 1):
        A[i] = binom.pmf(i, n, p)
    return A

print("Sum of all probabilities in a binomial distribution(verification): ",sum(getpmf(10,0.1)))
pr_atleast_one = 1 - binom.pmf(0,10,0.1)
print("Probability that atleast one egg is defective: ",pr_atleast_one)

#Arrays for PMF
X = np.array(range(11))
Y = getpmf(10, 0.1)       #n=10,p=1/10
Z = np.cumsum(Y)

#Plotting the PMF
plt.subplot(1, 2, 1)
plt.xlabel('Value of Y')
plt.ylabel('Probability Mass Function')
plt.xticks(X)
stem(X, Y, linefmt='k--', markerfmt='ko', basefmt='k-')

#Plotting the CDF
plt.subplot(1, 2, 2)
stem(X, Z, linefmt='k--', markerfmt='ko', basefmt='k-')
plt.xlabel('Value of Y')
plt.ylabel('Cumulative Distribution Function')
plt.xticks(X)
plt.grid()
plt.tight_layout() #Space the subplots properly
plt.savefig("C:\\Users\\Tejal Kulkarni\\OneDrive\\Pictures\\Saved Pictures\\Pmf&Cdf.png")

