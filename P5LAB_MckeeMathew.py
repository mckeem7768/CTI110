# Mathew Mckee
# 7/11/2025
# P5LAB
# Self checkout simulation

import random

def disperse_change(money):
    money = int(money * 100)
    dollar = int(100)
    quarter = int(25)
    dime = int(10)
    nickel = int(5)
    penny = int(1)
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




rand_pay = round(random.uniform(0.01, 100.00), 2)
def main():
    print(f"You owe ${rand_pay}")
    input_money = float(input("How much cash will you put in the self-checkout? "))
    money = input_money - rand_pay
    print(f"Change is: ${money:.2f}")
    print()
    disperse_change(money)
main()
