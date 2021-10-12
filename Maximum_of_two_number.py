'''
 Find the maximum of two number : 
like: 10 and 20 , here 20 is maximum number.

''' 

def Func(a,b):
    if(a<b):
        return f"Maximum Number : {b} "
    return f"Maximum Number : {a} "

a=float(input("Enter the first number : "))
b=float(input("Enter the second number : "))

print(Func(a,b))