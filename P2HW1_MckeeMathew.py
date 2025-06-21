# Mathew McKee
# 6/15/2025
# P2HW1
# create a program that does basic math on a travel scenario adding floats for formatting

print("This program calculates and displays travel expenses\n")
# Ask user to enter budget
budget = float(input("Enter Budget: "))
print()
# Ask user to enter travel destination
location = input("Enter your travel destination: ")
print()
# Ask user for amount they will spend on gas
gas = float(input("Approximately, how much will be spent in fuel costs: "))
print()
# Ask user for amount they will spend on accomodation
hotel = float(input("How much will you need for accomodations: "))
print()
# Ask user for amount they will spend on food
food = float(input("Finally, how much will you need for food: "))
print()
# add expenses (addition of defined variables above)
expenses = gas + hotel + food

# subtract from budget (budget-expenses)
balance = budget - expenses

# Display result (print sequence of input variables and result)
print("-----------Travel Expenses-----------")
print(f"{"Location:": <20} {location}")
print(f"{"Initial Budget:": <20} ${budget:.2f}")
print(f"{"Fuel:": <20} ${gas:.2f}")
print(f"{"Accomodation:": <20} ${hotel:.2f}")
print(f"{"Food: ": <20} ${food:.2f}")
print("-------------------------------------")
print()
print(f"{"Remaining balance:": <20} ${balance:.2f}")
