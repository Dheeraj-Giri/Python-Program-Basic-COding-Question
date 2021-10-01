user=input("Enter something:\n")
try:
    val = int(user)
    print("you entered integer  ", val)
except ValueError:
    try:
        val = float(user)
        print("you entered floating Number  ", val)
    except ValueError:
        print("You entered a string")