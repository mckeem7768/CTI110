# Mathew McKee
# 6/21/2025
# P2LAB2
# Dictionary storage lab

car = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
    }
keys = car.keys()

print(keys, "\n")
x = input("Enter a vehicle to see it's mpg: ")
print()
print(f"The Prius gets", car[x], "mpg.\n")
y = float(input(f"How many miles will you drive the {x}? "))
print()
gas = float(f"{y / car[x]}")
print(f"{gas:.2f}", "gallon(s) of gas are needed to drive the", x, y, "miles.")
