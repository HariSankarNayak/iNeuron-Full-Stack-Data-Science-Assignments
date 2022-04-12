#  LCM of two numbers
def lcm_of_two(a,b):
    if a > b:
        big = a
    else:
        big = b
    while True:
        print(big ," " ,a, " ", b)
        if((big%a == 0) and (big%b == 0)):
            lcm = big
            break
        else:
            big +=1
    print(f'The LCM of {a},{b} is {lcm}')

a= int(input('Enter first number: '))
b= int(input('Enter second number: '))
lcm_of_two(a,b)