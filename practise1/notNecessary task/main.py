# Введення тексту
import sys

text = input("Введіть текст для аналізу: ")

# Розділити текст на слова
words = text.split(" ")

truncated_sentence = []
count = 0
key = True
# Запускання циклу для перевірки умови задачі
while True:
    # Форматування рядка
    if count != 1:
        print(f"Аналіз тексту: {text}")
        count += 1
    maximumSymbols = int(input("Введіть максимальну кількість символів: "))
    maximumWords = int(input("Введіть максимальну кількість слів: "))
    if maximumSymbols > len(list("".join(text))) or maximumWords > len(words):
        print("Ви вказали кількість слів чи символів більшу, ніж у Вашому тексті! ")
        continue

    else:
        for i in range(maximumWords + 1):
            if len(list("".join(truncated_sentence))) < maximumSymbols or maximumWords > len(truncated_sentence):
                truncated_sentence.append(words[i])
            if len(list("".join(truncated_sentence))) > maximumSymbols or maximumWords < len(truncated_sentence):
                truncated_sentence.pop(-1)
                print(" ".join(truncated_sentence))
                sys.exit()
