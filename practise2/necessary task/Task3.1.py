from statistics import mean

numbers = list(map(int, input("Введіть числа через кому").split(", ")))
print(f"Список -  {list(numbers)}")
print(f"Кортеж -  {tuple(numbers)}")
print(f"Сума -  {sum(list(numbers))}")
print(f"Середнє арифметичне -  {mean(list(numbers))}")
