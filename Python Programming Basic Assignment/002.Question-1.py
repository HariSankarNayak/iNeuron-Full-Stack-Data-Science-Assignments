# killometers to miles
def km_to_miles(km):
    miles = km * 0.621371
    return round(miles, 2)


dist_in_km = float(input("Enter distance in kilometers: "))

print("Distance of({})in miles:".format(dist_in_km), km_to_miles(dist_in_km))
