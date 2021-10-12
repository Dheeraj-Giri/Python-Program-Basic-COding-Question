def LargestElementInArray(arry):
    sort=sorted(arry)           # we sorting the array.
    return sort[-1]             # check the last element in the sorted list i.e large element.

arry=list(map(float,input("Enter the element : ").split()))
print(LargestElementInArray(arry))