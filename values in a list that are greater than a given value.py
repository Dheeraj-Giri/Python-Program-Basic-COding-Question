def GreatVal(lst, target):
    sort = sorted(lst)
    return target < lst[0]


print(GreatVal(list(map(int, input("Enter the list : ").split())), int(input("Enter the target : "))))
