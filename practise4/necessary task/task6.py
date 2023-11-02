from task5 import Manager
from task2 import Employee

employees = [Manager('John', 50000, 5, 20, 10),
             Employee('Angel', 30000, 20, 5),
             Employee('Christian', 35000, 23, 7)
]
print()
for employee in employees:
    print(f"{employee.get_name()}, worked days: {employee.get_days()}, salary: {employee.salary_per_month()},  bonus: {employee.bonus()}")
    if isinstance(employee, Manager):
        print(employee.report(), "\n")


