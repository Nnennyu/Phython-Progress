#Program to compute a person's income tax.
'''
Program: Tax_income_calculator
Author: Nnennaya Ihekwoaba

Program to compute a person's income tax.
1. Significant constants:
    tax rate
    Standard personal allowance deduction
2. The inputs are:
    gross income(GI)
3.Computations:
    taxable income(TI) = gross income - standard personal allowance
    income tax = is a fixed percentage of taxable income
4. The outputs are
        the income tax'''

print("The Income Tax Calculator ")
print()
Standard_PA_deduction = 12500
G_income = float(input("Enter gross income: "))
T_income = G_income - Standard_PA_deduction

if T_income < 1:
    tax_rate = 0.0
    T_income = 0
    Income_tax = 0

#for T_income < £5000, use tax_rate=0.10(i.e 10%)
elif T_income >=1 and T_income <= 5000:
    tax_rate = 0.10
    Income_tax = T_income * tax_rate
elif T_income >= 5001 and 37500 >= T_income:
    tax_rate = 0.20
    Income_tax = T_income * tax_rate
elif G_income <= 100000 and (
        T_income >= 37501 and T_income < 150000):
    tax_rate = 0.40
    Income_tax = T_income * tax_rate

#For those with gross income above 100000, standard personal allowances
#reduces by £1 for every £2 they earn.
elif G_income > 100000:
    reduction = round((G_income - 100000) / 2)
    New_deduction = 12500 - reduction
    if reduction <= 12500:
        tax_rate = 0.40
        T_income = G_income - New_deduction
        Income_tax = New_Taxable_income * tax_rate

#For those who earn above 100000 and reduction is far above 12500 and taxable income < 150000
    elif reduction > 12500 and reduction < 25000:
        tax_rate = 0.40
        T_income = G_income
        Income_tax = G_income * tax_rate
    else:
        tax_rate = 0.45 #for Taxable income >= 150000:
        T_income = G_income
        Income_tax = G_income * tax_rate

print("Taxable Income :\t", T_income)
print("Tax rate : \t", tax_rate)
print("Annual Income Tax is :\t", Income_tax)
print("Monthly Income tax is :\t", round(Income_tax / 2))
print()
print("Bye")









