# Mathew Mckee
# 7/5/2025
# P4HW1
# Loop based score calculator

# Define variables for loops
num_scores = int(input("How many scores do you want to enter? "))
module_num = int(0)
# Create list to input scores
module_grades = []
# Begin initial while loop that appends scores to list via nested for loop
while num_scores > 0:
    for i in range(num_scores):
        module_num = module_num + 1
        num_scores = num_scores - 1
        x =(float(input("Enter grade for Module " + str(module_num) + ": ")))
        if x >= 0 and x <= 100:
            module_grades.append(x)
        else:
            print("Invalid Score entered!!!!")
            print("Score should be between 0 and 100")
            x = (int(input("Enter grade for Module " + str(module_num) + " again: ")))
            module_grades.append(x)

# Formatted Printed output
print()
print("------------Results------------")
print(f"{"Lowest Score": <20} : {min(module_grades):.1f}")
# Remove lowest grade from list
module_grades.remove(min(module_grades))
print(f"{"Modified List": <20} : {module_grades}")
avg = (sum(module_grades) / len(module_grades))
print(f"{"Scores Average:": <20} : {avg:.2f}")
# Calculate and assign grade here
if avg <= float(100) and avg >= float(90):
    grade = "A"
if avg < float(90) and avg >= float(80):
    grade = "B"
if avg < float(80) and avg >= float(70):
    grade = "C"
if avg < float(70) and avg >= float(60):
    grade = "D"
if avg < float(60):
    grade = "F"
print(f"{"Grade": <20} : {grade}")
print("--------------------------------")
