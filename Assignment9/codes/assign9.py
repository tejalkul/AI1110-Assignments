#Name : Tejal Kulkarni
#Roll Number:CS21BTECH11058
#Date: 27/05/2022

#Python Code to find E(x)


from statistics import mean


def Mean():
    Xi = [1,2,3,4,5,6]
    pi = [1/6,1/6,1/6,1/6,1/6,1/6]
    mean = 0

    for i in range(6):
        mean = mean + Xi[i]*pi[i]
    return mean

print("E(X) = ", Mean())


        

