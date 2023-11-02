word = list(input("Введіть слово: "))

most_common_letter = max(word, key=word.count)
print("Буква, яка найчастіше зустрічається:", most_common_letter)
print("Кількість входжень цієї букви:", word.count(most_common_letter))