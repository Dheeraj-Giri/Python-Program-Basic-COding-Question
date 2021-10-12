def _sum(arry):
    Sum=0
    for i in arry:
        Sum+=i
    return Sum

lst=list(map(float,input("Enter the element : ").split()))
print(_sum(lst))