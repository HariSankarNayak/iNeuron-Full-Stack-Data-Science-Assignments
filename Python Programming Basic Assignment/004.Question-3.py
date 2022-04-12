#  Python Program to print the fibonacci sequence


def fibonacci_sequence(num):
    a = 0
    b = 1
    print(a, end=' ')
    print(b, end=' ')
    for i in range(2, num):
        c = a + b
        print(c, end=' ')
        a = b
        b = c
        
        
num=int(input("Enter the number of terms: "))
if num < 0:
    print('Fibonacci series is not available for Negative Number')
elif num <= 2 and num >= 0:
    print(0 , 1)
else:
    fibonacci_sequence(num)