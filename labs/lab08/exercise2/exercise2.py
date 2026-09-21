employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

overtime_salary = overtime_hours * 35
gross_salary = base_salary + overtime_salary

if tax_status == "Single" and gross_salary >= 5000:
    tax_rate = 0.22
elif tax_status == "Single" and gross_salary <= 5000:
    tax_rate = 0.18
if tax_status == "Married" and gross_salary >= 6000:
    tax_rate = 0.20
elif tax_status == "Married" and gross_salary <= 6000:
    tax_rate = 0.15
if tax_status == "Head" and gross_salary >= 5500:
    tax_rate = 0.25
elif tax_status == "Head" and gross_salary <= 5500:
    tax_rate = 0.19

#deductions
income_tax = gross_salary * tax_rate
EPF = gross_salary * 0.11
SOCSO = gross_salary * 0.05

net_salary = gross_salary - income_tax - EPF - SOCSO

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")
