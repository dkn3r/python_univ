rating = {}
while True:
    name = input("Введіть ім'я студента (або 'stop' щоб переглянути оцінки): ")
    if name.lower() == "stop":
        break
    if name not in rating:
        rating[name] = []
    while True:
        mark = input("Введіть оцінку (або 'stop' щоб завершити введення оцінок для даного студента): ")
        if mark.lower() == "stop":
            break
        rating[name].append(mark)

for name, mark in rating.items():
    print(name + ": " + ", ".join(mark))