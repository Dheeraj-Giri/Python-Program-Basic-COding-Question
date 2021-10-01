# first method is long method 

user=int(input("Enter the number :\n"))
orginal_no=user
sum=0
while(user>0):
    sum=sum+(user%10)*(user%10)*(user%10)
    user//=10
if orginal_no==sum:
    print("This is Amstrong number ")
else:
    print("This is not Amstrong number ")



#second method some short method

i=int(input("Enter the number :"))
original_val=i
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i//=10     # or i=i//10
print("This is Amstrong number" if original_val==sum else "This is Not Amstrong number" )