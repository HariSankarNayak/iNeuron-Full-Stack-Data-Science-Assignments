# decimal to Binary, Octal and Hexadecimal conversion
def dec_to_Bin_Oct_Hex(num):
    print(f'Binary Form of {num} is : {bin(num)}')
    print(f'Octal Form of {num} is : {oct(num)}')    
    print(f'Hexadecimal Form of {num} is : {hex(num)}')    

num = int(input('Enter a Number: '))
dec_to_Bin_Oct_Hex(num)