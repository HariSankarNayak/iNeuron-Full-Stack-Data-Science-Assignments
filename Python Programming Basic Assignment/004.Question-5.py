import math

# Armstrong number in an interval

def check_armstrong(number):
    total_digits= int(math.log10(number))+1
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** total_digits
        temp //= 10
    if sum == number:
        return True
    else:
        return False
    
def armstrong_in_interval(lower, upper):
    for i in range(lower, upper+1):
        if check_armstrong(i):
            print(i, end=" ")
    
    
    
start_range = int(input("Enter the start range: "))
end_range = int(input("Enter the end range: "))
armstrong_in_interval(start_range, end_range)

