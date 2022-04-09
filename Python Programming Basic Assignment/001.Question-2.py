from operator import add, sub, mul, truediv

operations = { "+": add, "-": sub, "*":mul, "/":truediv } 

print('Select a Arithmetic Operation: \n 1. Addition(+) \n 2. Subtraction(-) \n 3. Multiplication(*) \n 4. Division(/) \n 5. Exit(other)')
   

while True:
    option = input('Enter a arithmetic operation -> ')
    if option == '0':
        print("Exited")
        break
    elif option not in ['+','-','*','/']:
        print("Please enter a valid option... Exiting...")
        break
    else:
        in1 = int(input('\nEnter 1st Number: '))
        in2 = int(input('\nEnter 2nd Number: '))
        print('{}{}{}={}\n'.format(in1, option, in2, operations[option](in1,in2)))
