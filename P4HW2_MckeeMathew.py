# Mathew McKee
# 7/6/2025
# P4HW2
# Gross pay calc for multiple people

# Define variables
loop = int(0)
total_ot = float(0)
total_pay = float(0)
gross = float(0)
# initial user input
employee = input("Enter employee's name or \"Done\" to terminate: ")
# Calculating loop
while employee != "":
    if employee != "Done":
        loop = loop + 1
        hours = float(input("How mand hours did " + employee + " work? "))
        pay = float(input("What is " + employee + " pay rate? "))
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
        print()
        print(f"Employee name: {employee:>10}")
        print()
        print("Hours Worked    Pay Rate    OverTime    OverTime Pay    ReqHour Pay    Gross Pay")
        print("--------------------------------------------------------------------------------")
        print(f"{hours:<15.1f} {pay:<11.2f} {ot:<11.1f} {otpay:<15.2f} ${reqpay:<13.2f} ${gpay:<11.2f}")
        print()
        print()
        #Tracking of variables from inputs
        total_ot = total_ot + otpay
        total_pay = total_pay + reqpay
        gross = gross + gpay
        #End of this loop input
        employee = input("Enter employee's name or \"Done\" to terminate: ")
        continue
    if employee == "Done":
        #termination here with output
        print()
        print("Total number of employees entered: " + str(loop))
        print(f"Total amount paid for overtime: ${total_ot:.2f}")
        print(f"Total amount paid for regular hours: ${total_pay:.2f}")
        print(f"Total amount paid in gross: ${gross:.2f}")
        break


