from manager import Manager
from empoloyee import Employee
from adress import Adress

addresses_employees = [Adress("Ukraine", "Kyiv", "Solomyanska", "7"),
                       Adress("Ukraine", "Kyiv", "Andriivska", "15"),
                       Adress("Ukraine", "Kyiv", "Solomyanska", "15"),
                       Adress("Ukraine", "Kyiv", "Solomyanska", "15")
                       ]
employees = [Manager('John', 50000, 5, 20, 10, addresses_employees[0]),
             Employee('Angel', 30000, 20, 5, addresses_employees[1]),
             Employee('Bob', 35000, 25, 7, addresses_employees[2]),
             Employee(-1, -1, -1, -1, addresses_employees[3])
             ]

print()
for employee in range(len(employees)):

    if employees[employee].get_name() != -1 and employees[employee].get_salary() != -1 and employees[
        employee].get_days() != -1 and employees[employee].get_bonus_percent() != -1:

        print(employees[employee].addresses_employee())
        print(employees[employee].info_abt_employee())

        if isinstance(employees[employee], Manager):
            print(employees[employee].report(), "\n")
        else:
            print()
    else:
        if employees[employee].get_name() == -1:
            print(f"Error! Name for employee {employee+1} must be a string!")
        if employees[employee].get_salary() == -1:
            print(f"Error! Salary for employee {employee+1} can't be negative!")
        if employees[employee].get_days() == -1:
            print(f"Error! Worked days for employee {employee+1} can't be negative!")
        if employees[employee].get_bonus_percent() == -1:
            print(f"Error! Bonus percent for employee {employee+1} can't be negative!")
