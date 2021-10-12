'''
string is said to be palindrome if the reverse of the string is the same as string.

Example:
Anna, civic, kayak, level, madam, mom, noon, racecar, radar, redder, refer, repaper, rotator,rotor, sagas, solos, stats, tenet, wow.

'''

def Palindrome(string):
    if (string[::-1]==string):
        return "The string is Palindrome "
    elif (string[::-1]!=str_iterator):
        return "The string is Not Palindrome "
    else:
        return "Please Enter a valid string "

string=input("Enter the string : ")
print(Palindrome(string))