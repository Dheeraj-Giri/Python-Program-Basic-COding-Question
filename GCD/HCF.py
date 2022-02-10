def calculateGCD(a, b):
    # if b == 0:
    #     return a
    # else:
    #     return calculateGCD(b, a % b)

    return a if (b == 0) else calculateGCD(b, a % b)


print(calculateGCD(int(input("Enter first value : ")), int(input("Enter second value : "))))
