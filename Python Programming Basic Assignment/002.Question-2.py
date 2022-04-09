#  Celcious to Fahrenheit

def celcious_to_fahrenheit(celcious):
    fahrenheit = (celcious * (9/5)) + 32
    return round(fahrenheit, 2)

temp_in_degree = float(input("Enter the temperature in degree Celcious: "))

print("Temperature of({}) in Fahrenheit:".format(temp_in_degree), celcious_to_fahrenheit(temp_in_degree))