print("1-> Sum \t2-> Sub \n3-> multiply \t4) division \n5) modulus \t5-> floar division \n Enetr Q for quite ")
a=int(input("Enter the what to do ? :\n"))

if a==1:
    a=float(input("Enter the first value : "))
    b=float(input("Enter the second value : "))
    print(f"The sum of {a} and {b} is {a+b}")
     
elif a==2:
    a=float(input("Enter the first value : "))
    b=float(input("Enter the second value : "))
    print(f"The substraction of {a} and {b} is {a-b}")

elif a==3:
    a=float(input("Enter the first value : "))
    b=float(input("Enter the second value : "))
    print(f"The substraction of {a} and {b} is {a*b}")

elif a==4:
    a=float(input("Enter the first value : "))
    b=float(input("Enter the second value : "))
    print(f"The substraction of {a} and {b} is {a/b}")

elif a==5:
    a=float(input("Enter the first value : "))
    b=float(input("Enter the second value : "))
    print(f"The substraction of {a} and {b} is {a%b}")

elif a==6:
    a=float(input("Enter the first value : "))
    b=float(input("Enter the second value : "))
    print(f"The substraction of {a} and {b} is {a//b}")
    