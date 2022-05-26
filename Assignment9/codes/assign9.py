#Name : Tejal Kulkarni
#Roll Number:CS21BTECH11058
#Date: 27/05/2022

#Python Code to find E(x)


def Mean():
    Xi = [1,2,3,4,5,6]
    pi = [1/6,1/6,1/6,1/6,1/6,1/6]
    m = 0

    for i in range(6):
        m = m + Xi[i]*pi[i]
    return m

print("E(X) = ", Mean())


        

