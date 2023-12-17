def main():
    rating = {}
    keyExit = True

    def exit(name):
        nonlocal keyExit
        if name.lower() == "stop":
            keyExit = False

    def addMarks(name):
        if name not in rating:
            rating[name] = []
        while True:
            mark = input("Введіть оцінку (або 'stop' щоб завершити введення оцінок для даного студента): ")
            if mark.lower() == "stop":
                break
            if mark.isdigit():
                rating[name].append(mark)

    def result(rating):
        for name, mark in rating.items():
            print(name + ": " + ", ".join(mark))

    while keyExit:
        name = input("Введіть ім'я студента ")
        exit(name)
        if keyExit:
            addMarks(name)
    result(rating)


if __name__ == "__main__":
    main()
