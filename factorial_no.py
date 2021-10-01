# In one line of code

# def factorial(n):
#     return 1 if(n==0 or n==1) else n*factorial(n-1)

# user=int(input("Enter the factorial number "))
# print("the factorial no. of ",user, "is",factorial(user))



# using while loop 

def factorial(n):
    if n<0:
        return -1
    elif n==0 or n==1:
        return 1
    else:
        fact=1
        while(n>1):
            fact*=n
            n-=1
        return fact
user=int(input("Enter the factorial number"))
print("the factorial number of ",user,"is",factorial(user))