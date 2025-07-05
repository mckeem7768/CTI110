# Mathew Mckee
# 7/5/2025
# P4Lab2
# loop exercise multiply positive integer

x = 0
while x >= 0 :
    x = int(input("Enter an integer: "))
    print()
    if x>= 0:
        for num in range(1, 13):
            print(x, "*", num, "=", (x * num))
        print()
        end = input("Would you like to run the program again? ")
        if end == "no":
            print()
            print("Exiting program...")
            break
        elif end == "yes":
            print()
            x = int(input("Enter an integer: "))
    if x < 0:
        print()
        print("This program does not handle negative numbers")
        print()
        end = input("Would you like to run the program again? ")
        if end == "no":
            print()
            print("Exiting program...")
            break
        elif end == "yes":
            print()
            x = 0
        

        
        
