i=int(input("Etner the number "))
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)
    i=i//10
print("The sum of square is : ",sum)