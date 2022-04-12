def sum_of_n_nos(num):
    sum = num*((num+1)/2)
    print(f'Sum of {num} natural numbers is {sum}')
    
num = int(input('Enter a number upto: '))
sum_of_n_nos(num)