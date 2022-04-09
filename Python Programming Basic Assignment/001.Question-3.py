from email.mime import base


theight = int(input("\nEnter height of the triangle: "))
tbase = int(input("\nEnter base of the triangle: "))

#  Calculate the area of the triangle
# formula: area = (base * height) * 0.5
def area_triangle(height, base):
    area = (height * base) * 0.5
    return area
print("\nArea of the triangle is: of base {} height {} is".format(tbase,theight), area_triangle(theight, tbase))