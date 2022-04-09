# Swap without third variable not number

x=input("Enter first variable: ")
y=input("Enter second variable: ")

def swap_two(x, y):
    print("Before swapping: ", x, y)
    x,y=y,x
    print("After swapping: ", x, y)
    
    
swap_two(x, y)