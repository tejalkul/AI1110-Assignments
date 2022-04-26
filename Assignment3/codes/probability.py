#Name : Tejal Kulkarni
#Roll Number:CS21BTECH11058
#Date: 10/04/2022

#Python Code to find probability of getting 2 heads in a 3 coin tossing experiment

import pandas as pd
import numpy as np
from numpy import linalg as LA, r_
from numpy import random as RN

import matplotlib.pyplot as plt
from matplotlib.pyplot import stem


read = pd.read_excel('C:\\Users\\Tejal Kulkarni\\OneDrive\\Documents\\IITH 1st year books\\table1.xlsx')
data = np.array(read)

#Sample size
N = 200

#Theorotical probability
frequency = np.array(data[0])
Pr_two_heads = frequency[2]/N

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

#Display probability
print("Probability of getting 2 Heads(Theorotical): ",Pr_two_heads)
print("Probability of getting 2 Heads(Practical): ", pr_2)

#Plotting PMF from the given data
X = np.array([3,2,1,0])
Y = np.array([frequency[1]/N,frequency[2]/N,frequency[3]/N,frequency[4]/N])
fig1 = stem(X, Y, linefmt='k-', markerfmt='ko', basefmt='k-')
plt.grid('minor')
plt.savefig("C:\\Users\\Tejal Kulkarni\\OneDrive\\Pictures\\Saved Pictures\\PMF1.png")

#Plotting PMF to compare theoretical and practical
X = np.array([0,1,2,3])
Y = np.array([1/8,3/8,3/8,1/8])
fig2 = stem(X, Y, linefmt='k-', markerfmt='ro', basefmt='k-')
plt.grid('minor')
plt.text(2.2,0.32,"o - Theoretical",color = 'red')
plt.text(2.2,0.3,"o - Practical",color = 'black')
plt.savefig("C:\\Users\\Tejal Kulkarni\\OneDrive\\Pictures\\Saved Pictures\\PMF2.png")


