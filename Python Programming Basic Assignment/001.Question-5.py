from random import randint

a = int(input("Enter Min number : "))
b = int(input("Enter Max number : "))

def generateRandomNumber(start=0, end=1000):
    print('Random number -> ',randint(start,end))

generateRandomNumber(a,b)

