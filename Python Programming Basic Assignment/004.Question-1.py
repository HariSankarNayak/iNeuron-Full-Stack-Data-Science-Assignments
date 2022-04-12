# Factorial of a number

unum= int(input("Enter a number: "))


def factorial_of_number(unum):
    factorial = 1
    for i in range(1, unum+1):
        factorial = factorial * i
    return factorial

print("factorial of {} is {}".format(unum, factorial_of_number(unum)))