def input_employers():
    info_employers = {}

    while True:
        name = input("Введ. ім'я або 'stop' щоб закінчити: ")

        if name.lower() == 'stop':
            print("\n")
            break

        salary = float(input("Введіть зарплатню: "))
        days = int(input("Введіть к-ть відпрацьованих днів: "))
        info_employers[name] = {'salary': salary, 'days': days}

    return info_employers


def calculation_salary(info_employers):
    result_salary = {}
    for name, data in info_employers.items():
        salary_per_month = data['salary'] / 30 * data['days']
        result_salary[name] = salary_per_month
    return result_salary


def matrix_employers(info_employers):
    matrix_name = []
    for name, data in info_employers.items():
        matrix_name.append([name, data['salary'], data['days']])
    return matrix_name


def output_employers(matrix_employers_data, i=0):
    if i == len(matrix_employers_data):
        return
    print(f"Робочий {i + 1}: {matrix_employers_data[i][0]}")
    output_employers(matrix_employers_data, i + 1)


info_employers = input_employers()
salary_per_month = calculation_salary(info_employers)
matrix_employers_data = matrix_employers(info_employers)
output_employers(matrix_employers_data)
for name, salary in salary_per_month.items():
    print(f"Зарплата {name}: {salary}")
