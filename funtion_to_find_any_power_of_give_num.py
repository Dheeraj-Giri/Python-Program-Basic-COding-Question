''' 

The program execute number of any power (raised to)  user want.
exmaple : if user want, power of 1,2,3,......n of 1,2,3,....n number then this program execute number of that power.

'''



def to_power(power):
    def to_num(num):
        return num**power
    return to_num

power_inp=int(input("Enter the power : "))

num_inp=int(input("Enter the number : "))

pow=to_power(power_inp)
print(pow(num_inp))