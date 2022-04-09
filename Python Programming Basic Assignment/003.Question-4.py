# Check number is prime or not
import math


def check_prime(num):
    mid_level = math.floor(math.sqrt(num))
    for i in range(3, mid_level+1):
        if num % i == 0:
            return False
    return True


try:
    num = int(input("Enter a number: "))
    if num >= 2:
        if num == 2:
            print("Prime")
        else:
            if num % 2 == 0:
                print("Not Prime")
            elif check_prime(num):
                print("Prime")
            else:
                print("Not Prime")
    else:
        print("Not Prime")
except:
    print("Invalid input")
