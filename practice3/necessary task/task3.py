from task3_input import input_employers, calculation_salary
from task3_calculation import matrix_employers, output_employers

info_employers = input_employers()
salary_per_month = calculation_salary(info_employers)
matrix_employers_data = matrix_employers(info_employers)
output_employers(matrix_employers_data)
for name, salary in salary_per_month.items():
    print(f"Зарплата {name}: {salary}")