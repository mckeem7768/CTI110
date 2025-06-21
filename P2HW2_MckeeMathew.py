# Mathew McKee
# 6/21/2025
# P2HW2
# List for input grades and then format results using fstrings

# create empty list and names it module_grades
module_grades = []
# Bulk inputs for appends to populate list from user input converted to float
module_grades.append(float(input("Enter grade for Module 1: ")))
module_grades.append(float(input("Enter grade for Module 2: ")))
module_grades.append(float(input("Enter grade for Module 3: ")))
module_grades.append(float(input("Enter grade for Module 4: ")))
module_grades.append(float(input("Enter grade for Module 5: ")))
module_grades.append(float(input("Enter grade for Module 6: ")))
print()
# Defining the Average as avg to make the print call back to this function
avg = (sum(module_grades) / len(module_grades))
print("------------Results------------")
print(f"{"Lowest Grade:": <20} {min(module_grades):.1f}")
print(f"{"Highest Grade:": <20} {max(module_grades):.1f}")
print(f"{"Sum of Grades:": <20} {sum(module_grades):.1f}")
print(f"{"Average:": <20} {avg:.2f}")
print("-------------------------------")

#Print Statement was used to test values were properly being entered into list
#print(module_grades)
