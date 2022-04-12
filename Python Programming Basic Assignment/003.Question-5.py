#  Print all prime numbers between 1-10000?

import math


def check_prime(num):
    mid_level = math.floor(math.sqrt(num))
    for i in range(3, mid_level+1):
        if num % i == 0:
            return False
    return True


prime_list = []
try:
    for num in range(1, 10001):
        if num >= 2:
            if num == 2:
                prime_list.append(num)
            else:
                if num % 2 == 0:
                    pass
                elif check_prime(num):
                    prime_list.append(num)
                else:
                    pass
        else:
            pass
    print(prime_list)
except:
    print("Something Wrong")
