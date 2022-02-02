# find the index of the element without using index funtion.
# you can use the same code for tuple insted of list.

lst = ['a', 'b', 'c', 'd', 'e']

char = input("Enter the Element ")

if char in lst:
    count = 0
    for a in lst:
        if a != char:
            count += 1
        else:
            break
    print(char, "index = ", count)
else:
    print(char, "is not in list")

