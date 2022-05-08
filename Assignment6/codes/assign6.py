#Name : Tejal Kulkarni
#Roll Number:CS21BTECH11058
#Date: 03/05/2022

#Python Code to find number of P(A U B).





#Given
prb = 5/13    #Probability of B
pra = prb/2   #Probability of A
prab = 2/5    #Probability A

#Calculations
pra_intersection_b = prab*prb      #Probability A intersection B
pra_union_b = pra + prb - pra_intersection_b   #Probability A U B
print("P(A U B) = ",pra_union_b)
