num=int(input("Enter how many element you want to Add : "))
lst=[]      # empty list
for i in range(1,num+1):
    a=input("Enter the element : ")
    lst.append(a)   # append into empty list 
print(len(set(lst)))