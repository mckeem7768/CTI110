# Mathew McKee
# 6/28/2025
# P3HW1
# fix supplied python code

# I was supposed to put a comment here
# My Last Name


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
add = sum(grades)
avg = sum(grades) / len(grades)

print("------------Results------------")
print(f"{"Lowest Grade:": <20} {low:.1f}")
print(f"{"Highest Grade:": <20} {high:.1f}")
print(f"{"Sum of Grades:": <20} {add:.1f}")
print(f"{"Average:": <20} {avg:.2f}")
print("-------------------------------")

# determine letter grade for average


if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
       print('Your grade is: B')
elif avg >= 70:
       print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')





