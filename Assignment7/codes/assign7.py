#Name : Tejal Kulkarni
#Roll Number:CS21BTECH11058
#Date: 11/05/2022

#Python Code for the qustion:
#Probability of solving specific
#problem independently by A and B are 1/2 and
#1/3 respectively. If both try to solve the problem
#independently, find the probability that
#(i) the problem is solved
#(ii) exactly one of them solves the problem

#Given
pr_e = 1/2
pr_f = 1/3

#Calculation (i)
pr_ef = pr_e*pr_f
pr_eUf = pr_e + pr_f - pr_ef
print("Probability that problem is solved: ",pr_eUf)

#Calculation (ii)
pr_e_not_f = pr_e*(1-pr_f)
pr_not_e_f = (1-pr_e)*pr_f
print("Probability that exactly one solves the problem: ",pr_e_not_f + pr_not_e_f)


