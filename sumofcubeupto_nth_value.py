n=int(input("Enter the value upto which you want to add :\n"))
i=1
sum=0
while(i<=n):
    sum=sum+(i*i*i)
    i=i+1
print("The sum of cube is :",sum)