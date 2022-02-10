def computGCD(a, b):
    return a if (b == 0) else computGCD(b, a % b)


print(computGCD(int(input("Enter first value : ")), int(input("Enter second value : "))))
