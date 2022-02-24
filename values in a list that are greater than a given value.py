def GreatVal(lst, target):
    return target < any(lst)


print(GreatVal(list(map(int, input("Enter the list : ").split())), int(input("Enter the target : "))))
