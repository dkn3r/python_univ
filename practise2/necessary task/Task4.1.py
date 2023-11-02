rating = {}
while True:
    name = input("Введіть ім'я студента: ")
    if name.lower() == "stop":
        break
    mark = input("Введіть оцінку: ")
    if mark.lower() == "stop":
        break
    rating[name] = mark
for name,mark in rating.items():
    print(name + " " + mark)