# Multiplication Table of a/upto Number

def multiplication_table_of_num(num):
    for i in range(1, 11):
        print(num, 'x', i, '=', num*i)


def multiplication_table_upto_num(num):
    for i in range(1, num+1):
        for j in range(1, 11):
            print(i*j, ' ', end='')
        print()




while True:
    print("\n 1. Choose 1 for multiplication table of one \n 2. Choose 2 for multiplications upto a number\n 3. Choose anyother to exit")
    choiceopt = int(input("\nEnter your choice: (1/2) "))
    if choiceopt == 1:
        num = int(input("Enter a number for table: "))
        multiplication_table_of_num(num)
    elif choiceopt == 2:
        num = int(input("Enter a number upto for table: "))
        multiplication_table_upto_num(num)
    else:
        print("\nThank you for using this program")
        exit()
