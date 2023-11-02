def input_employers():
    info_employers = {}

    while True:
        name = input("Введ. ім'я або 'stop' щоб закінчити: ")

        if name.lower() == 'stop':
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
