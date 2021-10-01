# count the no. of character in the given string 

string=input("Enter the string : \n")
val={char:string.count(char) for char in string}
print(val)


# in one line of code
val=input("Enter the string :\n")
print({char:val.count(char) for char in val}) 
