from task3_input import input_employers
from task3_calculation import matrix_employers, output_employers, currency, usd_eur, calculation_salary

request = usd_eur()

if request.lower() == "usd":
    symbol_currency = "$"
else:
    symbol_currency = "€"

info_employers = input_employers()
currency = currency(request)

salary_per_month = calculation_salary(info_employers)
matrix_employers_data = matrix_employers(info_employers)
output_employers(matrix_employers_data)
for name, salary in salary_per_month.items():
    print(f"Зарплата {name}: {salary}₴ | {symbol_currency}{salary / currency}")
