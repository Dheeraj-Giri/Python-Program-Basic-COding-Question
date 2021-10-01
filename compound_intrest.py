
def compoundIntrest(principale, rate, time):
    amount = principale *(pow(1 + rate/100, time))
    CI = amount - principale
    print("the compound intrest is ", CI)
compoundIntrest(10000,10.25,5)




#using user input 

def compoundIntrest(principale,rate,time):
 
    amount = principale * ((1+rate/100)**time)
    CI = amount - principale
    print("the compound intrest is ", CI)

principale=float(input("Enter the principale value : "))
rate=float(input("Enter the rate : "))
time=float(input("Enter the time period : "))

compoundIntrest(principale,rate,time) 