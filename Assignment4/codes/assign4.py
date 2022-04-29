#Name : Tejal Kulkarni
#Roll Number:CS21BTECH11058
#Date: 28/04/2022

#Python Code to find probability of getting a black ball from a bag and find x.

import numpy as np
import mpmath as mp
from numpy import linalg as LA, r_
from numpy import random as RN

import matplotlib.pyplot as plt

#initially Random simulation

#Sample size
N = 12

#Generating Samples
x = RN.randint(0, high = 2, size=N)

#Computing probability
ctr_1 = np.count_nonzero(x==1)
ctr_0 = np.count_nonzero(x==0)
pr_1 = 1.0*ctr_1/N
pr_0 = 1.0*ctr_0/N
#Display probability
print("Probability of getting a black ball(practical): ",pr_0)

#Plotting Pr(X = 0) with the given data in the problem
X = np.linspace(0,5,50)
plt.plot(X,X/6, label = '$y = x/6$')              # 2*(x/12) where x/12 is probability of getting a black ball initially
plt.plot(X,(X+6)/18, label = '$y = x+6/18$')
plt.plot(3,0.5,'ko')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best', prop={'size':11})
plt.annotate('(3, 1/2)', (1, 0.5),xytext = (3.1,0.45),textcoords = 'data')
plt.savefig("C:\\Users\\Tejal Kulkarni\\OneDrive\\Pictures\\Saved Pictures\\Verification.png")

#Displaying probabilities from given data
initial_pr_0 = 3/12
print("Probability of getting a black ball(initial): ",initial_pr_0)
final_pr_0 = 9/18
print("Probability of getting a black ball(final): ",final_pr_0)




