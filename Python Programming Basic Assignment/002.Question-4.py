#  Quadratic Equation
# Foormula for quadratic equation: ax^2 + bx + c = 0

print("Quadratic equation: ax^2 + bx + c = 0")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))


def quadratic_eq_formula(a, b, c):
    if a == 0:
        print("The equation is not quadratic")
    else:
        x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
        x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
        print("The roots of the equation are:", x1, x2)
        
quadratic_eq_formula(a, b, c)