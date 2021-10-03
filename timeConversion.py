'''
Normal to Standard time conversion 
'''
def timeConversion(s):
    if ( (s[-2:]=='AM' or s[-2:]=='am')  and (s[:2]=='12') ):
        return '00'+s[2:-2]
    elif (s[-2:]=='AM' or s[-2:]=='am'):
        return s[:-2]
    elif (( s[-2]=='PM' or s[-2:]=='PM') and (s[:2]=='12') ):
        return s[:-2]
    return  str(int(s[:2])+12)+s[2:8]
print("Time input format is : 00:00:00 AM/PM")
print(timeConversion(input("Enter the time : ")))