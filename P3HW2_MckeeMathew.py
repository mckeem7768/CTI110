# Mathew McKee
# 6/28/2025
# P3HW2
# Create employee pay charts with input values

# Inputs for individual
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay = float(input("Enter employee's pay rate: "))
# Overtime calc hours > 40 pay 1.5 times
if hours > 40:
    ot = hours - 40
    otpay = pay * 1.5 * ot
    reqpay = pay * 40
    gpay = reqpay + otpay
if hours < 40:
    ot = 0
    otpay = 0
    reqpay = pay * hours
    gpay = reqpay
    
print("------------------------------------")
print("Employee name:", name)
print()
print("Hours Worked    Pay Rate    OverTime    OverTime Pay    ReqHour Pay    Gross Pay")
print("--------------------------------------------------------------------------------")
print(f"{hours:<15.1f} {pay:<11.1f} {ot:<11.1f} {otpay:<15.2f} ${reqpay:<13.2f} ${gpay:<11.2f}")
