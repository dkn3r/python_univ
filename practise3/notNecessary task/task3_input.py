

def input_employers():
    info_employers = {}

    while True:
        name = input("Введ. ім'я або 'stop' щоб закінчити: ")

        if name.lower() == 'stop':
            break

        salary = float(input("Введіть зарплатню в грн: "))
        days = int(input("Введіть к-ть відпрацьованих днів: "))
        info_employers[name] = {'salary': salary, 'days': days}

    return info_employers


