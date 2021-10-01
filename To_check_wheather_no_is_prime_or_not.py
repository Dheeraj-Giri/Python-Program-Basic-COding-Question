// take input from the user and to check whether the inpute no. is prime or NOT.
def main():
    a=int(input())
    for i in range(2,a+1):
        if a%i==0:
            print(a," is NOT PRIME number ")
        else:
            print(a," is PRIME number ")
            break
main() 