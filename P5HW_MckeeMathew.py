# Mathew McKee
# 7/11/2025
# P5HW
# Basic fishing game

import random

def  createChar():
    # Create variables for dictionary
    name = input("Enter the name of your fisherman: ")
    bait_inventory = ["shrimp", "bloodworm", "crab", "cutbait", "minnow"]
    print(f"Welcome {name} to the coastal Atlantic where we will be fishing today.")
    print()
    print("These are the baits available for you to fish with.")
    print(bait_inventory)
    print()
    # Create dictionary that represents char
    character = {"name": name, "bait_inventory": bait_inventory}
    return character

# Function for creating the fish
def fish_type():
    fish = {}
    c_len = (str(random.randint(6, 20)) + " inches")
    bd_len = (str(random.randint(10, 70)) + " inches")
    bl_len = (str(random.randint(8, 35)) + " inches")
    rd_len = (str(random.randint(13, 73)) + " inches")
    f_len = (str(random.randint(12, 31)) + " inches")
    fish["croaker"] = {"name": "Atlantic Croaker", "length": c_len},
    fish["black_drum"] = {"name": "Black Drum", "length": bd_len},
    fish["bluefish"] = {"name": "Bluefish", "length": bl_len},
    fish["red_drum"] = {"name": "Red Drum", "length": rd_len},
    fish["flounder"] = {"name": "Flounder", "length": f_len}
        
    return fish

# Function made with access to char dictionary for fishing
def fishing(character, fish):
    print("To fish choose a bait from your inventory")
    bait = input()
    bait = bait.lower()
    print()
    #fishing loop should go in here
    while bait not in character["bait_inventory"]:
        bait = input(f"Please input a bait from this list {character["bait_inventory"]}: ")
        bait = bait.lower()
    while bait in character["bait_inventory"]:
        print(f"You have cast out your {bait}.")
        print()
        rng = random.randint(0, 101)
        if rng <= 60 and rng > 30:
            print("You have caught an Atlantic Croaker, this is the most common fish in this part of the Atlantic.")
            print(f"{fish["croaker"]}")
            print()
        elif rng > 60 and rng <= 80:
            print("You have caught a Black Drum, these fish although common can reach over 100 lbs")
            print(f"{fish["black_drum"]}")
            print()
        elif rng > 80 and rng <= 90:
            print("You have caught a Bluefish, be careful, they have a nasty bite.")
            print(f"{fish["bluefish"]}")
            print()
        elif rng > 90 and rng <= 98:
            print("You have caught a Red Drum, this is a prized sportfish in these parts. Congratulations!")
            print(f"{fish["red_drum"]}")
            print()
        elif rng > 98:
            print("You have caught a Flounder, certain species have been overfished commercially to be understocked in this part of the world.")
            print(f"{fish["flounder"]}")
            print()
        else:
            print(f"Your {bait} has been stolen, unlucky.")
            print()
        bait = input(f"Please select a new bait or q to quit: ")
        print()
        bait = bait.lower()
        while bait not in character["bait_inventory"] and bait != "q":
            print()
            bait = input(f"Please input a bait from this list {character["bait_inventory"]}: ")
            bait = bait.lower()
        if bait == "q":
            print()
            print("Thank you for playing")
            break
        continue
    



        
def main():
    character = createChar()
    fish = fish_type()
    fishing(character, fish)


if __name__ == "__main__":
    main()


