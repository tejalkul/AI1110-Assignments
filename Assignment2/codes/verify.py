#Name : Tejal Kulkarni
#Roll Number:CS21BTECH11058
#Date: 11/04/2022

#Python code to find the cost involved to increase production given initial units and final units.


import numpy as np
import mpmath as mp


#Input   
a = 100      #inital number of units
b = 300      #final number of units

f = lambda x: 500/(mp.sqrt(2*x + 25))     # Marginal Cost Function

#Output 
cost = mp.quad(f,[a,b])                 #Cost involved in increasing production from a to b
print(f"Cost involved to increase production from 100 units to 300 units is Rs.{int(cost)}")
  
