#  Check if entered number is positive or negative

try :
    x=eval(input("Enter number: "))
    if x>0:
        print("Positive")
    elif x<0:
        print("Negative")
    else:
        print("Zero")
except :
    print("Invalid input")



