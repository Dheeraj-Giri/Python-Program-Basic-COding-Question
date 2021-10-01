def Isprime(n):
    if n<0:
        print("Etner the positive no.")
    if n==1:
        print("prime no.")
    for i in range(2,n+1):
        if n>1:
            if n%i==0:
                print("Not prime number ")
                break
        else:
            print("is prime number ")
    else:
        print("Not prime no.")
user=int(input("Etner the number : "))
Isprime(user)