import math
# check Armstrong number

def check_armstrong(number):
    total_digits= int(math.log10(number))+1
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** total_digits
        temp //= 10
    if sum == number:
        print(number, "is an Armstrong number")
    else:
        print(number, "is not an Armstrong number")


user_input = int(input("Enter a number: "))    
check_armstrong(user_input)