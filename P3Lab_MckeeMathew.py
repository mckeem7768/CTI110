# Mathew McKee
# 6/28/2025
# P3Lab
# Write code that Converts monetary float input

# Enter money as a float
money = float(input("Enter the amount of money as a float: $"))
# Convert float to Int
money = int(money * 100)

# Assign money values
dollar = int(100)
quarter = int(25)
dime = int(10)
nickel = int(5)
penny = int(1)
# Branching statements to output correct money outputs
if money == 0:
    print("No change")
if money >= 0:
    x = money // dollar
    if x >= 2:
        print(x, "Dollars")
        money = money - dollar * x
    if x == 1:
        print(x, "Dollar")
        money = money - dollar
if money >= 0:
    x = money // quarter
    if x >= 2:
        print(x, "Quarters")
        money = money - quarter * x
    if x == 1:
        print(x, "Quarter")
        money = money - quarter
if money >= 0:
    x = money // dime
    if x >= 2:
        print(x, "Dimes")
        money = money - dime * x
    if x == 1:
        print(x, "Dime")
        money = money - dime
if money >= 0:
    x = money // nickel
    if x >= 2:
        print(x, "Nickels")
        money = money - nickel * x
    if x == 1:
        print(x, "Nickel")
        money = money - nickel
if money >= 0:
    x = money // penny
    if x >= 2:
        print(x, "Pennies")
        money = money - penny * x
    if x == 1:
        print(x, "Penny")
        money = money - penny

