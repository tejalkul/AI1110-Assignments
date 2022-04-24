#Name : Tejal Kulkarni
#Roll Number:CS21BTECH11058
#Date: 24/04/2022

#Python Code to find probability of getting 2 heads in a 3 coin tossing experiment

import pandas as pd
import numpy as np
from numpy import linalg as LA, r_
from numpy import random as RN


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
print("Probability of getting 2 Heads(Theoretical): ",Pr_two_heads)
print("Probability of getting 2 Heads(Practical): ", pr_2)

