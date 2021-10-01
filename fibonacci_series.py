# using funtion method : 
def main():
    n1=0
    n2=1
    nterm=int(input())
    count=int(input())
    if nterm<0:
        print("Eneter the postive no. ")
    elif nterm==1:
        print(n1)
    else:
        print("Fibonaaci sequence :")
        print(n1, n2 , end=" ")
        while count<nterm:
            nth=n1+n2
            print(nth, end=" ")
            n1=n2
            n2=nth
            count=count+1
                      
main()

# second method short method : 
n1,n2=0,1
count=int(input("Enter the nThe element : "))
while n1<count:
    print(n1)
    n1,n2=n2,n1+n2
    
