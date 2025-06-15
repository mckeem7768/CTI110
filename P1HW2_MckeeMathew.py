# Mathew McKee
# 6/15/2025
# P1HW2
# create a program that does basic math on a travel scenario

print("This program calculates and displays travel expenses\n")
# Ask user to enter budget
budget = int(input("Enter Budget: "))
print()
# Ask user to enter travel destination
location = input("Enter your travel destination: ")
print()
# Ask user for amount they will spend on gas
gas = int(input("Approximately, how much will be spent in fuel costs: "))
print()
# Ask user for amount they will spend on accomodation
hotel = int(input("How much will you need for accomodations: "))
print()
# Ask user for amount they will spend on food
food = int(input("Finally, how much will you need for food: "))
print()
# add expenses (addition of defined variables above)
expenses = gas + hotel + food

# subtract from budget (budget-expenses)
balance = budget - expenses

# Display result (print sequence of input variables and result)
print("--------Travel Expenses--------")
print("Location: ", location)
print("Initial Budget: ", budget, "\n")
print("Fuel: ", gas)
print("Accomodation: ", hotel)
print("Food: ", food, "\n")
print("Remaining balance: ", balance)
