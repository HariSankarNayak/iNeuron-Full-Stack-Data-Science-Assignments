# Swap of two numbers without using third variable
f_no=int(input("Enter first number: "))
s_no=int(input("Enter second number: "))


def swap_nos(f_no,s_no):
    f_no,s_no=s_no,f_no
    return f_no,s_no

print("\nAfter swapping first number is: ",swap_nos(f_no,s_no))