# This is for debuggin.
# import pdb
# pdb.set_trace()
import time 
def Deposit(netAmount):
    
    amount=int(input("Enter the deposit Amount : "))
    netAmount=netAmount+amount
    print("waiting for Transaction ........!!!")
    time.sleep(1)
    #print("The total amount is ",netAmount)
    return netAmount
def Withdraw(netAmount):
    
    amount=int(input("Enter the withdraw Amount : "))
    check=netAmount=netAmount-amount
    if (check)<=0:
        if netAmount==0:
            print("Zero balance ! ")
        else:
            print("insufficient balance ")
        return check    

    else:
        print("waiting for Transaction ........!!!")
        time.sleep(1)
        #print("The total amount is", check)
        return netAmount


if __name__=="__main__":
    netAmount=0
    while True:
        print("Select the option :\n1) Deposit the Amount \t2) Withdraw the Amount \t3) check balance \t4) quit")
        a=int(input("Enter selected option : "))
        if (a==1):
            netAmount=Deposit(netAmount)
            print("The total amount is ",netAmount)
            print("\nTransaction completed Successfully... \n")
        elif (a==2):
            netAmount=Withdraw(netAmount)
            if netAmount>=0:
                print("The total amount is ",netAmount)
            else:
                print("YOU NEED TO ADD SOME AMOUNT IN YOUR ACCOUNT!")
            print("\nTransaction completed Successfully... \n")
        elif (a==3):
            print("current balance is ",netAmount)
        
        elif (a==4):
            print("Thank you for your Transactions !!\n have a good day !!")
            break
        else:
            print("Invalid input! ")

