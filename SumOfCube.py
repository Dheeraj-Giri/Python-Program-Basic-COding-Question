user=int(input("Enter the number : \n"))
sum=0
while(user>0):  # it will check the value is less than 0
    # this part user%10  gives the cub of the each value and Add it in sum variable 
    sum=sum+(user%10)*(user%10)*(user%10)  
    # floar division to ignore the point value after division
    user//=10   # or user=user//10
print("The sum of cube of the given number is :",sum)