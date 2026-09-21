employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

overtime_salary = overtime_hours * 35
gross_salary = base_salary + overtime_salary

if tax_status == "Single":
    tax_rate = 0.22 if gross_salary >= 5000 else 0.18
elif tax_status == "Married":
    tax_rate = 0.20 if gross_salary >= 6000 else 0.15
elif tax_status == "Head":
    tax_rate = 0.25 if gross_salary >= 5500 else 0.19
else:
    tax_rate = 0.0

#deductions
income_tax = gross_salary * tax_rate
EPF = gross_salary * 0.11
SOCSO = gross_salary * 0.005

net_salary = gross_salary - income_tax - EPF - SOCSO

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")
