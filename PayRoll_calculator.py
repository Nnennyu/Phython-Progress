#PROGRAM THAT CALCULATES THE WEEKLY PAY OF AN EMPLOYEE

'''Program: PayRoll_calculator.py
Author: Nnennaya Ihekwoaba

Program to compute an employee's weekly pay
1. Significant constant:
    Over time hourly rate = 1.5
2. The inputs are:
    Hourly wage,
    Total regular hours,
    Total over time hours
3. Computations:
Total weekly pay = HourlyWage * (TotalRegularHrs + (1.5 * TotalOvertimeHrs))
4. The outputs are:
    Total weekly pay'''

HourlyWage = float(input("Enter Hourly wage : "))
T_RegularHours = float(input("Enter total regular hours : "))
T_OvertimeHours = float(input("Enter the total overtime hours covered(if any) :" ))
T_WeeklyPay = HourlyWage * (T_RegularHours + (1.5 * T_OvertimeHours))
print("Total weekly pay is : ", T_WeeklyPay)
