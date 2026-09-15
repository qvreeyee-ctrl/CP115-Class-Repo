student_name = input()
gpa = float(input())
credit_hours = int(input())

if gpa >= 3.5 and credit_hours >= 12:
    classification =("Dean's list")
elif gpa >= 3.5 and credit_hours >= 12:
    classification =("Honor Roll")
elif gpa >= 2.0:
    classification =("Good Standing")
else gpa < 2.0:
    classification =("Academic Probation")

print(classification)