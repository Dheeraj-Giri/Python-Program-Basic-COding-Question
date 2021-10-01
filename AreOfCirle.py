def Areofcirlce():
    print("which value you have :\n1 -> Radius \t2-> Diameter ")
    a=int(input("Enter the value as per given above : "))
    if a==1:
        radius=float(input("Enter the radius value :"))
        area= pie*radius**2
        print("The area of circle is ", area)
        print()
    else:
        D=float(input("Enter the diameter value :"))
        radius=D/2
        area= pie*radius**2
        print("\nThe area of circle is ", area)
        print()
pie=3.14
Areofcirlce()