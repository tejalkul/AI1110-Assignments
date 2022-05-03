#Name : Tejal Kulkarni
#Roll Number:CS21BTECH11058
#Date: 03/05/2022

#Python Code to find number of heads/tails in a one time 3 coin tossing experiment.

import pandas as pd
import numpy as np
from numpy import linalg as LA, r_
from numpy import random as RN

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, stem

#Sample size
N = 1

#Generating Samples
x = RN.randint(0, high = 4, size=N)

#Finding the number of 3 Heads, 2 Heads, 1 Head and 0 Heads
ctr_3 = np.count_nonzero(x==3)
ctr_2 = np.count_nonzero(x==2)
ctr_1 = np.count_nonzero(x==1)
ctr_0 = np.count_nonzero(x==0)

#Compute probabilities
pr_3 = 1.0*ctr_3/N
pr_2 = 1.0*ctr_2/N
pr_1 = 1.0*ctr_1/N
pr_0 = 1.0*ctr_0/N
pr_atleast_2_heads = pr_2 + pr_3
pr_atmost_2_heads = pr_0 + pr_1 + pr_2
pr_atleast_1_head = pr_1 + pr_2 + pr_3
pr_atmost_2_tails = pr_atleast_1_head

print("In practical simulation probabilities are: ")
print("3 heads: ",pr_3)
print("2 heads: ",pr_2)
print("atleast 2 heads: ",pr_atleast_2_heads)
print("atlmost 2  heads: ",pr_atmost_2_heads)
print("0 heads: ",pr_0)
print("3 tails: ",pr_0)
print("2 tails: ",pr_1)
print("0 tails: ",pr_3)
print("atmost 2 tails: ",pr_atmost_2_tails)



#Plotting PMF and CDF
X = np.array([0,1,2,3])
Y = np.array([1/8,3/8,3/8,1/8])
Z = np.cumsum(Y)

#Extra points
X_cdf = np.array([-1,4])
Y_cdf = np.array([0,1])

#Arrays for ticks
T = np.array([-1, 0, 1, 2, 3, 4])

#Plotting the PMF
plt.subplot(1,2,1)
plt.xlabel('Value of X')
plt.ylabel('Probability Mass Function')
plt.xticks(T)
plt.grid()
stem(X, Y, linefmt='k--', markerfmt='ko', basefmt='k-')


#Plotting the CDF
plt.subplot(1,2,2)
stem(X, Z, linefmt='k--', markerfmt='ko', basefmt='k-')
stem(X_cdf, Y_cdf, linefmt='k--', markerfmt='ko', basefmt='k-')
plt.xlabel('Value of X')
plt.ylabel('Cumulative Distribution Function')
plt.xticks(T)
plt.grid()
plt.tight_layout()
plt.savefig("C:\\Users\\Tejal Kulkarni\\OneDrive\\Pictures\\Saved Pictures\\PMF&CDF.png")
